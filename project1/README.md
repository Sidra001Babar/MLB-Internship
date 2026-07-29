# Smart Parking Lot Occupancy Analyzer

## Project Overview

The **Smart Parking Lot Occupancy Analyzer** is a Computer Vision-based system that automatically analyzes parking lot images and determines which parking spaces are occupied and which are vacant.

The project combines traditional **OpenCV image processing techniques** with a custom-trained **YOLOv8 object detection model** to detect parking spaces, classify them as empty or occupied, visualize the results, and display overall parking occupancy statistics.

The main objective of this project is to build an automated parking monitoring system that can help analyze parking availability without manual inspection.

---

# Dataset Used


## Original Dataset

The original PKLot dataset was obtained from Roboflow: https://public.roboflow.com/object-detection/pklot/2


## YOLO Format Dataset

The downloaded dataset into YOLO format

Dataset Drive Link:
https://drive.google.com/drive/folders/12kDwmbdeJAQDoXpK9r09KRvR0l0Ilv_W

---

## Preprocessed Dataset

Before training, OpenCV preprocessing was applied to the complete dataset.
The preprocessed dataset used for YOLO training is available here:

https://drive.google.com/drive/folders/1IcgmnIml2cAlAMsT5vgNI3cIcKgqsM8E?usp=sharing

---

# Project Workflow

The complete workflow of the Smart Parking Lot Occupancy Analyzer consists of dataset preprocessing, YOLO model training, prediction, visualization, and statistics generation.

```
                 Original PKLot Dataset
                         |
                         ↓
             OpenCV Preprocessing Pipeline
                         |
          --------------------------------
          |                              |
          ↓                              ↓
    Noise Reduction              Contrast Enhancement
    Gaussian Blur                CLAHE
          |
          ↓
        Preprocessed Dataset
                         |
                         ↓
              YOLOv8 Model Training
                         |
                         ↓
              Trained Parking Detector
                         |
                         ↓
                Test Image Input
                         |
                         ↓
              YOLO Parking Detection
                         |
                         ↓
        space-empty / space-occupied Prediction
                         |
                         ↓
             OpenCV Visualization
                         |
                         ↓
              Statistics Calculation
                         |
                         ↓
                  Save Final Result
```
## OpenCV Techniques Selection

OpenCV techniques were selected based on their relevance to the YOLO-based parking detection approach.

| Technique | Status | Usage / Reason |
|------------|--------|----------------|
| Gaussian Blur |  Used | Applied during preprocessing for noise reduction and image smoothing before YOLO training. |
| CLAHE |  Used | Improved local contrast and visibility of parking spaces under different lighting conditions. |
| Image Resizing |  Not Used | PKLot YOLO dataset was already available in 640×640 format, so additional resizing was unnecessary. |
| Edge Detection (Canny/Sobel/Laplacian) |  Not Used | YOLO automatically learns important features such as parking slot boundaries. These techniques are more suitable for traditional edge-based detection approaches. |
| Morphological Operations |  Not Used | Not required because YOLO directly detects parking spaces. Useful for cleaning binary images and segmentation masks. |
| Contour Detection |  Not Used | Dataset already provided parking slot annotations. Contours can be used in traditional approaches for automatic parking slot extraction. |
| OpenCV Visualization |  Used | Used after YOLO detection to draw bounding boxes, labels, colors, and occupancy statistics. |

**Note:** Traditional computer vision techniques such as edge detection, morphological operations, and contour detection were evaluated. However, because the PKLot dataset already provides annotated parking spaces and the project uses a YOLO-based detector, these techniques were not included in the final detection pipeline. They could be used in future work for automatic parking slot extraction when annotations are unavailable.

**Final Approach:**  
OpenCV was used for image enhancement and result visualization, while YOLOv8 was used for parking space detection and classification.
## Workflow Explanation

### 1. Dataset Preprocessing Using OpenCV

Before training the YOLO model, OpenCV preprocessing techniques were applied to the complete PKLot dataset.

The purpose of preprocessing was to improve image quality and make parking spaces easier for the model to learn.

The preprocessing pipeline included:

### Noise Reduction - Gaussian Blur

Gaussian Blur was applied to reduce small image noise and unwanted variations.

Benefits:

- Reduces noise
- Smooths image details
- Improves image consistency


### Contrast Enhancement - CLAHE

Contrast Limited Adaptive Histogram Equalization (CLAHE) was applied to improve local contrast.

The image was converted from BGR to LAB color space, and CLAHE was applied only on the L (brightness) channel.
Benefits:

- Improves visibility of parking spaces
- Enhances details in different lighting conditions
- Maintains image color information


After preprocessing, all images were saved into a new preprocessed dataset while keeping the original YOLO labels unchanged.

---

### 2. YOLOv8 Model Training

The preprocessed dataset was used to train a custom YOLOv8 object detection model.

The model was trained to detect two classes:

```
0 - space-empty
1 - space-occupied
```

The trained model learned the location and occupancy status of parking spaces from the annotated images.

---

### 3. Parking Space Detection

The trained YOLOv8 model receives a parking lot image and predicts:

- Bounding box coordinates
- Class label
- Confidence score

The model identifies each parking space as:

- Empty parking space
- Occupied parking space


---

### 4. OpenCV Visualization

OpenCV was used after detection to create a user-friendly output.

The visualization stage:

- Draws bounding boxes around parking spaces
- Uses different colors for each class

Color representation:

- Blue → Space Empty
- Red → Space Occupied

---

### 5. Occupancy Statistics

After detecting all parking spaces, the system calculates parking statistics:

- Total parking spaces
- Number of empty spaces
- Number of occupied spaces
- Parking occupancy percentage

Example:

```
Total Spaces: 101
Empty Spaces: 29
Occupied Spaces: 72
Occupancy Percentage: 71.29%
```

---

### 6. Save Final Result

The final output image contains:

- Detected parking spaces
- Occupancy labels
- Confidence scores
- Parking statistics overlay

The processed images are saved for further analysis.
# Technologies Used
- Python(Programming language)
- OpenCV(CV library)
- YOLOv8(deep learning model)
- Ultralytics
- Google Colab GPU 
- PKLot.v2-640.yolov8
- VS Code
- Google Colab


---

# Results

The custom YOLOv8 model achieved strong performance on the validation dataset.

Training results:

| Metric | Value |
|---|---|
| Precision | 0.99848 |
| Recall | 0.99852 |
| mAP50 | 0.99452 |
| mAP50-95 | 0.97452 |

The model successfully detects parking spaces and classifies them into:

- Space Empty
- Space Occupied

The final system produces:

- Annotated parking images
- Color-coded parking spaces
- Occupancy statistics
## Trained YOLO Model

The trained YOLOv8 model with results.csv and batch jpgs and weights is available here:

https://drive.google.com/drive/folders/13KFMqmC1igJVRpuvKvMsYemS7xilrEBW

Example output:

```
Total Spaces: 101
Empty Spaces: 29
Occupied Spaces: 72
Occupancy Percentage: 71.29%
```

---

# Challenges Faced

## 1. Selecting the Correct Computer Vision Workflow

The first challenge was deciding which Computer Vision techniques should be included in the project workflow.

Since the project required combining OpenCV and YOLO, it was important to determine:

- Which preprocessing techniques improve image quality
- Which operations are unnecessary
- Where traditional computer vision techniques should be used
- Where deep learning should be applied

After testing different approaches, the final workflow combined OpenCV preprocessing with YOLO-based parking space detection.

---

## 2. Computational Resources and Processing Time

Initially, the YOLO model training and preprocessing tasks were attempted on a local laptop.

However, training the model locally required a very large amount of time and computational resources.

The solution was to move the training workflow to Google Colab.

The dataset was uploaded to Google Drive, allowing:

- Easier dataset management
- Saving processed data directly to Drive
- Faster training using GPU resources

During preprocessing, another challenge occurred:

The preprocessing pipeline was taking several hours in Google Colab.

The process was optimized by using multiprocessing, which significantly reduced preprocessing time.

For YOLO training, Google Colab GPU acceleration was used to make training faster.

---

## 3. Training Session Timeout

The YOLO model was initially configured for:

```
Epochs = 50
```

However, during training, the Google Colab runtime session timed out at epoch 45.

The training process stopped before completing all 50 epochs.

After analyzing the generated `results.csv` file, the model performance was already good, so the trained model from epoch 45 was used.

The achieved results showed:

- high precision
- high recall
- mAP scores

Therefore, additional training was not necessary.

---

# Future Improvements

Possible future improvements include:

## 1. Real-Time Parking Monitoring

Integrate the system with:

- CCTV cameras
- Live video streams
- Real-time parking monitoring systems

---

## 2. Database Integration

Store parking information including:

- Time
- Date
- Occupancy percentage
- Available spaces

for historical analysis.

---

## 3. Web Application Development

Create a dashboard that displays:

- Live parking status
- Parking availability
- Occupancy trends

---

## 4. Improved Visualization

Enhance visualization by adding:

- Better parking slot highlighting
- Interactive parking maps
- More detailed analytics

---

## 5. Automatic Parking Slot Mapping

Implement automatic parking slot extraction using:

- Contour detection
- Perspective transformation
- Geometric analysis

to reduce dependency on annotated datasets.

---

# Conclusion

The Smart Parking Lot Occupancy Analyzer demonstrates a complete Computer Vision pipeline by combining OpenCV image processing techniques with YOLOv8 object detection.

The system successfully detects parking spaces, classifies occupancy status, visualizes results, and generates parking statistics, providing a foundation for an automated smart parking management solution.