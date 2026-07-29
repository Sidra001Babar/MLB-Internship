# OpenCV Video Processing Concepts

## 1. VideoCapture

**Concept:**
`VideoCapture` is an OpenCV class used to open and read videos or access a webcam.

**Syntax**
```python
video = cv2.VideoCapture("input.mp4")
```

or for a webcam:

```python
camera = cv2.VideoCapture(0)
```

- `"input.mp4"` opens a video file.
- `0` opens the default webcam.

---

## 2. Checking if the Video Opened Successfully

**Concept:**
Before processing, always check whether the video or webcam was opened successfully.

**Syntax**
```python
if not video.isOpened():
    print("Cannot open video")
```

This prevents the program from crashing if the file path is incorrect or the webcam is unavailable.

---

## 3. Reading Video Properties

OpenCV stores information about a video, such as its frame rate and dimensions.

### FPS (Frames Per Second)

FPS represents the number of frames displayed every second.

```python
fps = video.get(cv2.CAP_PROP_FPS)
```

Example:
- FPS = 30
- The video displays 30 images every second.

---

### Width

Width is the number of pixels in each frame horizontally.

```python
width = int(video.get(cv2.CAP_PROP_FRAME_WIDTH))
```

Example:
- Width = 1280 pixels

---

### Height

Height is the number of pixels in each frame vertically.

```python
height = int(video.get(cv2.CAP_PROP_FRAME_HEIGHT))
```

Example:
- Height = 720 pixels

---

### Total Number of Frames

Returns how many frames are present in the video.

```python
total_frames = int(video.get(cv2.CAP_PROP_FRAME_COUNT))
```

Example:
- Total Frames = 300

---

## 4. Reading Frames

**Concept:**
A video is simply a sequence of images called **frames**. OpenCV reads one frame at a time.

```python
success, frame = video.read()
```

### Returns

- **success** → `True` if a frame was read successfully.
- **frame** → The current image from the video.

When the video ends:

```python
success = False
```

---

## 5. While Loop

**Concept:**
A `while` loop continuously reads frames until the video ends.

```python
while True:
```

The loop stops when:

```python
if not success:
    break
```

---

## 6. Grayscale Conversion

**Concept:**
A color image contains three channels:

- Blue (B)
- Green (G)
- Red (R)

Grayscale converts the image into a single intensity channel.

```python
gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
```

### Advantages

- Faster processing
- Less memory usage
- Easier edge detection

---

## 7. Canny Edge Detection

**Concept:**
Canny Edge Detection detects the boundaries of objects in an image.

```python
edges = cv2.Canny(gray, 100, 200)
```

### Parameters

- `100` → Lower threshold
- `200` → Upper threshold

### Result

The output image contains:

- White pixels → Edges
- Black pixels → Background

---

## 8. Displaying Frames

**Concept:**
`imshow()` displays each processed frame in a window.

```python
cv2.imshow("Edges", edges)
```

Since frames are shown rapidly, they appear as a video.

---

## 9. waitKey()

**Concept:**
`waitKey()` pauses the program for a specified number of milliseconds and checks for keyboard input.

```python
cv2.waitKey(30)
```

Example:

```python
if cv2.waitKey(30) & 0xFF == ord('q'):
    break
```

Pressing **q** stops the program.

---

## 10. Saving the Processed Video

**Concept:**
`VideoWriter` creates a new video file and saves processed frames.

```python
output = cv2.VideoWriter(
    "output.avi",
    fourcc,
    fps,
    (width, height),
    False
)
```

### Parameters

- Output file name
- Video codec
- FPS
- Frame size
- `False` indicates grayscale frames

Each processed frame is saved using:

```python
output.write(edges)
```

---

## 11. Releasing Resources

**Concept:**
After processing, release the video and close all OpenCV windows.

```python
video.release()
output.release()
cv2.destroyAllWindows()
```

### Purpose

- Frees memory
- Closes video files
- Closes display windows
- Releases the webcam if used

---

# Webcam Capture

## Opening the Webcam

```python
camera = cv2.VideoCapture(0)
```

`0` represents the default webcam.

---

## Capturing Live Frames

```python
success, frame = camera.read()
```

The webcam continuously captures new frames in real time.

---

## Displaying Live Video

```python
cv2.imshow("Live Webcam", frame)
```

The captured frames are displayed continuously, creating a live video feed.

---

## Closing the Webcam

```python
camera.release()
cv2.destroyAllWindows()
```

Always release the webcam after use so other applications can access it.

---

# Workflow

```
Open Video/Webcam
        │
        ▼
Check if Opened Successfully
        │
        ▼
Read Video Properties
(FPS, Width, Height, Total Frames)
        │
        ▼
Read One Frame
        │
        ▼
Convert to Grayscale
        │
        ▼
Apply Canny Edge Detection
        │
        ▼
Display Processed Frame
        │
        ▼
Save Processed Frame
        │
        ▼
Repeat Until Video Ends
        │
        ▼
Release Resources
```