# Document Enhancement Pipeline - Structure
## Custom Functions

| Function | Purpose |
|----------|---------|
| `load_image(path)` | Loads an image from disk. |
| `_order_points(pts)` | Orders four corner points as top-left, top-right, bottom-right, and bottom-left. |
| `_largest_quad_from_mask(mask)` | Finds the largest document-like quadrilateral from a binary mask. |
| `_find_document_contour(image)` | Detects the document contour using edge-based and color-based methods. |
| `correct_perspective(image)` | Straightens the document using perspective transformation. |
| `convert_to_grayscale(image)` | Converts a color image into grayscale. |
| `reduce_noise(gray_image)` | Removes image noise while preserving text edges. |
| `enhance_contrast(gray_image)` | Improves local contrast using CLAHE. |
| `sharpen_image(image)` | Sharpens text and document edges using Unsharp Masking. |
| `save_image(image, path)` | Saves the processed image to disk. |
| `process_image(input_path, output_path)` | Executes the complete document enhancement pipeline. |
| `_default_output_path(input_path)` | Generates the default output filename. |

---

# OpenCV Built-in Functions

| Function | Purpose |
|----------|---------|
| `cv2.imread()` | Reads an image from disk. |
| `cv2.imwrite()` | Saves an image to disk. |
| `cv2.resize()` | Resizes an image. |
| `cv2.cvtColor()` | Converts an image between color spaces. |
| `cv2.GaussianBlur()` | Reduces noise by smoothing the image. |
| `cv2.Canny()` | Detects image edges. |
| `cv2.dilate()` | Expands edges or white regions. |
| `cv2.findContours()` | Finds contours in a binary image. |
| `cv2.contourArea()` | Calculates the area of a contour. |
| `cv2.arcLength()` | Calculates the perimeter of a contour. |
| `cv2.approxPolyDP()` | Approximates a contour into a polygon. |
| `cv2.minAreaRect()` | Finds the minimum-area rotated rectangle around a contour. |
| `cv2.boxPoints()` | Returns the four corner points of a rotated rectangle. |
| `cv2.threshold()` | Converts a grayscale image into a binary image. |
| `cv2.morphologyEx()` | Performs morphological operations (Opening, Closing, etc.). |
| `cv2.split()` | Splits an image into separate channels. |
| `cv2.getPerspectiveTransform()` | Computes the perspective transformation matrix. |
| `cv2.warpPerspective()` | Applies perspective transformation to an image. |
| `cv2.fastNlMeansDenoising()` | Removes noise while preserving image details. |
| `cv2.createCLAHE()` | Creates a CLAHE object for contrast enhancement. |
| `clahe.apply()` | Applies CLAHE to the image. |
| `cv2.addWeighted()` | Combines two images using weighted addition (used for sharpening). |

---

# NumPy Functions

| Function | Purpose |
|----------|---------|
| `np.zeros()` | Creates an array filled with zeros. |
| `np.ones()` | Creates an array filled with ones. |
| `np.array()` | Creates a NumPy array. |
| `np.argmin()` | Returns the index of the minimum value. |
| `np.argmax()` | Returns the index of the maximum value. |
| `np.diff()` | Computes the difference between adjacent values. |
| `np.linalg.norm()` | Computes the Euclidean distance between two points. |
| `reshape()` | Changes the shape of an array without changing its data. |

---

# OS Module Functions

| Function | Purpose |
|----------|---------|
| `os.path.dirname()` | Returns the parent directory of a path. |
| `os.makedirs()` | Creates directories if they do not exist. |
| `os.path.splitext()` | Splits a filename into its name and extension. |

---

# Overall Processing Pipeline

```
Load Image
      │
      ▼
Find Document Contour
      │
      ▼
Correct Perspective
      │
      ▼
Convert to Grayscale
      │
      ▼
Reduce Noise
      │
      ▼
Enhance Contrast (CLAHE)
      │
      ▼
Sharpen Image
      │
      ▼
Save Enhanced Image
```