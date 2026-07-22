# Document Image Enhancement Tool

## Transformations Implemented

### 1. Perspective Correction
**What it does:**
- Detects the document boundaries using contour detection.
- Applies a perspective transformation to obtain a top-down view of the document.

**Purpose:**
- Corrects tilted or skewed document images.
- Makes the document appear as if it were scanned directly from above.
- Improves readability and prepares the image for further processing such as OCR.

---

### 2. Grayscale Conversion
**What it does:**
- Converts the color document image into a single-channel grayscale image.

**Purpose:**
- Removes unnecessary color information.
- Simplifies image processing.
- Reduces computational complexity while preserving text information.

---

### 3. Noise Reduction
**What it does:**
- Uses OpenCV's Non-Local Means Denoising algorithm (`fastNlMeansDenoising`) to remove image noise.

**Purpose:**
- Eliminates camera and compression noise.
- Preserves document edges while removing unwanted artifacts.
- Produces a cleaner image for later enhancement steps.

---

### 4. Contrast Enhancement
**What it does:**
- Applies CLAHE (Contrast Limited Adaptive Histogram Equalization).

**Purpose:**
- Improves local contrast.
- Enhances faded text.
- Corrects uneven lighting without overexposing bright regions.
- Makes the document easier to read.

---

### 5. Image Sharpening
**What it does:**
- Applies an Unsharp Mask using Gaussian Blur and weighted image addition.

**Purpose:**
- Enhances text edges.
- Improves the clarity of characters.
- Makes the final document appear sharper and more readable.

---

## Purpose of Each Enhancement Technique

| Technique | Purpose |
|-----------|---------|
| Perspective Correction | Removes tilt and produces a flat document. |
| Grayscale Conversion | Simplifies the image by removing color information. |
| Noise Reduction | Removes camera noise while preserving text edges. |
| Contrast Enhancement (CLAHE) | Improves readability by increasing local contrast. |
| Image Sharpening | Makes text edges clearer and improves overall document quality. |

---

## Transformation with the Biggest Impact

The **Perspective Correction** had the biggest impact on document quality.

This transformation converts a tilted document into a properly aligned, top-down view. Without perspective correction, the remaining enhancement techniques (grayscale conversion, denoising, contrast enhancement, and sharpening) cannot fully improve the document because the text remains distorted.

For documents where the page boundary is successfully detected, perspective correction significantly improves readability and creates a scan-like appearance.

---

## Challenges Faced During Implementation

- Detecting document boundaries in real-world images was the most challenging part of the project.
- The contour detection approach worked well on images with clear backgrounds but struggled when:
  - The document occupied only a small portion of the image.
  - Shadows were present.
  - The background color was similar to the paper.
  - The page edges were partially blurred or curled.
- Selecting suitable Canny edge detection thresholds and contour filtering parameters required experimentation to balance accurate detection with robustness.
- Different document images required different preprocessing conditions, making it difficult to design a single pipeline that worked perfectly for every image.

---

## Overall Observation

The complete enhancement pipeline successfully improves document readability by combining multiple image processing techniques. Perspective correction aligns the document, grayscale conversion simplifies the image, noise reduction removes unwanted artifacts, CLAHE enhances local contrast, and sharpening improves text clarity. While the pipeline performs well on many document images, its accuracy depends largely on successful document boundary detection under varying lighting and background conditions.