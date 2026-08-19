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

The main reason is that the pretrained model started with useful visual features learned from the COCO dataset. With only **40 training images**, transfer learning gives the model a strong initialization, whereas the scratch model has to learn useful visual representations from a very small dataset.

Overall, this experiment demonstrates that **fine-tuning pretrained weights is much more effective than training from scratch for a small custom instance segmentation dataset**.