import os
import cv2
import numpy as np
def process_image(image):

    ############ Original
    original = image.copy()

    ############ Grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    ############ Gaussian Blur
    blur = cv2.GaussianBlur(gray, (5, 5), 0)

    ############ Edge Detection
    edges = cv2.Canny(blur, 50, 150)

    ############ Morphological Operation (Closing)
    kernel = np.ones((5, 5), np.uint8)
    morphology = cv2.morphologyEx(edges, cv2.MORPH_CLOSE, kernel)

    ############ Find Largest Contour
    contours, _ = cv2.findContours(morphology,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
    boundary = image.copy()
    if contours:
        largest = max(contours, key=cv2.contourArea)
        cv2.drawContours(boundary,[largest],-1,(0, 255, 0),3)
    return original, edges, morphology, boundary

def main():
    input_folder = "dataset"
    output_folder = "output"
    ############ Create output folders
    original_folder = os.path.join(output_folder, "original")
    edge_folder = os.path.join(output_folder, "edges")
    morphology_folder = os.path.join(output_folder, "morphology")
    boundary_folder = os.path.join(output_folder, "boundary")
    os.makedirs(original_folder, exist_ok=True)
    os.makedirs(edge_folder, exist_ok=True)
    os.makedirs(morphology_folder, exist_ok=True)
    os.makedirs(boundary_folder, exist_ok=True)
    valid_extensions = (".jpg",".jpeg",".png",".bmp",".tif",".tiff")
    processed = 0
    for filename in os.listdir(input_folder):
        if not filename.lower().endswith(valid_extensions):
            continue
        image_path = os.path.join(input_folder, filename)
        image = cv2.imread(image_path)
        if image is None:
            print(f"Could not read {filename}")
            continue
        original, edges, morphology, boundary = process_image(image)
        ############ Save images
        cv2.imwrite(os.path.join(original_folder, filename), original)
        cv2.imwrite(os.path.join(edge_folder, filename), edges)
        cv2.imwrite(os.path.join(morphology_folder, filename), morphology)
        cv2.imwrite(os.path.join(boundary_folder, filename), boundary)
        processed += 1
        print(f"Processed: {filename}")
    print(f"Successfully processed {processed} image(s).")
    print(f"Results saved inside '{output_folder}' folder.")

if __name__ == "__main__":
    main()