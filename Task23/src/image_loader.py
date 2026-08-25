from pathlib import Path

from src.config import (
    DATASET_DIR,
    SUPPORTED_EXTENSIONS,
)


def get_image_paths():
    """
    Return all supported image paths from the dataset directory.
    """

    if not DATASET_DIR.exists():
        raise FileNotFoundError(
            f"Dataset directory does not exist: {DATASET_DIR}"
        )

    image_paths = [
        path
        for path in DATASET_DIR.iterdir()
        if path.is_file()
        and path.suffix.lower() in SUPPORTED_EXTENSIONS
    ]

    image_paths.sort()

    return image_paths


def get_image_count():
    """
    Return the number of images in the dataset.
    """

    return len(get_image_paths())