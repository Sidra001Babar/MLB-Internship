import os
import cv2
import csv
import json

from document_enhancer import (
    process_image,
    save_image
)

from ocr_engine import (
    run_ocr,
    draw_ocr_results
)

from ground_truth import (
    load_ground_truth,
    detections_to_text,
    evaluate_against_ground_truth
)

from comparison_visualizer import (
    create_comparison_grid
)


# ============================================================
# CONFIGURATION
# ============================================================

INPUT_DIR = "input"

GROUND_TRUTH_DIR = "ground_truth"

OUTPUT_DIR = "output"

ENHANCED_DIR = os.path.join(
    OUTPUT_DIR,
    "enhanced"
)

RAW_OCR_DIR = os.path.join(
    OUTPUT_DIR,
    "raw_ocr"
)

ENHANCED_OCR_DIR = os.path.join(
    OUTPUT_DIR,
    "enhanced_ocr"
)

JSON_DIR = os.path.join(
    OUTPUT_DIR,
    "json"
)

TEXT_DIR = os.path.join(
    OUTPUT_DIR,
    "text"
)

HARDEST_DIR = os.path.join(
    OUTPUT_DIR,
    "hardest_comparisons"
)

COMPARISON_FILE = os.path.join(
    OUTPUT_DIR,
    "comparison.csv"
)

# How many of the toughest documents get a full before/after grid saved.
NUM_HARDEST_TO_VISUALIZE = 3


# ============================================================
# CREATE DIRECTORIES
# ============================================================

for directory in [

    OUTPUT_DIR,

    ENHANCED_DIR,

    RAW_OCR_DIR,

    ENHANCED_OCR_DIR,

    JSON_DIR,

    TEXT_DIR,

    HARDEST_DIR,

    GROUND_TRUTH_DIR

]:

    os.makedirs(
        directory,
        exist_ok=True
    )


# ============================================================
# OCR COMPARISON (confidence-based, unchanged from before)
# ============================================================

def compare_ocr_results(
    raw_detections,
    enhanced_detections
):

    raw_confidences = [
        detection["confidence"]
        for detection in raw_detections
    ]

    enhanced_confidences = [
        detection["confidence"]
        for detection in enhanced_detections
    ]

    if raw_confidences:
        raw_average = sum(raw_confidences) / len(raw_confidences)
    else:
        raw_average = 0

    if enhanced_confidences:
        enhanced_average = sum(enhanced_confidences) / len(enhanced_confidences)
    else:
        enhanced_average = 0

    confidence_improvement = enhanced_average - raw_average

    raw_count = len(raw_detections)
    enhanced_count = len(enhanced_detections)

    if raw_count > 0:
        detection_ratio = enhanced_count / raw_count
    else:
        detection_ratio = 0

    # Case 1: Enhanced image produced no detections.
    if enhanced_count == 0:
        selected_result = "raw"
        reason = "Enhanced preprocessing produced no OCR detections."

    # Case 2: Raw image produced no detections.
    elif raw_count == 0:
        selected_result = "enhanced"
        reason = "Raw image produced no OCR detections."

    # Case 3: Enhanced preprocessing removed more than 30% of detections.
    elif detection_ratio < 0.70:
        selected_result = "raw"
        reason = "Enhanced preprocessing removed too many OCR detections."

    # Case 4: Enhanced image has better confidence, without excessive loss.
    elif enhanced_average > raw_average:
        selected_result = "enhanced"
        reason = "Enhanced image improved OCR confidence without excessive detection loss."

    # Case 5: Enhanced image did not improve OCR.
    else:
        selected_result = "raw"
        reason = "Enhanced image did not improve OCR confidence."

    return {
        "raw_detections": raw_count,
        "enhanced_detections": enhanced_count,
        "raw_average_confidence": round(raw_average, 2),
        "enhanced_average_confidence": round(enhanced_average, 2),
        "confidence_improvement": round(confidence_improvement, 2),
        "detection_ratio": round(detection_ratio, 2),
        "selected_result": selected_result,
        "preprocessing_applied": selected_result == "enhanced",
        "selection_reason": reason
    }


# ============================================================
# DIFFICULTY SCORE (used to auto-pick the "hardest" documents)
# ============================================================

def compute_difficulty_score(result):
    """
    Higher score = harder document. Prefers ground-truth character
    accuracy (most reliable) when available, otherwise falls back to
    raw OCR confidence as a proxy for difficulty.
    """

    if result.get("ground_truth_available"):
        return 100 - result.get("raw_char_accuracy", 0)

    return 100 - result.get("raw_average_confidence", 100)


# ============================================================
# PROCESS ONE IMAGE
# ============================================================

def process_document(image_path):

    image_name = os.path.basename(image_path)
    name, _ = os.path.splitext(image_name)

    print(f"Processing: {image_name}")

    raw_image = cv2.imread(image_path)

    if raw_image is None:
        print(f"Could not read: {image_path}")
        return None

    # ========================================================
    # 1. RAW IMAGE -> OCR
    # ========================================================

    print("Running OCR on RAW image...")

    raw_detections = run_ocr(raw_image)

    raw_visualization = draw_ocr_results(raw_image, raw_detections)

    raw_visualization_path = os.path.join(RAW_OCR_DIR, f"{name}_raw_ocr.jpg")

    save_image(raw_visualization, raw_visualization_path)

    # ========================================================
    # 2. RAW IMAGE -> DOCUMENT ENHANCEMENT
    # ========================================================

    print("Running document enhancement...")

    enhanced_result = process_image(image_path)

    enhanced_image = enhanced_result["final"]

    enhanced_image_path = os.path.join(ENHANCED_DIR, f"{name}_enhanced.jpg")

    save_image(enhanced_image, enhanced_image_path)

    # ========================================================
    # 3. ENHANCED IMAGE -> OCR
    # ========================================================

    print("Running OCR on ENHANCED image...")

    enhanced_detections = run_ocr(enhanced_image)

    enhanced_visualization = draw_ocr_results(enhanced_image, enhanced_detections)

    enhanced_visualization_path = os.path.join(
        ENHANCED_OCR_DIR,
        f"{name}_enhanced_ocr.jpg"
    )

    save_image(enhanced_visualization, enhanced_visualization_path)

    # ========================================================
    # 4. COMPARE RAW VS ENHANCED OCR (confidence-based)
    # ========================================================

    comparison = compare_ocr_results(raw_detections, enhanced_detections)

    comparison["image"] = image_name
    comparison["deskew_angle"] = round(enhanced_result["deskew_angle"], 2)
    comparison["perspective_corrected"] = enhanced_result["contour_found"]

    # ========================================================
    # 5. SELECT BEST OCR RESULT (confidence-based decision)
    # ========================================================

    if comparison["selected_result"] == "enhanced":
        final_detections = enhanced_detections
        final_image = enhanced_image
        print("Using ENHANCED image for final OCR.")
    else:
        final_detections = raw_detections
        final_image = raw_image
        print("Reverting to RAW image for final OCR.")

    # ========================================================
    # 6. SAVE FINAL OCR VISUALIZATION
    # ========================================================

    final_visualization = draw_ocr_results(final_image, final_detections)

    final_visualization_path = os.path.join(OUTPUT_DIR, f"{name}_final_ocr.jpg")

    save_image(final_visualization, final_visualization_path)

    # ========================================================
    # 7. SAVE EXTRACTED TEXT (.txt)
    # ========================================================

    final_text = detections_to_text(final_detections)

    text_path = os.path.join(TEXT_DIR, f"{name}.txt")

    with open(text_path, "w", encoding="utf-8") as file:
        file.write(final_text)

    # ========================================================
    # 8. GROUND TRUTH EVALUATION (new)
    # ========================================================

    ground_truth_text = load_ground_truth(name, GROUND_TRUTH_DIR)
    ground_truth_available = ground_truth_text is not None

    raw_gt_eval = None
    enhanced_gt_eval = None
    final_gt_eval = None

    if ground_truth_available:

        raw_gt_eval = evaluate_against_ground_truth(raw_detections, ground_truth_text)
        enhanced_gt_eval = evaluate_against_ground_truth(enhanced_detections, ground_truth_text)
        final_gt_eval = evaluate_against_ground_truth(final_detections, ground_truth_text)

        gt_best_choice = (
            "enhanced"
            if enhanced_gt_eval["character_accuracy"] >= raw_gt_eval["character_accuracy"]
            else "raw"
        )

        comparison["ground_truth_available"] = True
        comparison["raw_char_accuracy"] = raw_gt_eval["character_accuracy"]
        comparison["raw_word_accuracy"] = raw_gt_eval["word_accuracy"]
        comparison["enhanced_char_accuracy"] = enhanced_gt_eval["character_accuracy"]
        comparison["enhanced_word_accuracy"] = enhanced_gt_eval["word_accuracy"]
        comparison["final_char_accuracy"] = final_gt_eval["character_accuracy"]
        comparison["final_word_accuracy"] = final_gt_eval["word_accuracy"]
        comparison["ground_truth_best_choice"] = gt_best_choice
        comparison["selection_matches_ground_truth"] = (
            gt_best_choice == comparison["selected_result"]
        )

        print(
            f"Ground truth found. Raw char accuracy: "
            f"{raw_gt_eval['character_accuracy']}% | "
            f"Enhanced char accuracy: {enhanced_gt_eval['character_accuracy']}%"
        )

    else:

        comparison["ground_truth_available"] = False
        comparison["raw_char_accuracy"] = ""
        comparison["raw_word_accuracy"] = ""
        comparison["enhanced_char_accuracy"] = ""
        comparison["enhanced_word_accuracy"] = ""
        comparison["final_char_accuracy"] = ""
        comparison["final_word_accuracy"] = ""
        comparison["ground_truth_best_choice"] = ""
        comparison["selection_matches_ground_truth"] = ""

        print(
            f"No ground truth file found for {image_name} "
            f"(expected {GROUND_TRUTH_DIR}/{name}.txt) — skipping accuracy scoring."
        )

    # Keep paths around so main() can build hardest-image comparisons later.
    comparison["raw_image_path"] = image_path
    comparison["enhanced_image_path"] = enhanced_image_path
    comparison["final_ocr_visualization_path"] = final_visualization_path

    # ========================================================
    # 9. SAVE JSON
    # ========================================================

    json_data = {

        "image": image_name,

        "deskew_angle": enhanced_result["deskew_angle"],

        "perspective_correction": enhanced_result["contour_found"],

        "raw_ocr": raw_detections,

        "enhanced_ocr": enhanced_detections,

        "final_ocr": final_detections,

        "ocr_selection": comparison["selected_result"],

        "preprocessing_applied": comparison["preprocessing_applied"],

        "selection_reason": comparison["selection_reason"],

        "raw_average_confidence": comparison["raw_average_confidence"],

        "enhanced_average_confidence": comparison["enhanced_average_confidence"],

        "confidence_improvement": comparison["confidence_improvement"],

        "raw_detections_count": comparison["raw_detections"],

        "enhanced_detections_count": comparison["enhanced_detections"],

        "detection_ratio": comparison["detection_ratio"],

        "final_extracted_text": final_text,

        "ground_truth": {

            "available": ground_truth_available,

            "raw": raw_gt_eval,

            "enhanced": enhanced_gt_eval,

            "final": final_gt_eval,

            "best_choice": comparison["ground_truth_best_choice"],

            "selection_matches_ground_truth": comparison["selection_matches_ground_truth"]
        }
    }

    json_path = os.path.join(JSON_DIR, f"{name}.json")

    with open(json_path, "w", encoding="utf-8") as file:
        json.dump(json_data, file, indent=4, ensure_ascii=False)

    # ========================================================
    # 10. PRINT SUMMARY
    # ========================================================

    print(f"Raw detections: {comparison['raw_detections']}")
    print(f"Enhanced detections: {comparison['enhanced_detections']}")
    print(f"Raw average confidence: {comparison['raw_average_confidence']}%")
    print(f"Enhanced average confidence: {comparison['enhanced_average_confidence']}%")
    print(f"Confidence improvement: {comparison['confidence_improvement']}%")
    print(f"Detection retention ratio: {comparison['detection_ratio']}")
    print(f"Selected result: {comparison['selected_result']}")
    print(f"Reason: {comparison['selection_reason']}")

    if ground_truth_available and not comparison["selection_matches_ground_truth"]:
        print(
            "NOTE: confidence-based selection differs from what ground truth "
            "says is more accurate for this image."
        )

    print()

    return comparison


# ============================================================
# BUILD BEFORE/AFTER GRIDS FOR THE HARDEST DOCUMENTS
# ============================================================

def save_hardest_comparisons(all_results, count=NUM_HARDEST_TO_VISUALIZE):

    if not all_results:
        return

    hardest = sorted(
        all_results,
        key=compute_difficulty_score,
        reverse=True
    )[:count]

    for rank, result in enumerate(hardest, start=1):

        raw_img = cv2.imread(result["raw_image_path"])
        enhanced_img = cv2.imread(result["enhanced_image_path"])
        ocr_img = cv2.imread(result["final_ocr_visualization_path"])

        if raw_img is None or enhanced_img is None or ocr_img is None:
            print(f"Skipping hardest-image comparison for {result['image']} (missing file).")
            continue

        grid = create_comparison_grid(raw_img, enhanced_img, ocr_img)

        base_name, _ = os.path.splitext(result["image"])

        out_name = f"hardest_{rank}_{base_name}.jpg"

        save_image(grid, os.path.join(HARDEST_DIR, out_name))

        print(f"Saved hardest-document comparison ({rank}/{count}): {out_name}")


# ============================================================
# PROCESS ALL DOCUMENTS
# ============================================================

def main():

    image_extensions = (
        ".jpg", ".jpeg", ".png", ".bmp", ".tif", ".tiff"
    )

    image_files = [
        file
        for file in os.listdir(INPUT_DIR)
        if file.lower().endswith(image_extensions)
    ]

    image_files.sort()

    if not image_files:
        print(f"No images found in {INPUT_DIR}")
        return

    all_results = []

    for file in image_files:

        image_path = os.path.join(INPUT_DIR, file)

        result = process_document(image_path)

        if result is not None:
            all_results.append(result)

    # ========================================================
    # SAVE COMPARISON CSV
    # ========================================================

    if all_results:

        fieldnames = [
            "image",
            "raw_detections",
            "enhanced_detections",
            "raw_average_confidence",
            "enhanced_average_confidence",
            "confidence_improvement",
            "detection_ratio",
            "selected_result",
            "preprocessing_applied",
            "selection_reason",
            "deskew_angle",
            "perspective_corrected",
            "ground_truth_available",
            "raw_char_accuracy",
            "raw_word_accuracy",
            "enhanced_char_accuracy",
            "enhanced_word_accuracy",
            "final_char_accuracy",
            "final_word_accuracy",
            "ground_truth_best_choice",
            "selection_matches_ground_truth"
        ]

        with open(COMPARISON_FILE, "w", newline="", encoding="utf-8") as file:

            writer = csv.DictWriter(
                file,
                fieldnames=fieldnames,
                extrasaction="ignore"
            )

            writer.writeheader()
            writer.writerows(all_results)

    # ========================================================
    # AUTO-GENERATE BEFORE/AFTER GRIDS FOR THE HARDEST DOCS
    # ========================================================

    save_hardest_comparisons(all_results)

    print("PROCESSING COMPLETE")
    print(f"Results saved in: {OUTPUT_DIR}")
    print(f"Comparison file: {COMPARISON_FILE}")
    print(f"Extracted text files: {TEXT_DIR}")
    print(f"Hardest-document comparisons: {HARDEST_DIR}")


if __name__ == "__main__":
    main()