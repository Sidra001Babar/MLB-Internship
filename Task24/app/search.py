import json
from pathlib import Path

import numpy as np
import torch
from transformers import (
    CLIPProcessor,
    CLIPModel,
)

from app.config import (
    CLIP_MODEL_NAME,
    DEVICE,
    TOP_K_RESULTS,
    SIMILARITY_DECIMAL_PLACES,
    SEARCH_RESULTS_JSON,
)


class ImageSearchEngine:

    def __init__(
        self,
        image_index,
    ):

        print(
            "Loading CLIP search model..."
        )

        self.device = torch.device(
            DEVICE
        )

        self.processor = (
            CLIPProcessor.from_pretrained(
                CLIP_MODEL_NAME
            )
        )

        self.model = (
            CLIPModel.from_pretrained(
                CLIP_MODEL_NAME
            )
        )

        self.model.to(
            self.device
        )

        self.model.eval()

        self.image_index = image_index

        print(
            "CLIP search model loaded."
        )

    # TEXT EMBEDDING

    def encode_text(
        self,
        query,
    ):
        """
        Convert natural language query
        into a normalized CLIP embedding.
        """

        inputs = self.processor(
            text=[query],
            return_tensors="pt",
            padding=True,
        )

        inputs = {
            key: value.to(
                self.device
            )
            for key, value in inputs.items()
        }

        with torch.no_grad():

            text_outputs = (
                self.model.text_model(
                    input_ids=inputs[
                        "input_ids"
                    ],
                    attention_mask=inputs[
                        "attention_mask"
                    ],
                )
            )

            text_features = (
                text_outputs.pooler_output
            )

            text_features = (
                self.model.text_projection(
                    text_features
                )
            )

        # Normalize embedding
        text_features = (
            text_features
            / (
                text_features.norm(
                    dim=-1,
                    keepdim=True,
                )
                + 1e-12
            )
        )

        return (
            text_features
            .cpu()
            .numpy()[0]
        )

    # LOAD SEARCH HISTORY

    def load_search_history(self):


        if not SEARCH_RESULTS_JSON.exists():

            return []

        try:

            with open(
                SEARCH_RESULTS_JSON,
                "r",
                encoding="utf-8",
            ) as file:

                history = json.load(
                    file
                )

            if isinstance(
                history,
                dict,
            ):

                history = [
                    history
                ]

            return history

        except (
            json.JSONDecodeError,
            OSError,
        ):

            return []

    # SAVE SEARCH HISTORY

    def save_search_history(
        self,
        search_history,
    ):
        """
        Save the complete search history.
        """

        SEARCH_RESULTS_JSON.parent.mkdir(
            parents=True,
            exist_ok=True,
        )

        with open(
            SEARCH_RESULTS_JSON,
            "w",
            encoding="utf-8",
        ) as file:

            json.dump(
                search_history,
                file,
                indent=4,
                ensure_ascii=False,
            )

    # SEARCH

    def search(
        self,
        query,
        top_k=TOP_K_RESULTS,
    ):

        query = query.strip()

        if not query:

            raise ValueError(
                "Search query cannot be empty."
            )

        print()

        print(
            f'Searching for: "{query}"'
        )

        # STEP 1: Encode query

        query_embedding = (
            self.encode_text(
                query
            )
        )

        # STEP 2: Compare query with every image embedding

        results = []

        for record in self.image_index:

            embedding_path = Path(
                record[
                    "embedding_file"
                ]
            )

            image_embedding = np.load(
                embedding_path
            )

            similarity = float(
                np.dot(
                    query_embedding,
                    image_embedding,
                )
            )

            results.append(
                {
                    "image": record[
                        "image"
                    ],
                    "similarity": round(
                        similarity,
                        SIMILARITY_DECIMAL_PLACES,
                    ),
                    "caption": record[
                        "caption"
                    ],
                }
            )

        # STEP 3: Sort by similarity
        results.sort(
            key=lambda item: item[
                "similarity"
            ],
            reverse=True,
        )

        # STEP 4: Keep Top K
        results = results[
            :top_k
        ]

        # STEP 5: Add ranks
        for rank, result in enumerate(
            results,
            start=1,
        ):

            result["rank"] = rank

        # STEP 6: Create current search
        current_search = {
            "query": query,
            "top_k": top_k,
            "results": results,
        }

        # STEP 7: Load previous searches

        search_history = (
            self.load_search_history()
        )
        # STEP 8: Add current search

        search_history.append(
            current_search
        )

        # STEP 9: Save complete history
        self.save_search_history(
            search_history
        )

        print()

        print(
            f"Search history saved: "
            f"{SEARCH_RESULTS_JSON}"
        )

        print(
            f"Total saved queries: "
            f"{len(search_history)}"
        )

        return results