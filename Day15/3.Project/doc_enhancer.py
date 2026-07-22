import cv2
import numpy as np
import os
##################### 1. LOAD
def load_image(path):
    image = cv2.imread(path)
    if image is None:
        raise FileNotFoundError(f"Could not read image: {path}")
    return image

################### 2. PERSPECTIVE CORRECTION
def _order_points(pts):
    rect = np.zeros((4, 2), dtype="float32")
    s = pts.sum(axis=1)
    rect[0] = pts[np.argmin(s)]      # top-left has smallest sum
    rect[2] = pts[np.argmax(s)]      # bottom-right has largest sum
    diff = np.diff(pts, axis=1)
    rect[1] = pts[np.argmin(diff)]   # top-right has smallest difference
    rect[3] = pts[np.argmax(diff)]   # bottom-left has largest difference
    return rect


def _largest_quad_from_mask(mask, min_area_ratio=0.2):
    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    if not contours:
        return None

    c = max(contours, key=cv2.contourArea)
    total_area = mask.shape[0] * mask.shape[1]
    if cv2.contourArea(c) < min_area_ratio * total_area:
        return None

    peri = cv2.arcLength(c, True)
    for eps_mult in (0.02, 0.03, 0.05):
        approx = cv2.approxPolyDP(c, eps_mult * peri, True)
        if len(approx) == 4:
            return approx.reshape(4, 2)

    # Fall back to the rotated bounding rectangle of the contour -- this
    # still gives 4 usable corners even when the outline is a bit ragged.
    rect = cv2.minAreaRect(c)
    return cv2.boxPoints(rect)


def _find_document_contour(image):
    ratio = image.shape[0] / 500.0
    small = cv2.resize(image, (int(image.shape[1] / ratio), 500))

    # --- Strategy 1: edge-based ---
    gray = cv2.cvtColor(small, cv2.COLOR_BGR2GRAY)
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)
    edged = cv2.Canny(blurred, 50, 150)
    edged = cv2.dilate(edged, np.ones((3, 3), np.uint8), iterations=1)
    quad = _largest_quad_from_mask(edged)
    if quad is not None:
        return quad * ratio

    # --- Strategy 2: color/saturation-based ---
    hsv = cv2.cvtColor(small, cv2.COLOR_BGR2HSV)
    _, sat, _ = cv2.split(hsv)
    _, sat_mask = cv2.threshold(sat, 60, 255, cv2.THRESH_BINARY_INV)
    sat_mask = cv2.morphologyEx(sat_mask, cv2.MORPH_CLOSE, np.ones((15, 15), np.uint8))
    sat_mask = cv2.morphologyEx(sat_mask, cv2.MORPH_OPEN, np.ones((5, 5), np.uint8))
    quad = _largest_quad_from_mask(sat_mask)
    if quad is not None:
        return quad * ratio

    return None


def correct_perspective(image):
    contour = _find_document_contour(image)

    if contour is None:
        return image.copy(), False

    rect = _order_points(contour)
    (tl, tr, br, bl) = rect

    width_a = np.linalg.norm(br - bl)
    width_b = np.linalg.norm(tr - tl)
    max_width = max(int(width_a), int(width_b))

    height_a = np.linalg.norm(tr - br)
    height_b = np.linalg.norm(tl - bl)
    max_height = max(int(height_a), int(height_b))

    # Guard against degenerate/too-small detections
    if max_width < 20 or max_height < 20:
        return image.copy(), False

    dst = np.array([
        [0, 0],
        [max_width - 1, 0],
        [max_width - 1, max_height - 1],
        [0, max_height - 1]], dtype="float32")

    m = cv2.getPerspectiveTransform(rect, dst)
    warped = cv2.warpPerspective(image, m, (max_width, max_height))
    return warped, True

################## 3. GRAYSCALE
def convert_to_grayscale(image):
    if len(image.shape) == 2:
        return image
    return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

############ 4. NOISE REDUCTION
def reduce_noise(gray_image, strength=10):
    return cv2.fastNlMeansDenoising(gray_image, None, h=strength,
                                     templateWindowSize=7,
                                     searchWindowSize=21)

################# 5. BRIGHTNESS / CONTRAST ENHANCEMENT
def enhance_contrast(gray_image, clip_limit=2.5, tile_grid_size=(8, 8)):
    clahe = cv2.createCLAHE(clipLimit=clip_limit, tileGridSize=tile_grid_size)
    return clahe.apply(gray_image)


########################### 6. SHARPENING
def sharpen_image(image, amount=1.5, radius=2):
    blurred = cv2.GaussianBlur(image, (0, 0), radius)
    return cv2.addWeighted(image, 1 + amount, blurred, -amount, 0)


######################## 7. SAVE
def save_image(image, path):
    parent = os.path.dirname(path)
    if parent:
        os.makedirs(parent, exist_ok=True)
    cv2.imwrite(path, image)
    return path


####################### FULL PIPELINE
def process_image(input_path, output_path=None):
    original = load_image(input_path)
    corrected, contour_found = correct_perspective(original)
    gray = convert_to_grayscale(corrected)
    denoised = reduce_noise(gray)
    contrasted = enhance_contrast(denoised)
    final = sharpen_image(contrasted)

    if output_path:
        save_image(final, output_path)

    return {
        "original": original,
        "perspective_corrected": corrected,
        "contour_found": contour_found,
        "grayscale": gray,
        "denoised": denoised,
        "contrast_enhanced": contrasted,
        "sharpened": final,
        "final": final,
    }

########################### COMMAND-LINE ENTRY POINT
def _default_output_path(input_path):
    """Builds "<name>_enhanced.png" next to the input image if no output
    path is given on the command line."""
    root, _ = os.path.splitext(input_path)
    return f"{root}_enhanced.png"
