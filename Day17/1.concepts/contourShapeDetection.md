# Find and Draw Contours using OpenCV (Python)

## What are Contours?

Contours are the **boundaries (outline)** of objects in an image.

- A contour is represented as a collection of **(x, y) coordinate points**.
- Contours are usually detected on **binary or edge images**.
- They are commonly used for:
  - Object Detection
  - Shape Detection
  - Object Counting
  - Measuring Area and Perimeter
  - Image Segmentation
  - Document Boundary Detection

---



# Find Contours

```python
contours, hierarchy = cv2.findContours(
    edged,
    cv2.RETR_EXTERNAL,
    cv2.CHAIN_APPROX_NONE
)
```

## Function

### `cv2.findContours()`

Finds object boundaries from a binary image.

### Syntax

```python
cv2.findContours(image, mode, method)
```

### Parameters

| Parameter | Meaning |
|-----------|----------|
| `image` | Binary or edge image |
| `mode` | Contour retrieval mode |
| `method` | Contour approximation method |

---

## Contour Retrieval Modes

### 1. `cv2.RETR_EXTERNAL`

Returns only outer contours.


Use when:

- Object counting
- Document detection

---

### 2. `cv2.RETR_LIST`

Returns all contours.

No parent-child relationship stored.

Useful for:

- Shape detection
- General contour analysis

---

### 3. `cv2.RETR_TREE`

Returns every contour and stores the complete hierarchy.

Example

```
Rectangle
 ├── Circle
 │     └── Hole
```

Keeps all relationships.

Useful for:

- Nested objects
- Image hierarchy analysis

---

### 4. `cv2.RETR_CCOMP`

Creates two hierarchy levels.

Level 1

Outer contours

Level 2

Holes inside objects

Useful for:

- Region analysis
- Hole detection

---

### 5. `cv2.RETR_FLOODFILL`

Special retrieval mode used with flood-fill operations.

Rarely used.

---

## Contour Approximation Methods

### 1. `cv2.CHAIN_APPROX_NONE`

Stores every contour point.
Memory usage:

High

Accuracy:

Highest

---

### 2. `cv2.CHAIN_APPROX_SIMPLE`

Stores only essential points.


Only stores the four corners.

Memory usage:

Low

Recommended in most projects.

---

### 3. `cv2.CHAIN_APPROX_TC89_L1`

Uses the Teh-Chin approximation algorithm.

Produces smoother contours.

---

### 4. `cv2.CHAIN_APPROX_TC89_KCOS`

Another Teh-Chin approximation method.

Provides even smoother contour representation.

---

## Returns

### contours

A list containing all detected contours.

Each contour is a NumPy array of coordinate points.

Example

```python
[
 [[10,20]],
 [[11,21]],
 [[12,22]]
]
```

---

### hierarchy

Stores relationships among contours.

Example

```python
[[Next, Previous, FirstChild, Parent]]
```

---

# Draw Contours

```python
cv2.drawContours(
    image,
    contours,
    -1,
    (0,255,0),
    2
)
```

## Function

### `cv2.drawContours()`

Draws contours on an image.

### Syntax

```python
cv2.drawContours(
    image,
    contours,
    contourIdx,
    color,
    thickness,
    lineType=cv2.LINE_8
)
```

### Parameters

| Parameter | Meaning |
|-----------|----------|
| `image` | Image to draw on |
| `contours` | List of contours |
| `contourIdx` | Which contour to draw |
| `color` | BGR color |
| `thickness` | Line thickness |
| `lineType` | Type of line |

---

## contourIdx Values

| Value | Meaning |
|--------|----------|
| `-1` | Draw all contours |
| `0` | Draw first contour |
| `1` | Draw second contour |
| `2` | Draw third contour |

---

## Color (BGR)

| Color | Value |
|--------|--------|
| Blue | `(255,0,0)` |
| Green | `(0,255,0)` |
| Red | `(0,0,255)` |
| White | `(255,255,255)` |
| Black | `(0,0,0)` |
| Yellow | `(0,255,255)` |
| Cyan | `(255,255,0)` |
| Magenta | `(255,0,255)` |

---

## Thickness

| Value | Meaning |
|--------|----------|
| `1` | Thin line |
| `2` | Medium line |
| `3-5` | Thick line |
| `-1` | Fill the contour *(only for closed contours)* |

---

## lineType Values

| Value | Meaning |
|--------|----------|
| `cv2.LINE_4` | 4-connected line |
| `cv2.LINE_8` | 8-connected line (Default) |
| `cv2.LINE_AA` | Anti-aliased smooth line |

---
# Contour Area

The area of a contour is the number of pixels enclosed by its boundary.

---

## Built-in Function

```python
area = cv2.contourArea(contour)
```

### Syntax

```python
cv2.contourArea(contour, oriented=False)
```

### Parameters

| Parameter | Meaning |
|-----------|---------|
| `contour` | Input contour (list of contour points) |
| `oriented` | If `False` (default), returns positive area. If `True`, area can be positive or negative depending on contour direction (clockwise/counterclockwise). |

### Returns

```python
float
```

Area of the contour.

---

## Example

```python
area = cv2.contourArea(contour)
print(area)
```

---

# Contour Perimeter

Also called **Arc Length**.

It is the total distance around the contour.

---

## Built-in Function

```python
perimeter = cv2.arcLength(contour, True)
```

### Syntax

```python
cv2.arcLength(curve, closed)
```

### Parameters

| Parameter | Meaning |
|-----------|---------|
| `curve` | Input contour |
| `closed` | `True` if contour is closed, `False` otherwise |

### Returns

```python
float
```

Perimeter (arc length).

---

## Example

```python
perimeter = cv2.arcLength(contour, True)
print(perimeter)
```

---


# Comparison

| Feature | Manual Calculation | OpenCV Built-in |
|----------|--------------------|-----------------|
| Area | Shoelace Formula | `cv2.contourArea()` |
| Perimeter | Sum of Euclidean distances | `cv2.arcLength()` |
| Speed | Slower | Very Fast (C++ optimized) |
| Accuracy | Depends on implementation | Highly accurate |
| Recommended | For understanding algorithms | For real-world projects |

# Shape Detection in Images using OpenCV (Python)

## What is Shape Detection?

Shape detection is the process of identifying the geometric shape of objects present in an image.

Examples:

- Triangle
- Square
- Rectangle
- Pentagon
- Hexagon
- Circle

OpenCV detects these shapes by:

1. Detecting contours (object boundaries)
2. Approximating the contour into a polygon
3. Counting the number of polygon vertices
4. Assigning a shape name based on the number of vertices

---

# Workflow

```
Input Image
      │
      ▼
Read Image
      │
      ▼
Convert to Grayscale
      │
      ▼
Threshold Image
      │
      ▼
Find Contours
      │
      ▼
Approximate Polygon
      │
      ▼
Count Vertices
      │
      ▼
Identify Shape
      │
      ▼
Draw Contour & Label
```

---

# Calculate Image Moments

```python
M = cv2.moments(contour)
```

## What are Moments?

Moments are mathematical values calculated from a contour that describe its geometric properties, such as:

- Area
- Center (Centroid)
- Orientation

---

## Function

### `cv2.moments()`

### Syntax

```python
cv2.moments(contour)
```

### Returns

A dictionary containing values like:

| Key | Meaning |
|-----|----------|
| `m00` | Area of contour |
| `m10` | X weighted moment |
| `m01` | Y weighted moment |
| `mu20` | Central moment |
| `mu11` | Central moment |
| `nu20` | Normalized moment |

---

# Find Center

```python
x = int(M["m10"] / M["m00"])
y = int(M["m01"] / M["m00"])
```

## Formula

Centroid

```
Cx = m10 / m00

Cy = m01 / m00
```

where:

- `m00` = Area
- `m10` = X moment
- `m01` = Y moment

---

# Count Vertices

```python
sides = len(approx)
```

## Built-in Function

### `len()`

Returns number of polygon vertices.

Example

```
Triangle → 3

Rectangle → 4

Pentagon → 5

Hexagon → 6

Circle → Many
```

---

# Detect Shape

```python
if sides == 3:
    label = "Triangle"

elif sides == 4:
    label = "Quadrilateral"

elif sides == 5:
    label = "Pentagon"

elif sides == 6:
    label = "Hexagon"

else:
    label = "Circle"
```

# Draw Text

```python
cv2.putText(
    img,
    label,
    (x,y),
    cv2.FONT_HERSHEY_SIMPLEX,
    0.6,
    (255,255,255),
    2
)
```

## Function

### `cv2.putText()`

Draws text on an image.

### Syntax

```python
cv2.putText(
    image,
    text,
    org,
    font,
    fontScale,
    color,
    thickness,
    lineType=cv2.LINE_8
)
```

### Parameters

| Parameter | Meaning |
|-----------|----------|
| `image` | Input image |
| `text` | Text to draw |
| `org` | Bottom-left corner of the text `(x, y)` |
| `font` | Font type |
| `fontScale` | Font size |
| `color` | Text color (BGR) |
| `thickness` | Text thickness |
| `lineType` | Line drawing style |

