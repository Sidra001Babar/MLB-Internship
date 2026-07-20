import cv2
import os
import numpy as np

############### Output Folder
OUTPUT_FOLDER = "processed_images"
os.makedirs(OUTPUT_FOLDER, exist_ok=True)

image = None
processed = None


########## Display Image

def showImage(title, img):
    cv2.imshow(title, img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

############ Image loaded check
def checkImage():
    global processed

    if processed is None:
        print("\nPlease load an image first!\n")
        return False

    return True


################ Load Image
def loadImage():
    global image, processed
    path = input("Enter Image Path: ")
    image = cv2.imread(path)
    if image is None:
        print("\nImage not found!\n")
        return
    processed = image.copy()
    print("\nImage Loaded Successfully.\n")
    showImage("Original Image", processed)


########### Convert to Grayscale
def grayscale():
    global processed
    if not checkImage():
        return
    processed = cv2.cvtColor(processed, cv2.COLOR_BGR2GRAY)
    print("\nConverted to Grayscale.\n")
    showImage("Grayscale", processed)


##############Resize Image
def resize():
    global processed
    if not checkImage():
        return
    width = int(input("Enter Width: "))
    height = int(input("Enter Height: "))
    processed = cv2.resize(processed, (width, height))
    print("\nResized Successfully.\n")
    showImage("Resized Image", processed)


############ Rotate Image
def rotate():
    global processed
    if not checkImage():
        return
    print("\n1. Rotate 90°")
    print("2. Rotate 180°")
    print("3. Rotate 270°")
    choice = input("Enter Choice: ")
    if choice == "1":
        processed = cv2.rotate(processed, cv2.ROTATE_90_CLOCKWISE)

    elif choice == "2":
        processed = cv2.rotate(processed, cv2.ROTATE_180)

    elif choice == "3":
        processed = cv2.rotate(processed, cv2.ROTATE_90_COUNTERCLOCKWISE)

    else:
        print("Invalid Choice")
        return
    print("\nRotation Completed.\n")
    showImage("Rotated Image", processed)


#################### Flip Image
def flip():
    global processed
    if not checkImage():
        return
    print("\n1. Horizontal Flip")
    print("2. Vertical Flip")
    choice = input("Enter Choice: ")
    if choice == "1":
        processed = cv2.flip(processed, 1)
    elif choice == "2":
        processed = cv2.flip(processed, 0)
    else:
        print("Invalid Choice")
        return
    print("\nFlip Completed.\n")
    showImage("Flipped Image", processed)


################ Crop Image
def crop():
    global processed
    if not checkImage():
        return
    x = int(input("Starting X: "))
    y = int(input("Starting Y: "))
    width = int(input("Crop Width: "))
    height = int(input("Crop Height: "))
    processed = processed[y:y+height, x:x+width]
    print("\nImage Cropped Successfully.\n")
    showImage("Cropped Image", processed)

############## Draw Shapes
def draw_shapes():
    global processed
    if not checkImage():
        return
    # Convert grayscale to BGR if needed
    if len(processed.shape) == 2:
        processed = cv2.cvtColor(processed, cv2.COLOR_GRAY2BGR)
    h, w = processed.shape[:2]

    # Rectangle
    cv2.rectangle(processed, (30, 30), (200, 150), (0, 255, 0), 3)
    # Circle
    cv2.circle(processed, (w // 2, h // 2), 60, (255, 0, 0), 3)
    # Line
    cv2.line(processed, (0, 0), (w, h), (0, 0, 255), 3)
    # Polygon
    points = np.array(
        [[250, 50], [350, 100], [300, 220], [180, 170]],
        np.int32
    )
    points = points.reshape((-1, 1, 2))
    cv2.polylines(processed, [points], True, (255, 255, 0), 3)
    print("\nShapes Drawn Successfully.\n")
    showImage("Shapes", processed)


############ Add Custom Text
def add_text():
    global processed
    if not checkImage():
        return
    if len(processed.shape) == 2:
        processed = cv2.cvtColor(processed, cv2.COLOR_GRAY2BGR)
    name = input("Enter Your Name: ")
    date = input("Enter Today's Date: ")
    cv2.putText(
        processed,
        name,
        (20, 40),
        cv2.FONT_HERSHEY_SIMPLEX,
        1,
        (255, 0, 255),
        2
    )

    cv2.putText(
        processed,
        date,
        (20, 80),
        cv2.FONT_HERSHEY_SIMPLEX,
        1,
        (0, 255, 255),
        2
    )

    print("\nText Added Successfully.\n")
    showImage("Text Added", processed)


################ Brightness
def brightness():
    global processed
    if not checkImage():
        return
    value = int(input("Brightness (-100 to 100): "))
    processed = cv2.convertScaleAbs(
        processed,
        alpha=1,
        beta=value
    )
    print("\nBrightness Adjusted.\n")
    showImage("Brightness", processed)


################### Contrast
def contrast():
    global processed
    if not checkImage():
        return
    alpha = float(input("Contrast (1.0 - 3.0): "))
    processed = cv2.convertScaleAbs(
        processed,
        alpha=alpha,
        beta=0
    )
    print("\nContrast Adjusted.\n")
    showImage("Contrast", processed)

############# RGB Comparison
def rgb_compare():
    if not checkImage():
        return
    if len(processed.shape) == 2:
        print("\nImage is already Grayscale.\n")
        showImage("Grayscale", processed)
        return
    rgb = cv2.cvtColor(processed, cv2.COLOR_BGR2RGB)
    print("Showing BGR Image")
    showImage("BGR Image", processed)
    print("Showing RGB Image")
    showImage("RGB Image", rgb)

############### Side by Side Comparison
def side_by_side():
    if not checkImage():
        return
    if len(image.shape) == 2:
        original = cv2.cvtColor(image, cv2.COLOR_GRAY2BGR)
    else:
        original = image.copy()
    if len(processed.shape) == 2:
        edited = cv2.cvtColor(processed, cv2.COLOR_GRAY2BGR)
    else:
        edited = processed.copy()
    edited = cv2.resize(
        edited,
        (original.shape[1], original.shape[0])
    )
    combined = np.hstack((original, edited))
    showImage("Original vs Processed", combined)


##################### Save Image
def save():
    if not checkImage():
        return
    filename = input("Enter File Name: ")
    if not filename.endswith(".jpg"):
        filename += ".jpg"
    path = os.path.join(OUTPUT_FOLDER, filename)
    cv2.imwrite(path, processed)
    print(f"\nImage Saved Successfully!\nLocation: {path}\n")

################### Main Menu
while True:

    print("\n################## Image Processing Toolkit ###################")
    print("1. Load Image")
    print("2. Convert to Grayscale")
    print("3. Resize Image")
    print("4. Rotate Image")
    print("5. Flip Image")
    print("6. Crop Image")
    print("7. Draw Shapes")
    print("8. Add Custom Text")
    print("9. Adjust Brightness")
    print("10. Adjust Contrast")
    print("11. BGR vs RGB Comparison")
    print("12. Original vs Processed")
    print("13. Save Image")
    print("0. Exit")

    choice = input("\nEnter Your Choice: ")

    if choice == "1":
        loadImage()

    elif choice == "2":
        grayscale()

    elif choice == "3":
        resize()

    elif choice == "4":
        rotate()

    elif choice == "5":
        flip()

    elif choice == "6":
        crop()

    elif choice == "7":
        draw_shapes()

    elif choice == "8":
        add_text()

    elif choice == "9":
        brightness()

    elif choice == "10":
        contrast()

    elif choice == "11":
        rgb_compare()

    elif choice == "12":
        side_by_side()

    elif choice == "13":
        save()

    elif choice == "0":
        print("\nThank you for using Image Processing Toolkit!")
        break

    else:
        print("\nInvalid Choice! Please Try Again.")