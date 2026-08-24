"""
ground_truth.py

Adds ground-truth based accuracy evaluation to the OCR pipeline.

Usage:
    Create a plain text file for each input image containing the exact
    text that appears on the document, e.g.:

        ground_truth/
            receipt1.txt      <- matches input/receipt1.jpg
            resume_sophia.txt <- matches input/resume_sophia.png

    If a ground truth file exists for an image, the pipeline will compute
    Character Error Rate (CER), Word Error Rate (WER), and derived
    accuracy percentages for the RAW OCR result, the ENHANCED OCR result,
    and the FINAL (selected) OCR result.

    If no ground truth file exists for an image, the pipeline simply
    skips ground-truth evaluation for that image (confidence-based
    comparison still runs as before).
"""

import os
import re


# ============================================================
# LOAD GROUND TRUTH
# ============================================================

def load_ground_truth(image_name, gt_dir="ground_truth"):
    """
    Looks for a ground truth text file matching the given image base name
    (without extension). Returns the file contents as a string, or None
    if no ground truth file is found.
    """

    path = os.path.join(gt_dir, f"{image_name}.txt")

    if not os.path.isfile(path):
        return None

    with open(path, "r", encoding="utf-8") as file:
        return file.read()


# ============================================================
# TEXT NORMALIZATION
# ============================================================

def normalize_text(text):
    """
    Lowercases, strips punctuation, and collapses whitespace so that
    OCR output and ground truth can be compared fairly.
    """

    text = text.lower()
    text = re.sub(r"[^\w\s]", "", text)
    text = re.sub(r"\s+", " ", text).strip()

    return text


# ============================================================
# CONVERT DETECTIONS TO READING-ORDER TEXT
# ============================================================

def detections_to_text(detections):
    """
    Joins individual OCR detections into a single block of text, ordered
    roughly top-to-bottom, left-to-right using each detection's bounding
    box coordinates.
    """

    sorted_detections = sorted(
        detections,
        key=lambda detection: (
            detection["coordinates"][1],
            detection["coordinates"][0]
        )
    )

    return " ".join(
        detection["text"]
        for detection in sorted_detections
    )


# ============================================================
# LEVENSHTEIN (EDIT) DISTANCE
# ============================================================

def _levenshtein(seq_a, seq_b):

    n = len(seq_a)
    m = len(seq_b)

    if n == 0:
        return m

    if m == 0:
        return n

    previous_row = list(range(m + 1))

    for i in range(1, n + 1):

        current_row = [i] + [0] * m

        for j in range(1, m + 1):

            cost = 0 if seq_a[i - 1] == seq_b[j - 1] else 1

            current_row[j] = min(
                previous_row[j] + 1,       # deletion
                current_row[j - 1] + 1,    # insertion
                previous_row[j - 1] + cost  # substitution
            )

        previous_row = current_row

    return previous_row[m]


# ============================================================
# CHARACTER ERROR RATE
# ============================================================

def character_error_rate(ground_truth_text, hypothesis_text):

    gt = normalize_text(ground_truth_text)
    hyp = normalize_text(hypothesis_text)

    if len(gt) == 0:
        return 0.0 if len(hyp) == 0 else 1.0

    distance = _levenshtein(gt, hyp)

    return distance / len(gt)


# ============================================================
# WORD ERROR RATE
# ============================================================

def word_error_rate(ground_truth_text, hypothesis_text):

    gt_words = normalize_text(ground_truth_text).split()
    hyp_words = normalize_text(hypothesis_text).split()

    if len(gt_words) == 0:
        return 0.0 if len(hyp_words) == 0 else 1.0

    distance = _levenshtein(gt_words, hyp_words)

    return distance / len(gt_words)


# ============================================================
# EVALUATE A SET OF DETECTIONS AGAINST GROUND TRUTH
# ============================================================

def evaluate_against_ground_truth(detections, ground_truth_text):
    """
    Compares OCR detections against ground truth text and returns
    CER, WER, and accuracy percentages.
    """

    hypothesis_text = detections_to_text(detections)

    cer = character_error_rate(ground_truth_text, hypothesis_text)
    wer = word_error_rate(ground_truth_text, hypothesis_text)

    character_accuracy = max(0.0, 1.0 - cer) * 100
    word_accuracy = max(0.0, 1.0 - wer) * 100

    return {
        "extracted_text": hypothesis_text,
        "character_error_rate": round(cer, 4),
        "word_error_rate": round(wer, 4),
        "character_accuracy": round(character_accuracy, 2),
        "word_accuracy": round(word_accuracy, 2)
    }