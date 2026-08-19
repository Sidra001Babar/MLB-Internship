# Laptop Instance Segmentation — YOLOv8n-seg

## Overview

This project implements a small custom **instance segmentation dataset for laptops** and compares two YOLOv8n-seg models:

- **Model 1:** YOLOv8n-seg trained from scratch using random weights
- **Model 2:** YOLOv8n-seg fine-tuned from pretrained COCO weights

Both models were trained using the **same dataset and CPU-friendly training settings** to provide a fair comparison.

---

## Dataset

- **Object class:** Laptop
- **Total images:** 50
- **Training images:** 40
- **Validation images:** 5
- **Test images:** 5
- **Annotation:** Manually created polygon masks
- **Annotation tool:** CVAT
- **Export format:** YOLO Segmentation

### Dataset Structure

```text
Laptop_Dataset/
├── images/
│   ├── train/     # 40 images
│   ├── val/       # 5 images
│   └── test/      # 5 images
│
├── labels/
│   ├── train/
│   ├── val/
│   └── test/
│
└── data.yaml
```
## Workflow
```text
Raw Laptop Images
        ↓
Manual Polygon Annotation in CVAT
        ↓
Export Annotations in YOLO Segmentation Format
        ↓
Organize Dataset
        ↓
Train / Validation / Test Split
        ↓
Dataset Verification
        ↓
        ┌──────────────────────────────┐
        │                              │
        ▼                              ▼
Model 1                         Model 2
YOLOv8n-seg                     YOLOv8n-seg
Random Weights                  COCO Pretrained Weights
        │                              │
        └──────────────┬───────────────┘
                       ↓
              Same Training Settings
                       ↓
              Validation Evaluation
                       ↓
              Test / Unseen Images
                       ↓
          Compare Segmentation Results
                       ↓
        Mask mAP + Training + Inference Time
```

## Model Comparison

| Metric | Model 1 — YOLOv8n-seg Scratch | Model 2 — YOLOv8n-seg Pretrained |
|---|---:|---:|
| Initialization | Random Weights | COCO Pretrained Weights |
| Epochs | 50 | 50 |
| Image Size | 320 | 320 |
| Batch Size | 4 | 4 |
| Device | CPU | CPU |
| Mask Precision | 0.498 | **0.969** |
| Mask Recall | 0.600 | **1.000** |
| Mask mAP50 | 0.617 | **0.995** |
| Mask mAP50-95 | 0.348 | **0.945** |
| Training Time | **9.94 min** | 11.04 min |
| Average Inference Time | 632.73 ms/image | **155.72 ms/image** |

## Results and Conclusion

The **COCO pretrained YOLOv8n-seg model performed significantly better** than the model trained from scratch.

Model 2 achieved:

- Much higher **Mask mAP50**: **0.995 vs 0.617**
- Much higher **Mask mAP50-95**: **0.945 vs 0.348**
- Higher **mask precision and recall**
- Lower measured inference time on the unseen-image test

Although Model 2 took slightly longer to train (**11.04 min vs 9.94 min**), it provided substantially better segmentation performance.

### Reason for Difference Between Model 1 and Model 2

- **Model 1** (`yolov8n-seg.yaml`) is trained **from scratch**, so all weights start randomly. It must learn basic features, object shapes, and laptop segmentation from the dataset itself.
- **Model 2** (`yolov8n-seg.pt`) uses **COCO pretrained weights**, so it already has learned useful visual features such as edges, shapes, textures, and object boundaries.
- Both models use the same dataset, epochs, image size, and batch size, but **50 epochs may not be enough for the scratch model** to learn good features.
- Therefore, Model 2 produces a much better laptop segmentation because **transfer learning gives it a strong starting point**, while Model 1 has to learn everything from zero.

**In short:**  
`Pretrained weights → faster/better learning → better segmentation`  
`Random weights → needs more training/data → poorer result at 50 epochs`