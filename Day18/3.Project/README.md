# Video Processing Tool

## Project Overview

This project demonstrates how to process recorded videos and live webcam feeds using OpenCV in Python. The application reads videos frame by frame, applies several image processing techniques, displays the processed results in real time, and saves the processed video as a new file.

---

# Features

- Read a recorded video.
- Display the original video.
- Convert each frame to grayscale.
- Apply Gaussian Blur.
- Apply Canny Edge Detection.
- Display the processed video in real time.
- Save the processed video.
- Capture and process live webcam video.

---

# How OpenCV Reads Videos

OpenCV reads videos using the `cv2.VideoCapture()` class.

```python
video = cv2.VideoCapture("video1.mp4")
```

A video is made up of many individual images called **frames**. OpenCV reads one frame at a time using:

```python
success, frame = video.read()
```

- `success` indicates whether a frame was read successfully.
- `frame` contains the current image from the video.

A `while` loop is used to continuously read frames until the video ends.

```python
while True:
    success, frame = video.read()

    if not success:
        break
```

---

# What FPS Means

**FPS (Frames Per Second)** is the number of frames displayed or processed every second.

Example:

- FPS = 30 means the video contains 30 frames every second.

OpenCV retrieves the FPS using:

```python
fps = video.get(cv2.CAP_PROP_FPS)
```

The FPS is also used while saving the processed video so that the output video plays at the same speed as the original.

---

# Processing Techniques Applied

## 1. Grayscale Conversion

The original color frame is converted into a grayscale image.

```python
gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
```

**Purpose**

- Reduces image complexity.
- Uses only one color channel instead of three.
- Makes further processing faster.

---

## 2. Gaussian Blur

Gaussian Blur smooths the image and removes small noise.

```python
blur = cv2.GaussianBlur(gray, (5,5), 0)
```

**Purpose**

- Reduces unwanted noise.
- Produces smoother images.
- Improves edge detection results.

---

## 3. Canny Edge Detection

Canny Edge Detection detects the boundaries of objects.

```python
edges = cv2.Canny(blur, 100, 200)
```

**Purpose**

- Detects object edges.
- Highlights important boundaries.
- Removes unnecessary image details.

---


# Results

The application successfully:

- Processed multiple recorded videos.
- Displayed the original and processed videos simultaneously.
- Applied grayscale conversion, Gaussian Blur, and Canny Edge Detection.
- Saved processed videos successfully.
- Processed live webcam video in real time.

---
Drive link of input videos and output processed videos: https://drive.google.com/drive/folders/1nFLyLF3GQvrMsoIVnesBrSvG0y5DAMbk?usp=sharing

# Conclusion

This project provided practical experience with OpenCV video processing. It demonstrated how videos are read frame by frame and how image processing techniques such as grayscale conversion, Gaussian Blur, and Canny Edge Detection can be applied to each frame. The project also highlighted the importance of FPS and efficient frame processing when working with videos.