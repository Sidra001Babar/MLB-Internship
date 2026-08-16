# Traffic Object Detection Using YOLOv8

## Project Overview

This project implements a custom **traffic object detection system using YOLOv8**. The model was trained on a custom dataset of traffic frames and then tested on a **new unseen traffic video**.

The YOLOv8n model was trained **from scratch** without using pretrained weights or fine-tuning.

The final model detects seven traffic-related classes:

- Bus
- Truck
- Car
- Bicycle
- Bike
- Auto
- Pedestrian

---

## Technologies Used

- Python
- Google Colab
- PyTorch
- Ultralytics YOLOv8
- OpenCV
- Google Drive
- YOLO Annotation Format

---

## Dataset

The dataset contains approximately **1,151 traffic frames** extracted from traffic videos.

The frames were annotated using a custom annotation tool and exported in YOLO format.

### Dataset Split

The dataset was divided approximately as follows:

| Split | Images |
|---|---:|
| Training | 805 |
| Validation | 230 |
| Testing | 116 |
| **Total** | **1,151** |

---

## Classes and Object Distribution

After cleaning the annotations, the final dataset contained the following classes:

| ID | Class | Objects |
|---:|---|---:|
| 0 | Bus | 1,143 |
| 1 | Truck | 48 |
| 2 | Car | 415 |
| 3 | Bicycle | 100 |
| 4 | Bike | 951 |
| 5 | Auto | 4,100 |
| 6 | Pedestrian | 554 |

### Class Distribution

The dataset is **imbalanced**, with `Auto` being the dominant class.

```text
Auto        → 4,100 objects
Bus         → 1,143 objects
Bike        →   951 objects
Pedestrian  →   554 objects
Car         →   415 objects
Bicycle     →   100 objects
Truck       →    48 objects
```

---

## Project Workflow

```text
Traffic Videos
      ↓
Frame Extraction
      ↓
Traffic Dataset
      ↓
YOLO Annotation
      ↓
Annotation Cleaning
      ↓
Remove Unwanted Classes
      ↓
Class ID Remapping
      ↓
Train / Validation / Test Split
      ↓
Create YOLO data.yaml
      ↓
YOLOv8n Training From Scratch
      ↓
Model Validation
      ↓
New Unseen Traffic Video
      ↓
YOLO Object Detection
      ↓
Detected Output Video
```

---

# Video Testing

After training, the model was applied to a **new traffic video that was not included in the training dataset**.

The purpose of this step was to evaluate the model in a real traffic-video scenario and check whether it could detect the trained traffic classes frame-by-frame.

The output video contains:

- Bounding boxes
- Class names
- Confidence scores

### Input Video and output video

https://drive.google.com/drive/folders/1sOSJKud3QHo2H3KlGuUyYQYDZjOeJgGy?usp=drive_link


# Challenges Faced

### 1. Class Imbalance

The biggest challenge was the unequal number of objects between classes.

`Auto` had **4,100 objects**, while `Truck` had only **48** and `Bicycle` had **100**.

As a result, the model learned the majority classes better than the minority classes.

### 2. Limited Dataset Size

Only approximately **1,151 frames** were used for training, validation, and testing.

Training a YOLO model from scratch with a relatively small dataset limits the model's ability to generalize to different traffic conditions.

### 3. Different Object Frequencies

Some objects appeared frequently in the traffic scenes while others appeared rarely. This made it difficult to achieve balanced performance across all seven classes.

### 4. Real-World Video Detection

Testing on a new traffic video introduced variations in object size, position, traffic density, and scene conditions that were not always present in the training frames.

---

# Limitations

The current model has weaker performance on underrepresented classes.

The main reason is the limited number of training examples for these classes.

The current dataset can be improved by collecting more examples for minority classes and balancing the dataset.

---

# Future Improvements

- Increase the overall dataset size.
- Collect more frames.
- Balance the number of objects across classes.
- Collect traffic videos from different locations.
- Include different lighting and weather conditions.
- Perform additional model and hyperparameter tuning.
- Test on multiple unseen traffic videos.
- Add object tracking for continuous video detection.