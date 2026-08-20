import os
import cv2
import csv

from document_enhancer import (
    process_image,
    save_image
)

from ocr_engine import (
    run_ocr,
    draw_ocr_results,
    save_json
)
# CONFIGURATION
INPUT_DIR = "input"
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
COMPARISON_FILE = os.path.join(
    OUTPUT_DIR,
    "comparison.csv"
)
# CREATE DIRECTORIES
for directory in [

    OUTPUT_DIR,
    ENHANCED_DIR,
    RAW_OCR_DIR,
    ENHANCED_OCR_DIR,
    JSON_DIR

]:

    os.makedirs(
        directory,
        exist_ok=True
    )


# OCR COMPARISON
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

        raw_average = sum(
            raw_confidences
        ) / len(raw_confidences)

    else:

        raw_average = 0

    if enhanced_confidences:

        enhanced_average = sum(
            enhanced_confidences
        ) / len(enhanced_confidences)

    else:

        enhanced_average = 0

    return {

        "raw_detections": len(
            raw_detections
        ),

        "enhanced_detections": len(
            enhanced_detections
        ),

        "raw_average_confidence":
            round(raw_average, 2),

        "enhanced_average_confidence":
            round(enhanced_average, 2),

        "confidence_improvement":
            round(
                enhanced_average -
                raw_average,
                2
            )
    }

# PROCESS ONE IMAGE
def process_document(
    image_path
):

    image_name = os.path.basename(
        image_path
    )

    name, _ = os.path.splitext(
        image_name
    )
    print(
        f"Processing: {image_name}"
    )

    # LOAD RAW IMAGE
    raw_image = cv2.imread(
        image_path
    )

    if raw_image is None:

        print(
            f"Could not read: {image_path}"
        )

        return None
    # 1. RAW IMAGE → OCR
    print(
        "Running OCR on RAW image..."
    )
    raw_detections = run_ocr(
        raw_image
    )
    raw_visualization = draw_ocr_results(
        raw_image,
        raw_detections
    )
    raw_visualization_path = os.path.join(
        RAW_OCR_DIR,
        f"{name}_raw_ocr.jpg"
    )

    save_image(
        raw_visualization,
        raw_visualization_path
    )
    # 2. RAW → DOCUMENT ENHANCER
    print(
        "Running document enhancement..."
    )

    enhanced_result = process_image(
        image_path
    )

    enhanced_image = enhanced_result[
        "final"
    ]

    enhanced_image_path = os.path.join(
        ENHANCED_DIR,
        f"{name}_enhanced.jpg"
    )

    save_image(
        enhanced_image,
        enhanced_image_path
    )
    # 3. ENHANCED IMAGE → OCR
    print(
        "Running OCR on ENHANCED image..."
    )

    enhanced_detections = run_ocr(
        enhanced_image
    )

    enhanced_visualization = draw_ocr_results(
        enhanced_image,
        enhanced_detections
    )

    enhanced_visualization_path = os.path.join(
        ENHANCED_OCR_DIR,
        f"{name}_enhanced_ocr.jpg"
    )

    save_image(
        enhanced_visualization,
        enhanced_visualization_path
    )
    # 4. SAVE JSON
    json_data = {

        "image": image_name,

        "deskew_angle": enhanced_result[
            "deskew_angle"
        ],

        "perspective_correction": enhanced_result[
            "contour_found"
        ],

        "raw_ocr": raw_detections,

        "enhanced_ocr": enhanced_detections
    }

    json_path = os.path.join(
        JSON_DIR,
        f"{name}.json"
    )

    import json

    with open(
        json_path,
        "w",
        encoding="utf-8"
    ) as file:

        json.dump(
            json_data,
            file,
            indent=4,
            ensure_ascii=False
        )
    # 5. COMPARE
    comparison = compare_ocr_results(
        raw_detections,
        enhanced_detections
    )

    comparison["image"] = image_name

    comparison["deskew_angle"] = round(
        enhanced_result["deskew_angle"],
        2
    )

    comparison["perspective_corrected"] = (
        enhanced_result["contour_found"]
    )

    print(
        f"Raw detections: "
        f"{comparison['raw_detections']}"
    )

    print(
        f"Enhanced detections: "
        f"{comparison['enhanced_detections']}"
    )

    print(
        f"Raw average confidence: "
        f"{comparison['raw_average_confidence']}%"
    )

    print(
        f"Enhanced average confidence: "
        f"{comparison['enhanced_average_confidence']}%"
    )

    print(
        f"Confidence improvement: "
        f"{comparison['confidence_improvement']}%"
    )

    return comparison
# PROCESS ALL DOCUMENTS
def main():

    image_extensions = (
        ".jpg",
        ".jpeg",
        ".png",
        ".bmp",
        ".tif",
        ".tiff"
    )

    image_files = [

        file

        for file in os.listdir(
            INPUT_DIR
        )

        if file.lower().endswith(
            image_extensions
        )
    ]

    image_files.sort()

    if not image_files:

        print(
            f"No images found in {INPUT_DIR}"
        )

        return


    all_results = []

    for file in image_files:

        image_path = os.path.join(
            INPUT_DIR,
            file
        )

        result = process_document(
            image_path
        )

        if result is not None:

            all_results.append(
                result
            )
    # SAVE COMPARISON CSV
    if all_results:

        fieldnames = [
            "image",
            "raw_detections",
            "enhanced_detections",
            "raw_average_confidence",
            "enhanced_average_confidence",
            "confidence_improvement",
            "deskew_angle",
            "perspective_corrected"
        ]

        with open(
            COMPARISON_FILE,
            "w",
            newline="",
            encoding="utf-8"
        ) as file:

            writer = csv.DictWriter(
                file,
                fieldnames=fieldnames
            )

            writer.writeheader()

            writer.writerows(
                all_results
            )
    print(
        "PROCESSING COMPLETE"
    )
    print(
        f"Results saved in: {OUTPUT_DIR}"
    )

    print(
        f"Comparison file: "
        f"{COMPARISON_FILE}"
    )
if __name__ == "__main__":

    main()