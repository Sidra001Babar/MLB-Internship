import cv2
import json
import os
import easyocr
import numpy as np
reader = easyocr.Reader(
    ['en'],
    gpu=True
)
def run_ocr(
    image,
    confidence_threshold=0.0,
    scale_factor=2.0,
    contrast_ths=0.1,
    adjust_contrast=0.6,
    text_threshold=0.6,
    low_text=0.35,
    mag_ratio=1.5,
    width_ths=0.9,
    height_ths=0.7,
    ycenter_ths=0.6,
    slope_ths=0.2,
    add_margin=0.1
):

    if len(image.shape) == 2:

        image_for_ocr = cv2.cvtColor(
            image,
            cv2.COLOR_GRAY2BGR
        )
    else:
        image_for_ocr = image
    if scale_factor and scale_factor != 1.0:

        image_for_ocr = cv2.resize(
            image_for_ocr,
            None,
            fx=scale_factor,
            fy=scale_factor,
            interpolation=cv2.INTER_CUBIC
        )

    results = reader.readtext(
        image_for_ocr,
        contrast_ths=contrast_ths,
        adjust_contrast=adjust_contrast,
        text_threshold=text_threshold,
        low_text=low_text,
        mag_ratio=mag_ratio,
        width_ths=width_ths,
        height_ths=height_ths,
        ycenter_ths=ycenter_ths,
        slope_ths=slope_ths,
        add_margin=add_margin
    )

    detections = []

    for result in results:

        bbox, text, confidence = result

        confidence = float(
            confidence
        )

        if confidence < confidence_threshold:
            continue


        points = [
            [
                int(point[0] / scale_factor),
                int(point[1] / scale_factor)
            ]
            for point in bbox
        ]

        x_coordinates = [
            point[0]
            for point in points
        ]

        y_coordinates = [
            point[1]
            for point in points
        ]

        x1 = min(x_coordinates)
        y1 = min(y_coordinates)

        x2 = max(x_coordinates)
        y2 = max(y_coordinates)

        detections.append({

            "text": text,

            "confidence": round(
                confidence * 100,
                2
            ),

            "bbox": points,

            "coordinates": [
                x1,
                y1,
                x2,
                y2
            ]
        })

    return detections


# DRAW OCR RESULTS
# DRAW OCR RESULTS
def draw_ocr_results(
    image,
    detections
):

    if len(image.shape) == 2:

        output = cv2.cvtColor(
            image,
            cv2.COLOR_GRAY2BGR
        )

    else:

        output = image.copy()

    for detection in detections:

        points = np.array(
            detection["bbox"],
            dtype=np.int32
        )

        confidence = detection["confidence"]

        # Draw OCR bounding box
        cv2.polylines(
            output,
            [points],
            True,
            (0, 255, 0),
            2
        )

        # Get bounding box coordinates
        x1, y1, x2, y2 = detection[
            "coordinates"
        ]

        # Confidence score only
        confidence_label = (
            f"{confidence:.1f}%"
        )

        # Get text size
        (text_w, text_h), baseline = cv2.getTextSize(
            confidence_label,
            cv2.FONT_HERSHEY_SIMPLEX,
            0.5,
            1
        )

        # Position confidence score
        # LEFT side of the bounding box
        confidence_x = x1 - text_w - 8

        # Vertically center it with the bounding box
        confidence_y = (
            y1 + y2
        ) // 2

        # Prevent text from going outside left image boundary
        if confidence_x < 5:
            confidence_x = 5

        cv2.putText(
            output,
            confidence_label,
            (
                confidence_x,
                confidence_y
            ),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.5,
            (255, 0, 0),
            1,
            cv2.LINE_AA
        )

    return output
# SAVE JSON
def save_json(
    detections,
    image_name,
    output_path
):

    data = {

        "image": image_name,

        "detections": detections

    }

    parent = os.path.dirname(
        output_path
    )

    if parent:

        os.makedirs(
            parent,
            exist_ok=True
        )

    with open(
        output_path,
        "w",
        encoding="utf-8"
    ) as file:

        json.dump(
            data,
            file,
            indent=4,
            ensure_ascii=False
        )