# Similar & Duplicate Image Finder

A computer vision project that finds **visually similar images** and **exact/near-duplicate images** using two different approaches:

1. **MobileNetV2 feature embeddings + Cosine Similarity**
2. **Perceptual Hashing (pHash) + Hamming Distance**

The project also performs a mandatory robustness test using three modified versions of an original image:

- Resized
- Cropped
- Brightness-changed

The final system generates similarity results, duplicate reports, and visual result grids.

---

# 1. Project Objective

The objective of this project is to build a tool that can:

- Load a dataset containing 20–30 images.
- Handle different image categories.
- Extract visual feature embeddings using a pretrained CNN.
- Find the top 5 most visually similar images for a query image.
- Detect exact/near-duplicate images using perceptual hashing.
- Test whether modified versions of an image can still be recognized.
- Generate visual result grids.
- Save similarity results as CSV and JSON.
- Save duplicate detection results as JSON.

---

# 2. Dataset

The project uses a dataset of **24 images**.

The dataset contains different categories of images:

```text
Dataset
│
├── 5 Car images
├── 5 Tree images
├── 5 Black Rose images
├── 5 Cat images
│
└── 4 Home images
    ├── 21.jpg
    ├── 21_resized.jpg
    ├── 21_cropped.jpg
    └── 21_brightness.jpg
```

# 3. Project Structure
``` text
Task23/
│
├── dataset/
│   ├── 1.jpg
│   ├── 2.jpg
│   ├── ...
│   ├── 21.jpg
│   ├── 21_brightness.jpg
│   ├── 21_cropped.jpg
│   ├── 21_resized.jpg
│   ├── 22.jpg
│   ├── 23.jpg
│   └── 24.jpg
│
├── outputs/
│   ├── grids/
│   │   ├── 5_top5_results.jpg
│   │   ├── 10_top5_results.jpg
│   │   └── 21_duplicate_test.jpg
│   │
│   └── reports/
│       ├── similarity_report.csv
│       ├── similarity_report.json
│       └── duplicate_report.json
│
├── src/
│   ├── __init__.py
│   ├── config.py
│   ├── duplicate_detector.py
│   ├── feature_extractor.py
│   ├── image_loader.py
│   ├── main.py
│   ├── reporting.py
│   ├── similarity.py
│   └── visualizer.py
│
│
└── README.md
```

# 4. Technologies Used

* **Python:** The entire pipeline is implemented in Python.
* **TensorFlow / Keras:** Used to load the pretrained MobileNetV2 CNN.
* **MobileNetV2:** MobileNetV2 is used as a feature extractor. The classification head is removed and the CNN generates a feature vector for every image. The resulting embedding has **1280 dimensions**.

```text
21.jpg
    ↓
MobileNetV2
    ↓
1280-dimensional embedding
```

* **Cosine Similarity:** Compares two feature embeddings and measures how visually similar they are. A score closer to **1.0** means the images are more similar.
  * `0.97` → Very similar
  * `0.95` → Very similar
  * `0.87` → Visually similar
  * `0.48` → Less similar
  * `0.40` → Low similarity
  *(The exact interpretation depends on the dataset.)*

* **imagehash:** Used for perceptual hashing. The project uses `pHash` to detect images that have very similar visual structure.
* **Pillow:** Used for loading and processing images.
* **OpenCV:** Used where required for image processing.
* **Pandas:** Used to generate the CSV similarity report.
* **Matplotlib:** Used to create visual result grids.

---
# 5. Workflow
```text
                    ┌──────────────────────┐
                    │       DATASET        │
                    │      24 Images       │
                    └──────────┬───────────┘
                               │
                               ▼
                    ┌──────────────────────┐
                    │   STEP 1             │
                    │   Load Image Paths   │
                    └──────────┬───────────┘
                               │
                               ▼
                    Supported Images
                    1.jpg ... 24.jpg
                               │
                               ▼
                    ┌──────────────────────┐
                    │   STEP 2             │
                    │ Load MobileNetV2      │
                    │ Pretrained Model      │
                    └──────────┬───────────┘
                               │
                               ▼
                    ┌──────────────────────┐
                    │   STEP 3             │
                    │ Extract Features     │
                    │ from Every Image     │
                    └──────────┬───────────┘
                               │
                               ▼
                    ┌──────────────────────┐
                    │  Image Embeddings    │
                    │  1280 values/image   │
                    └──────────┬───────────┘
                               │
                 ┌─────────────┴─────────────┐
                 │                           │
                 ▼                           ▼
       ┌──────────────────┐        ┌──────────────────┐
       │ SIMILARITY       │        │ DUPLICATE        │
       │ SEARCH           │        │ DETECTION        │
       └────────┬─────────┘        └────────┬─────────┘
                │                           │
                ▼                           ▼
       Selected Query Images          All Image Pairs
       5, 10, 11, 18.jpg                    │
                │                           ▼
                ▼                     Calculate pHash
       Compare Embeddings                   │
                │                           ▼
                ▼                     Hamming Distance
       Cosine Similarity                    │
                │                           ▼
                ▼                     Threshold = 8
       Sort Highest → Lowest                │
                │                           ▼
                ▼                     Near Duplicates
       Select Top 5                         │
                │                           │
                ▼                           ▼
       Similarity Grids              Duplicate Results
                │                           │
                └─────────────┬─────────────┘
                              │
                              ▼
                    ┌──────────────────────┐
                    │ STEP 6               │
                    │ Modified Image Test  │
                    └──────────┬───────────┘
                               │
                               ▼
                       Original: 21.jpg
                               │
              ┌────────────────┼────────────────┐
              ▼                ▼                ▼
       Brightness Version   Resized Version   Cropped Version
              │                │                │
              └────────────────┼────────────────┘
                               │
                    ┌──────────┴──────────┐
                    ▼                     ▼
              CNN Similarity           pHash
                    │                     │
                    ▼                     ▼
             Cosine Score          Hamming Distance
                    │                     │
                    └──────────┬──────────┘
                               ▼
                     Compare Results
                               │
                               ▼
                     Duplicate Test Grid
                               │
                               ▼
                    ┌──────────────────────┐
                    │ STEP 7               │
                    │ Save Reports         │
                    └──────────┬───────────┘
                               │
             ┌─────────────────┼─────────────────┐
             ▼                 ▼                 ▼
       Similarity CSV    Similarity JSON    Duplicate JSON
```
# Conclusion

The **Similar & Duplicate Image Finder** successfully combines two different computer vision techniques to analyze image relationships:

- **MobileNetV2** is used to extract **1280-dimensional feature embeddings** from the dataset images.
- **Cosine similarity** is used on these embeddings to find the **Top 5 visually similar images** for query images such as `5.jpg`,`10.jpg`,`11.jpg` and `18.jpg`.
- **Perceptual hashing (pHash)** is used independently to detect **exact and near-duplicate images** using Hamming distance.
- The mandatory robustness test uses `21.jpg` and its three modified versions:
  - `21_resized.jpg`
  - `21_cropped.jpg`
  - `21_brightness.jpg`
- The results demonstrate that CNN-based visual similarity and pHash-based duplicate detection are complementary approaches. For example, a cropped image can still have high CNN similarity while having a larger pHash distance.
- The system generates **visual result grids** for similarity searches and the duplicate/modified-image test.
- Results are also saved in structured **CSV and JSON reports** for further analysis.

Overall, the project demonstrates a complete image analysis pipeline capable of distinguishing between **visual similarity** and **near-duplicate detection**, while also showing robustness against common image modifications such as resizing, cropping, and brightness changes.

