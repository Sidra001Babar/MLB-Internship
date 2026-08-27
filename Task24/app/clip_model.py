import json
from pathlib import Path

import numpy as np
import torch
from PIL import Image
from transformers import (
    CLIPProcessor,
    CLIPModel,
)

from app.config import (
    CLIP_MODEL_NAME,
    DEVICE,
    SUPPORTED_IMAGE_EXTENSIONS,
    EMBEDDINGS_DIR,
)


class CLIPImageEncoder:

    def __init__(self):

        print("Loading CLIP model...")

        self.device = torch.device(DEVICE)

        print(
            f"Using device: {self.device}"
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

        self.model.to(self.device)

        self.model.eval()

        print(
            "CLIP model loaded successfully."
        )

    def generate_embedding(
        self,
        image_path,
    ):
        # Generate a normalized CLIP image embedding.
        image = (
            Image.open(image_path)
            .convert("RGB")
        )

        inputs = self.processor(
            images=image,
            return_tensors="pt",
        )

        inputs = {
            key: value.to(self.device)
            for key, value in inputs.items()
        }

        with torch.no_grad():

            vision_outputs = (
                self.model.vision_model(
                    pixel_values=inputs[
                        "pixel_values"
                    ]
                )
            )

            image_features = (
                vision_outputs.pooler_output
            )

            image_features = (
                self.model.visual_projection(
                    image_features
                )
            )

        image_features = (
            image_features
            / (
                image_features.norm(
                    dim=-1,
                    keepdim=True,
                )
                + 1e-12
            )
        )

        return (
            image_features
            .cpu()
            .numpy()[0]
        )

    def process_folder(
        self,
        input_dir,
        image_records,
    ):
        """
        Generate and save embeddings for
        every image.
        """
        input_dir = Path(input_dir)
        EMBEDDINGS_DIR.mkdir(
            parents=True,
            exist_ok=True,
        )
        image_files = sorted(
            [
                path
                for path in input_dir.iterdir()
                if (
                    path.is_file()
                    and path.suffix.lower()
                    in SUPPORTED_IMAGE_EXTENSIONS
                )
            ]
        )

        print()
        print("CLIP IMAGE EMBEDDING GENERATION")
        results = []

        for index, image_path in enumerate(
            image_files,
            start=1,
        ):

            print(
                f"[{index}/{len(image_files)}] "
                f"{image_path.name}"
            )

            embedding = (
                self.generate_embedding(
                    image_path
                )
            )

            embedding_path = (
                EMBEDDINGS_DIR
                / f"{image_path.stem}.npy"
            )

            np.save(
                embedding_path,
                embedding,
            )

            caption = ""

            for record in image_records:

                if (
                    record["image"]
                    == image_path.name
                ):

                    caption = record[
                        "caption"
                    ]

                    break

            results.append(
                {
                    "image": image_path.name,
                    "caption": caption,
                    "embedding_file": str(
                        embedding_path
                    ),
                    "embedding_dimension": int(
                        embedding.shape[0]
                    ),
                }
            )

            print(
                f"Embedding shape: "
                f"{embedding.shape}"
            )

        return results