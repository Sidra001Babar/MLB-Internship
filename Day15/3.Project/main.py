import os
import cv2
import numpy as np
from doc_enhancer import process_image


############ Resize image while keeping aspect ratio
def resize_height(image, height=500):

    h, w = image.shape[:2]

    scale = height / h

    width = int(w * scale)

    return cv2.resize(image, (width, height))


###################### Convert grayscale image to BGR
def to_bgr(image):

    if len(image.shape) == 2:
        return cv2.cvtColor(image, cv2.COLOR_GRAY2BGR)

    return image


################ Put title on image
def add_title(image, text):

    img = image.copy()

    cv2.putText(
        img,
        text,
        (20, 35),
        cv2.FONT_HERSHEY_SIMPLEX,
        1,
        (0, 0, 255),
        2,
        cv2.LINE_AA,
    )

    return img


###################### Create comparison image
def create_comparison(original, corrected, final):

    original = resize_height(to_bgr(original))
    corrected = resize_height(to_bgr(corrected))
    final = resize_height(to_bgr(final))

    max_height = max(
        original.shape[0],
        corrected.shape[0],
        final.shape[0]
    )

    def pad(img):

        h, w = img.shape[:2]

        if h < max_height:

            pad = np.full(
                (max_height - h, w, 3),
                255,
                dtype=np.uint8,
            )

            img = np.vstack((img, pad))

        return img

    original = pad(original)
    corrected = pad(corrected)
    final = pad(final)

    original = add_title(original, "Original")
    corrected = add_title(corrected, "Perspective")
    final = add_title(final, "Enhanced")

    comparison = cv2.hconcat(
        [original, corrected, final]
    )

    return comparison


############## Main
def main():

    input_folder = "dataset"
    output_folder = "output"

    os.makedirs(output_folder, exist_ok=True)

    extensions = (".jpg", ".jpeg", ".png", ".bmp", ".tif", ".tiff")

    images = [
        file
        for file in os.listdir(input_folder)
        if file.lower().endswith(extensions)
    ]

    if len(images) == 0:
        print("No images found.")
        return

    print(f"Found {len(images)} images\n")

    for image_name in images:

        print(f"Processing {image_name}")

        input_path = os.path.join(input_folder, image_name)

        results = process_image(input_path)

        name = os.path.splitext(image_name)[0]

        save_folder = os.path.join(output_folder, name)

        os.makedirs(save_folder, exist_ok=True)

        # Save Original
        cv2.imwrite(
            os.path.join(save_folder, "1_original.jpg"),
            results["original"],
        )

        # Save Perspective Corrected
        cv2.imwrite(
            os.path.join(save_folder, "2_perspective.jpg"),
            results["perspective_corrected"],
        )

        # Save Final Enhanced
        cv2.imwrite(
            os.path.join(save_folder, "3_final.jpg"),
            results["final"],
        )

        # Comparison
        comparison = create_comparison(
            results["original"],
            results["perspective_corrected"],
            results["final"],
        )

        cv2.imwrite(
            os.path.join(save_folder, "comparison.jpg"),
            comparison,
        )

    print("\nProcessing Completed!")
    print(f"Results saved in '{output_folder}'")


if __name__ == "__main__":
    main()