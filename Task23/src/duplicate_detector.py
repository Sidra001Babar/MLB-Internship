from pathlib import Path
from typing import Dict, List
import imagehash
from PIL import Image
from src.config import PHASH_THRESHOLD

def calculate_phash(image_path: Path) -> imagehash.ImageHash:
    """
    Calculate the perceptual hash of an image.
    """
    with Image.open(image_path) as img:
        img = img.convert("RGB")

        return imagehash.phash(img)


def calculate_hamming_distance(
    hash1: imagehash.ImageHash,
    hash2: imagehash.ImageHash,
) -> int:
    """
    Calculate the Hamming distance between two
    perceptual hashes.
    """
    return hash1 - hash2

def is_near_duplicate(
    distance: int,
    threshold: int = PHASH_THRESHOLD,
) -> bool:
    """
    Determine whether two images are near-duplicates
    based on their perceptual hash distance.
    """
    return distance <= threshold


def generate_hashes(
    image_paths: List[Path],
) -> Dict[str, imagehash.ImageHash]:
    """
    Generate perceptual hashes for all images.
    """

    hashes = {}

    for image_path in image_paths:

        image_hash = calculate_phash(image_path)

        hashes[image_path.name] = image_hash
    return hashes

def find_duplicates(
    image_paths: List[Path],
    threshold: int = PHASH_THRESHOLD,
):
    """
    Compare every unique pair of images and return
    pairs that are considered near-duplicates.
    """
    hashes = generate_hashes(image_paths)
    duplicate_pairs = []
    for i in range(len(image_paths)):
        image1 = image_paths[i].name
        hash1 = hashes[image1]
        for j in range(i + 1, len(image_paths)):
            image2 = image_paths[j].name
            hash2 = hashes[image2]
            distance = calculate_hamming_distance(
                hash1,
                hash2,
            )
            if distance <= threshold:
                duplicate_pairs.append(
                    {
                        "image_1": image1,
                        "image_2": image2,
                        "hamming_distance": distance,
                    }
                )

    return duplicate_pairs

def compare_specific_images(
    image_path_1: Path,
    image_path_2: Path,
):
    """
    Calculate and return the pHash distance between
    two specific images.
    """

    hash1 = calculate_phash(image_path_1)
    hash2 = calculate_phash(image_path_2)

    distance = calculate_hamming_distance(
        hash1,
        hash2,
    )

    return {
        "image_1": image_path_1.name,
        "image_2": image_path_2.name,
        "hash_1": str(hash1),
        "hash_2": str(hash2),
        "hamming_distance": distance,
        "near_duplicate": is_near_duplicate(
            distance
        ),
    }