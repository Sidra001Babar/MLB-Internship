from pathlib import Path
from typing import List, Tuple

import matplotlib.pyplot as plt
from PIL import Image


def create_similarity_grid(
    query_path: Path,
    results: List[Tuple[str, float]],
    dataset_dir: Path,
    output_path: Path,
):
    """
    Create and save a grid showing the query image
    and its top similar images.
    """

    # Query + top 5 results
    total_images = len(results) + 1

    fig, axes = plt.subplots(
        1,
        total_images,
        figsize=(20, 5),
    )

    # Query image

    query_image = Image.open(query_path)

    axes[0].imshow(query_image)
    axes[0].set_title(
        f"QUERY\n{query_path.name}",
        fontsize=11,
    )
    axes[0].axis("off")

    # Similar images

    for index, (image_name, score) in enumerate(
        results,
        start=1,
    ):

        image_path = dataset_dir / image_name

        img = Image.open(image_path)

        axes[index].imshow(img)

        axes[index].set_title(
            f"Rank {index}\n"
            f"{image_name}\n"
            f"Similarity: {score:.4f}",
            fontsize=10,
        )

        axes[index].axis("off")

    # Save grid

    plt.tight_layout()

    plt.savefig(
        output_path,
        dpi=150,
        bbox_inches="tight",
    )

    plt.close(fig)

def create_duplicate_grid(
    original_path: Path,
    modified_results: List[dict],
    dataset_dir: Path,
    output_path: Path,
):
    """
    Create a grid for the mandatory duplicate/modified-image test.

    Each modified image displays:
    - CNN cosine similarity
    - pHash Hamming distance
    - duplicate classification
    """

    total_images = len(modified_results) + 1

    fig, axes = plt.subplots(
        1,
        total_images,
        figsize=(20, 5),
    )

    # Original image

    original_image = Image.open(original_path)

    axes[0].imshow(original_image)

    axes[0].set_title(
        f"ORIGINAL\n{original_path.name}",
        fontsize=11,
    )

    axes[0].axis("off")

    # Modified images

    for index, result in enumerate(
        modified_results,
        start=1,
    ):

        image_name = result["image"]

        image_path = dataset_dir / image_name

        img = Image.open(image_path)

        axes[index].imshow(img)

        # Get metrics

        cnn_similarity = result.get(
            "cosine_similarity"
        )

        hamming_distance = result.get(
            "hamming_distance"
        )

        near_duplicate = result.get(
            "near_duplicate"
        )

        # Classification text

        if near_duplicate:

            status = "Near Duplicate: YES"

        else:

            status = "CNN Visual Match: YES"

        # Title

        title = (
            f"{image_name}\n"
            f"CNN: {cnn_similarity:.4f}\n"
            f"pHash Distance: {hamming_distance}\n"
            f"{status}"
        )

        axes[index].set_title(
            title,
            fontsize=10,
        )

        axes[index].axis("off")

    # Save

    plt.tight_layout()

    plt.savefig(
        output_path,
        dpi=150,
        bbox_inches="tight",
    )

    plt.close(fig)