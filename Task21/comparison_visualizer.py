"""
comparison_visualizer.py

Builds the mandatory "raw -> preprocessed -> OCR output" side-by-side
comparison image used for the hardest documents in the batch.
"""

import cv2
import numpy as np


def _to_bgr(image):
    if len(image.shape) == 2:
        return cv2.cvtColor(image, cv2.COLOR_GRAY2BGR)
    return image


def _resize_to_height(image, height):
    h, w = image.shape[:2]
    scale = height / float(h)
    return cv2.resize(image, (int(w * scale), height))


def _add_label(image, label, bg_color=(30, 30, 30), text_color=(255, 255, 255)):

    banner_height = 40

    banner = np.full(
        (banner_height, image.shape[1], 3),
        bg_color,
        dtype=np.uint8
    )

    cv2.putText(
        banner,
        label,
        (10, 28),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.8,
        text_color,
        2,
        cv2.LINE_AA
    )

    return np.vstack([banner, image])


def create_comparison_grid(raw_image, enhanced_image, ocr_image, target_height=500):
    """
    Stacks raw / preprocessed / OCR-annotated images side by side, each
    labeled, for easy before/after inspection.
    """

    raw_resized = _resize_to_height(_to_bgr(raw_image), target_height)
    enhanced_resized = _resize_to_height(_to_bgr(enhanced_image), target_height)
    ocr_resized = _resize_to_height(_to_bgr(ocr_image), target_height)

    raw_labeled = _add_label(raw_resized, "RAW")
    enhanced_labeled = _add_label(enhanced_resized, "PREPROCESSED")
    ocr_labeled = _add_label(ocr_resized, "OCR OUTPUT (FINAL)")

    separator = np.full(
        (raw_labeled.shape[0], 6, 3),
        (200, 200, 200),
        dtype=np.uint8
    )

    grid = np.hstack([
        raw_labeled,
        separator,
        enhanced_labeled,
        separator,
        ocr_labeled
    ])

    return grid