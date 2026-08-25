from typing import Dict, List, Tuple

import numpy as np
from sklearn.metrics.pairwise import cosine_similarity


def calculate_similarity(
    query_embedding: np.ndarray,
    candidate_embedding: np.ndarray,
) -> float:
    """
    Calculate cosine similarity between two image embeddings.

    Returns:
        Similarity score between -1 and 1.
    """

    query_embedding = query_embedding.reshape(1, -1)
    candidate_embedding = candidate_embedding.reshape(1, -1)

    score = cosine_similarity(
        query_embedding,
        candidate_embedding,
    )[0][0]

    return float(score)


def find_top_similar(
    query_name: str,
    embeddings: Dict[str, np.ndarray],
    top_k: int = 5,
) -> List[Tuple[str, float]]:
    """
    Find the top-k most visually similar images
    for a given query image.

    The query image itself is excluded.
    """

    if query_name not in embeddings:
        raise ValueError(
            f"Query image '{query_name}' "
            f"was not found in embeddings."
        )

    query_embedding = embeddings[query_name]

    similarities = []

    for image_name, embedding in embeddings.items():

        # Don't compare image with itself
        if image_name == query_name:
            continue

        score = calculate_similarity(
            query_embedding,
            embedding,
        )

        similarities.append(
            (image_name, score)
        )

    # Highest similarity first
    similarities.sort(
        key=lambda item: item[1],
        reverse=True,
    )

    return similarities[:top_k]