# Traffic Object Detection, Tracking and Counting

## Project Overview

This project uses a previously trained **YOLOv8n traffic detection model (`best.pt`)** to perform object detection, tracking, and counting on a new unseen traffic video.

The trained model is combined with the **ByteTrack object tracker** to track individual traffic objects across video frames, display their movement paths, and count how many objects of each class cross a virtual counting line.

---

## Project Workflow

```text
Trained YOLOv8 Model (best.pt)
              ↓
       Load Trained Model
              ↓
     New Unseen Traffic Video
              ↓
       YOLO Object Detection
              ↓
        ByteTrack Tracking
              ↓
      Unique Tracking IDs
              ↓
       Tracking Tail / Path
              ↓
       Virtual Counting Line
              ↓
      Line-Crossing Detection
              ↓
       Per-Class Object Count
              ↓
    Final Tracked & Counted Video

```

## Input Video and output video

https://drive.google.com/drive/folders/1NBZSSOcH4NZ2UHHOJ0PbVwLCW6AS1zso?usp=drive_link
