# Shape Detection System using OpenCV

## Overview

This project is a Python-based Shape Detection System developed using OpenCV. It detects multiple geometric shapes present in an image, draws contours around them, labels each detected shape, calculates its area and perimeter, and saves the processed output images.

---

# What are Contours?

Contours are the boundaries or outlines of objects in an image. They represent a curve joining all the continuous points having the same intensity or color.

In OpenCV, contours are mainly used for:

- Object detection
- Shape analysis
- Object recognition
- Measuring object properties such as area and perimeter

A contour is represented as a collection of points that define the boundary of an object.

---

# How Contour Detection Works

The contour detection process in this project follows these steps:

1. **Load Image**
   - Read the input image from the `inputImages` folder.

2. **Convert to Grayscale**
   - Convert the color image into a grayscale image to simplify processing.

3. **Apply Thresholding**
   - Convert the grayscale image into a binary image where the foreground objects are separated from the background.

4. **Find Contours**
   - Use OpenCV's `cv2.findContours()` function to detect the boundaries of all objects.

5. **Approximate the Shape**
   - Use `cv2.approxPolyDP()` to approximate each contour into a polygon.
   - The number of polygon vertices is used to identify the shape.

6. **Calculate Measurements**
   - Compute the contour area using `cv2.contourArea()`.
   - Compute the contour perimeter using `cv2.arcLength()`.

7. **Draw Results**
   - Draw contours and bounding rectangles.
   - Display the detected shape name, area, and perimeter.

---

# Shapes Detected

The program can detect the following geometric shapes:

- Triangle
- Square
- Rectangle
- Pentagon
- Hexagon
- Circle

Shapes are identified based on the number of vertices obtained after contour approximation and, for quadrilaterals, by checking the aspect ratio to distinguish between squares and rectangles.

---

# Challenges Faced

During implementation, several challenges were encountered:

- Choosing an appropriate threshold value for images with different colors and lighting conditions.
---



# Output

For every input image, the program generates:

- Original Image
- Contour Detection Result
- Final Shape Detection Result with:
  - Shape Labels
  - Bounding Rectangles
  - Area
  - Perimeter

All output images are automatically saved in the `outputImages` folder.