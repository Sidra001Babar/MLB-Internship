import os
import cv2
import numpy as np

#################### Load Image
def load_image(image_path):
    return cv2.imread(image_path)

#################### Convert to Grayscale
def convert_to_grayscale(image):
    return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

################### Apply Threshold
def apply_threshold(gray):
    _, threshold = cv2.threshold(gray, 200, 255, cv2.THRESH_BINARY_INV)
    return threshold

################## Detect Contours
def detect_contours(binary_image):
    contours, hierarchy = cv2.findContours(binary_image,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
    return contours

############### Detect Shape
def detect_shape(contour):
    perimeter = cv2.arcLength(contour, True)
    hull = cv2.convexHull(contour)
    approx = cv2.approxPolyDP(hull, 0.02 * cv2.arcLength(hull, True), True)
    sides = len(approx)
    if sides == 3:
        return "Triangle"
    elif sides == 4:
        # Distinguish Square and Rectangle
        x, y, w, h = cv2.boundingRect(approx)
        aspect_ratio = w / float(h)
        if 0.95 <= aspect_ratio <= 1.05:
            return "Square"
        else:
            return "Rectangle"
    elif sides == 5:
        return "Pentagon"
    elif sides == 6:
        return "Hexagon"
    else:
        return "Circle"
################## Draw Contours and Labels
def draw_shapes(image, contours):
    output = image.copy()
    for contour in contours:
        area = cv2.contourArea(contour)
        if area < 100:
            continue
        perimeter = cv2.arcLength(contour, True)
        shape = detect_shape(contour)
        cv2.drawContours(output, [contour], -1, (0, 255, 0), 2)
        # Bounding Rectangle
        x, y, w, h = cv2.boundingRect(contour)
        cv2.rectangle(output, (x, y), (x + w, y + h), (255, 0, 0), 2)
        # Shape Label
        cv2.putText(output,shape,(x, y - 40),cv2.FONT_HERSHEY_SIMPLEX,0.6,(0, 0, 255),2)
    return output


################## Draw Only Contours
def draw_contours(image, contours):
    contour_image = image.copy()
    cv2.drawContours(contour_image,contours,-1,(0, 255, 0),2)
    return contour_image

#################### Save Images
def save_images(filename,original,contour_image,final_image,output_folder):
    name = os.path.splitext(filename)[0]
    cv2.imwrite(
        os.path.join(output_folder, f"{name}_original.png"),
        original
    )
    cv2.imwrite(
        os.path.join(output_folder, f"{name}_contours.png"),
        contour_image
    )
    cv2.imwrite(
        os.path.join(output_folder, f"{name}_shapes.png"),
        final_image
    )

###################### Process One Image
def process_image(image_path, output_folder):
    filename = os.path.basename(image_path)
    image = load_image(image_path)
    if image is None:
        print(f"Cannot read {filename}")
        return
    gray = convert_to_grayscale(image)
    threshold = apply_threshold(gray)
    contours = detect_contours(threshold)
    contour_image = draw_contours(image, contours)
    final_image = draw_shapes(image, contours)
    save_images(filename,image,contour_image,final_image,output_folder)
    print(f"Processed: {filename}")

##################### Process Folder
def process():
    input_folder = "inputImages"
    output_folder = "outputImages"
    os.makedirs(output_folder, exist_ok=True)
    valid_extensions = (".jpg",".jpeg",".png",".bmp",".tif",".tiff"
    )
    images = [
        file
        for file in os.listdir(input_folder)
        if file.lower().endswith(valid_extensions)
    ]
    print(f"Total Images Found: {len(images)}")
    for image_name in images:
        image_path = os.path.join(input_folder, image_name)
        process_image(image_path,output_folder)
    print("Processing Completed.")

#################### Main
if __name__ == "__main__":
    process()