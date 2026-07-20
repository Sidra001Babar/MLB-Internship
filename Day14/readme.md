# Image Processing Toolkit using OpenCV

## Project Overview

This project is a menu-driven Image Processing Toolkit developed using **Python** and **OpenCV**. It allows users to perform common image processing operations such as loading an image, converting it to grayscale, resizing, rotating, flipping, cropping, drawing shapes, adding text, adjusting brightness and contrast, comparing BGR and RGB images, and saving the processed image.

---

# Difference Between BGR and RGB

Both **BGR** and **RGB** are color models that represent images using three color channels.

## RGB (Red, Green, Blue)

- RGB is the standard color format used by most image processing libraries and display systems.
- The channels are arranged as:
  - Red
  - Green
  - Blue

Example:

```
RGB = (255, 0, 0)
```

This represents a **red** color.

---

## BGR (Blue, Green, Red)

- OpenCV reads color images in **BGR** format by default.
- The channel order is:
  - Blue
  - Green
  - Red

Example:

```
BGR = (255, 0, 0)
```

In OpenCV, this represents **blue**, not red.

---

## Why is this important?

If a BGR image is displayed in a library that expects RGB (such as Matplotlib), the colors will appear incorrect. Therefore, images often need to be converted from BGR to RGB before displaying them outside OpenCV.

Example:

```python
rgb_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
```

---

# What are Grayscale Images?

A grayscale image contains only **one channel** that represents the intensity (brightness) of each pixel instead of three color channels.

Pixel values range from:

- **0** → Black
- **255** → White
- Values between 0 and 255 represent different shades of gray.

Example:

```
0     = Black
128   = Gray
255   = White
```

---

# Why are Grayscale Images Used?

Grayscale images are commonly used because:

- They require less memory than color images.
- Processing is faster since only one channel is analyzed.
- They simplify many computer vision tasks.
- They are widely used for:
  - Face detection
  - OCR (Optical Character Recognition)
  - Edge detection
  - Medical image analysis
  - Object detection

Example:

```python
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
```

---

# OpenCV Functions Used

The following OpenCV functions were used in this project.

| Function | Purpose |
|----------|---------|
| `cv2.imread()` | Load an image from disk |
| `cv2.imshow()` | Display an image |
| `cv2.waitKey()` | Wait for a keyboard key |
| `cv2.destroyAllWindows()` | Close all OpenCV windows |
| `cv2.imwrite()` | Save an image |
| `cv2.cvtColor()` | Convert image color spaces (BGR ↔ RGB, BGR → Gray) |
| `cv2.resize()` | Resize an image |
| `cv2.rotate()` | Rotate an image |
| `cv2.flip()` | Flip an image horizontally or vertically |
| `cv2.rectangle()` | Draw a rectangle |
| `cv2.circle()` | Draw a circle |
| `cv2.line()` | Draw a line |
| `cv2.polylines()` | Draw polygons |
| `cv2.putText()` | Add text to an image |
| `cv2.convertScaleAbs()` | Adjust brightness and contrast |

---

# Challenges Faced and Solutions

## Challenge 1: Displaying Images in Google Colab

**Problem**

`cv2.imshow()` does not work in Google Colab.

**Solution**

Used:

```python
from google.colab.patches import cv2_imshow
```

For the VS Code version, replaced it with:

```python
cv2.imshow()
cv2.waitKey(0)
cv2.destroyAllWindows()
```

---

## Challenge 2: Menu-Driven Program in Google Colab

**Problem**

Google Colab does not reliably support continuous menu-driven programs using `input()` inside a loop.

**Solution**

Tested the complete application in **VS Code**, where interactive console input works correctly.

---

## Challenge 3: Preventing Program Crashes

**Problem**

If the user selected an operation before loading an image, the program produced an error.

**Solution**

Created a helper function to check whether an image had been loaded before performing any operation.

Example:

```python
def check_image():
    if processed is None:
        print("Please load an image first.")
        return False
    return True
```

---

## Challenge 4: Working with Grayscale Images

**Problem**

Drawing colored shapes and text on grayscale images caused incorrect behavior because grayscale images contain only one channel.

**Solution**

Converted grayscale images back to BGR before drawing.

Example:

```python
processed = cv2.cvtColor(processed, cv2.COLOR_GRAY2BGR)
```

---


# Conclusion

This project provided practical experience with OpenCV and image processing techniques. It helped in understanding image representation, color spaces, grayscale conversion, geometric transformations, drawing operations, and building a reusable menu-driven application using Python.