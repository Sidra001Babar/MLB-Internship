# Vehicle Detection using YOLOv8

## Overview

This project demonstrates **Object Detection** using the **YOLOv8 (You Only Look Once)** model from the Ultralytics library. A pre-trained YOLOv8 Nano model was used to detect vehicles in a public Vehicle Detection dataset downloaded from **Roboflow Universe**. The model identifies objects in images, draws bounding boxes around them, assigns class labels, and provides confidence scores for each detection.

---

# What is Object Detection?

**Object Detection** is a computer vision task that identifies **what objects are present in an image** and **where they are located**. The output consists of:

- Bounding Boxes
- Class Labels
- Confidence Scores

Unlike image classification, object detection can detect **multiple objects** in a single image.

---

# How is Object Detection Different from Image Classification?

| Image Classification | Object Detection |
|----------------------|------------------|
| Predicts the class of the entire image. | Detects and localizes multiple objects within an image. |
| Produces only a class label. | Produces bounding boxes, class labels, and confidence scores. |
| Does not identify object locations. | Identifies the location of each detected object. |

Example:

**Image Classification**

```
Prediction:
Car
```

**Object Detection**

```
Car → Bounding Box
Truck → Bounding Box
Bus → Bounding Box
```

---

# What is YOLO?

**YOLO (You Only Look Once)** is a deep learning-based object detection algorithm that detects and localizes objects in a **single forward pass** through a neural network.

Key features of YOLO include:

- Real-time object detection
- High detection speed
- Good detection accuracy
- Simultaneous object localization and classification

For this project, the **YOLOv8 Nano (`yolov8n.pt`)** pre-trained model from Ultralytics was used.

---

# Dataset Used

A **Vehicle Detection** dataset was downloaded from **Roboflow Universe** in **YOLOv8 format**.

### Dataset Information

- **Dataset:** Vehicle Detection
- **Source:** Roboflow Universe
- **Format:** YOLOv8
- **Number of Classes:** 12

Dataset Classes:

- big bus
- big truck
- bus-l-
- bus-s-
- car
- mid truck
- small bus
- small truck
- truck-l-
- truck-m-
- truck-s-
- truck-xl-

---

# Objects Detected

The pre-trained YOLOv8 model detected common vehicle categories such as:

- Car
- Bus
- Truck

Each detected object was displayed with:

- Bounding Box
- Class Label
- Confidence Score

The prediction results were automatically saved with annotated bounding boxes.

---

# Observations

- The YOLOv8 model successfully detected most visible vehicles in the test images.
- Large and clearly visible vehicles were detected with high confidence.
- Some distant or partially visible vehicles had lower confidence scores.
- Since the pre-trained YOLOv8 model was trained on the COCO dataset, it predicted generic classes such as **car**, **bus**, and **truck** instead of the custom dataset classes (e.g., **big truck** or **truck-xl-**).
- To accurately recognize all 12 custom vehicle categories, the model would need to be fine-tuned on the downloaded Vehicle Detection dataset.

---

# Technologies Used

- Python
- Ultralytics YOLOv8
- Roboflow Universe

---

# Output

The prediction results include:

- Bounding Boxes
- Vehicle Class Labels
- Confidence Scores

The output images were automatically saved in the output directory after inference.

---

# Conclusion

This project demonstrated how to perform object detection using a pre-trained YOLOv8 model on a public Vehicle Detection dataset. The model successfully detected common vehicle categories and generated annotated images with bounding boxes and confidence scores. The experiment also highlighted the difference between using a generic pre-trained model and a model fine-tuned on a custom dataset.