## Document Boundary Detection using OpenCV

This project detects document boundaries from images using OpenCV. The processing pipeline includes grayscale conversion, Gaussian blurring, Canny edge detection, morphological operations, contour detection, and boundary visualization.

---

## Difference Between Sobel, Laplacian, and Canny

### Sobel Operator
The Sobel operator calculates the first-order derivative (gradient) of the image intensity to detect edges in the horizontal and vertical directions. It provides information about edge direction but is sensitive to noise and often produces thicker edges.

### Laplacian Operator
The Laplacian operator calculates the second-order derivative of the image intensity. It detects edges in all directions but is more sensitive to noise than Sobel because it amplifies small intensity changes. Gaussian Blur is usually applied before using the Laplacian operator.

### Canny Edge Detection
Canny is a multi-stage edge detection algorithm that includes noise reduction, gradient calculation, non-maximum suppression, double thresholding, and edge tracking by hysteresis. It produces thin, continuous, and accurate edges while effectively reducing noise.

| Technique | Advantages | Disadvantages |
|-----------|------------|---------------|
| Sobel | Fast, detects edge direction | Sensitive to noise, thick edges |
| Laplacian | Detects edges in all directions | Highly sensitive to noise |
| Canny | Accurate, thin, and clean edges | Requires threshold tuning and is computationally slower |

---

## Purpose of Each Morphological Operation

### Erosion
Shrinks the foreground objects by removing pixels from their boundaries. It is useful for removing small white noise and separating connected objects.

### Dilation
Expands the foreground objects by adding pixels to their boundaries. It helps fill small holes and reconnect broken edges.

### Opening
Opening is erosion followed by dilation. It removes small foreground noise while preserving the main object.

### Closing
Closing is dilation followed by erosion. It fills small holes, closes gaps in object boundaries, and connects broken edges. This operation was used in the project after Canny edge detection.

### Morphological Gradient
Computes the difference between the dilated and eroded images to highlight object boundaries.

### Top Hat
Extracts small bright regions by subtracting the opened image from the original image. It is useful for highlighting bright details.

### Black Hat
Extracts small dark regions by subtracting the original image from the closed image. It is useful for detecting cracks, dark spots, and defects.

---

## Which Combination of Techniques Gave the Best Results?

The best results were obtained using the following processing pipeline:

1. Convert the image to grayscale.
2. Apply Gaussian Blur to reduce noise.
3. Detect edges using Canny Edge Detection.
4. Apply Morphological Closing to connect broken edges and fill small gaps.
5. Detect the largest contour as the document boundary.
6. Draw the detected boundary on the original image.

This combination produced clean and continuous document edges, making it easier to detect the largest contour corresponding to the document.

---

## Challenges Faced While Detecting Document Boundaries


- Documents with low contrast against the background were more difficult to detect accurately.
- Slightly folded or curved documents produced irregular contours.
- Selecting appropriate Canny threshold values required experimentation, as different images responded differently.
- In some cases, increasing the kernel size for morphological operations connected unwanted objects, while a smaller kernel failed to close gaps in document edges.

---

## Conclusion

The combination of Gaussian Blur, Canny Edge Detection, Morphological Closing, and contour detection proved to be an effective approach for detecting document boundaries in most images. While performance depends on image quality and background complexity, this pipeline provides reliable results for scanned documents and well-captured photographs.