# Document Text Extraction Tool

An end-to-end pipeline that takes raw document photos (including tilted, blurry, or poorly-lit ones), enhances them, runs OCR with **EasyOCR**, compares raw vs. enhanced accuracy — including against manually-provided **ground truth** — and produces visual, JSON, CSV, and plain-text outputs for review.


---
## 2. How the Pipeline Works (Workflow)

The pipeline processes every image in `input/` through the following stages, orchestrated by `main.py`:

```
             ┌─────────────────────────┐
             │   input/*.jpg, *.png     │
             └────────────┬─────────────┘
                          │
        ┌─────────────────┴──────────────────┐
        │                                     │
        ▼                                     ▼
┌───────────────┐                   ┌───────────────────────┐
│  RAW IMAGE     │                   │  document_enhancer.py  │
│  → run_ocr()   │                   │  (preprocessing)       │
└───────┬────────┘                   └───────────┬────────────┘
        │                                        │
        │                     1. Perspective correction (auto-detect
        │                        document edges, warp to flat rectangle)
        │                     2. Grayscale conversion
        │                     3. Deskew (auto-detect & correct rotation angle)
        │                     4. Denoise (Non-Local Means)
        │                     5. Contrast enhancement (CLAHE)
        │                     6. Sharpening
        │                                        │
        │                                        ▼
        │                             ┌────────────────────┐
        │                             │  ENHANCED IMAGE      │
        │                             │  → run_ocr()         │
        │                             └──────────┬────────────┘
        │                                        │
        ▼                                        ▼
┌───────────────────────────────────────────────────────────┐
│              compare_ocr_results() — confidence based       │
│  • average confidence (raw vs enhanced)                     │
│  • detection count retention ratio                          │
│  • picks "raw" or "enhanced" as the FINAL result             │
└───────────────────────────┬─────────────────────────────────┘
                            │
                            ▼
              ┌─────────────────────────────┐
              │  ground_truth.py (optional)   │
              │  If ground_truth/<name>.txt    │
              │  exists:                        │
              │   • Character Error Rate (CER)  │
              │   • Word Error Rate (WER)       │
              │   • Accuracy % for raw/enhanced/│
              │     final                        │
              │   • Flags if confidence-based    │
              │     choice disagrees with what   │
              │     ground truth says is best    │
              └───────────────┬─────────────────┘
                              │
                              ▼
        ┌─────────────────────────────────────────┐
        │  Save outputs per image:                  │
        │  • enhanced image (JPG)                    │
        │  • raw OCR visualization (JPG)              │
        │  • enhanced OCR visualization (JPG)          │
        │  • final OCR visualization (JPG)             │
        │  • extracted text (TXT)                       │
        │  • full structured result (JSON)               │
        └─────────────────┬───────────────────────────┘
                          │
                          ▼
        ┌───────────────────────────────────────────┐
        │  After ALL images are processed:             │
        │  • comparison.csv — summary of every image    │
        │  • Auto-select the 3 hardest documents          │
        │    (lowest ground-truth accuracy, or lowest      │
        │     raw OCR confidence if no ground truth)         │
        │  • Save raw → preprocessed → OCR grid image for    │
        │    each into output/hardest_comparisons/             │
        └───────────────────────────────────────────────────┘
```

### Stage details

**A. Preprocessing (`document_enhancer.py`)**
| Step | Function | Purpose |
|---|---|---|
| Perspective correction | `correct_perspective()` | Detects the document's quadrilateral edges (via Canny edges or saturation mask) and warps it into a flat, front-facing rectangle. |
| Grayscale | `convert_to_grayscale()` | Simplifies the image for text-focused processing. |
| Deskew | `deskew_image()` | Detects the dominant text angle and rotates to correct tilt. |
| Denoise | `reduce_noise()` | Removes camera/scan noise using Non-Local Means denoising. |
| Contrast enhancement | `enhance_contrast()` | Applies CLAHE to improve legibility in poorly-lit images. |
| Sharpening | `sharpen_image()` | Unsharp-mask style sharpening to crisp up text edges. |

**B. OCR (`ocr_engine.py`)**
- `run_ocr()` — runs EasyOCR on an image (auto up-scaled 2x for better small-text detection), returns each detection's text, confidence (%), bounding box, and coordinates.
- `draw_ocr_results()` — draws bounding boxes + confidence score labels over the image.

**C. Ground Truth Scoring (`ground_truth.py`)** — *see Section 4 below.*

**D. Comparison Visualization (`comparison_visualizer.py`)**
- `create_comparison_grid()` — stacks the raw, preprocessed, and OCR-annotated images side-by-side with labels, used for the mandatory 3-hardest-document comparison.

**E. Orchestration (`main.py`)**
- Loops through every image in `input/`, runs the full flow above, writes all output files, and at the end:
  - Builds `output/comparison.csv` summarizing every image (confidence + ground-truth accuracy stats).
  - Automatically ranks documents by difficulty and saves before/after grids for the **3 hardest** into `output/hardest_comparisons/`.

---

## 3. Ground Truth Accuracy (Optional but Recommended)

To measure *actual* OCR accuracy (not just confidence scores), provide the real text of each document:

1. Create a `ground_truth/` folder next to `input/`.
2. For each image, create a `.txt` file with the **same base name** as the image, containing the exact text on the document.

```
input/
    receipt1.jpg
    resume1.png

ground_truth/
    receipt1.txt      ← exact text from receipt1.jpg
    resume1.txt        ← exact text from resume1.png
```

3. Formatting doesn't need to be pixel-perfect — the comparison normalizes text (lowercase, strips punctuation, collapses whitespace) before scoring. Word accuracy matters most.

If no matching ground truth file is found for an image, the pipeline simply skips accuracy scoring for it (no errors) — confidence-based comparison still runs as normal.

### What gets computed
For any image with ground truth available, `ground_truth.py` computes, for **raw**, **enhanced**, and the **final selected** OCR result:
- **Character Error Rate (CER)** and **Character Accuracy %**
- **Word Error Rate (WER)** and **Word Accuracy %**
- Whether the confidence-based "raw vs enhanced" decision actually matches what ground truth says is more accurate (`selection_matches_ground_truth`)

This is the most reliable way to judge whether preprocessing actually helped, since OCR confidence scores don't always correlate with real-world correctness.

---

## 4. Running the Pipeline

```bash
python main.py
```

Console output shows per-image progress (detections found, confidence scores, which version was selected, and ground-truth accuracy if available). All results are written to `output/`.

---

## 5. Output Reference

| File / Folder | Contents |
|---|---|
| `output/enhanced/<name>_enhanced.jpg` | Preprocessed image |
| `output/raw_ocr/<name>_raw_ocr.jpg` | Raw image with OCR boxes + confidence |
| `output/enhanced_ocr/<name>_enhanced_ocr.jpg` | Enhanced image with OCR boxes + confidence |
| `output/<name>_final_ocr.jpg` | Final selected result, visualized |
| `output/text/<name>.txt` | Extracted plain text (reading-order joined) |
| `output/json/<name>.json` | Full structured result: all detections, coordinates, confidences, deskew angle, perspective flag, selection reasoning, and ground-truth scores |
| `output/hardest_comparisons/hardest_N_<name>.jpg` | Side-by-side raw → preprocessed → OCR grid, for the 3 toughest documents |
| `output/comparison.csv` | One row per image: detection counts, confidence stats, ground-truth accuracy %, and which version (raw/enhanced) was chosen — plus whether that choice agreed with ground truth |

### JSON schema (per image)
```json
{
  "image": "receipt1.jpg",
  "deskew_angle": -1.4,
  "perspective_correction": true,
  "raw_ocr": [ { "text": "...", "confidence": 91.2, "bbox": [...], "coordinates": [...] } ],
  "enhanced_ocr": [ ... ],
  "final_ocr": [ ... ],
  "ocr_selection": "enhanced",
  "preprocessing_applied": true,
  "selection_reason": "Enhanced image improved OCR confidence without excessive detection loss.",
  "raw_average_confidence": 78.4,
  "enhanced_average_confidence": 88.9,
  "confidence_improvement": 10.5,
  "raw_detections_count": 22,
  "enhanced_detections_count": 21,
  "detection_ratio": 0.95,
  "final_extracted_text": "...",
  "ground_truth": {
    "available": true,
    "raw": { "character_accuracy": 84.1, "word_accuracy": 79.0, ... },
    "enhanced": { "character_accuracy": 93.7, "word_accuracy": 90.2, ... },
    "final": { "character_accuracy": 93.7, "word_accuracy": 90.2, ... },
    "best_choice": "enhanced",
    "selection_matches_ground_truth": true
  }
}
```

---

## 6. Selection Logic (Raw vs Enhanced)

`main.py` decides which OCR result to treat as "final" using confidence + detection retention:

1. If enhanced produced **zero** detections → use raw.
2. If raw produced **zero** detections → use enhanced.
3. If enhanced **lost more than 30%** of detections vs raw → use raw (preprocessing likely destroyed some text region).
4. If enhanced's **average confidence is higher** than raw's, and it didn't lose too many detections → use enhanced.
5. Otherwise → use raw.

When ground truth is available, this decision is cross-checked against actual accuracy, and any disagreement is flagged in both the console output and the CSV/JSON (`selection_matches_ground_truth`).

---

## Results & Conclusion

| Image | Raw Conf. | Enhanced Conf. | Raw Acc. (char/word) | Enhanced Acc. (char/word) | Final Used | Matches Ground Truth? |
|---|---|---|---|---|---|---|
| 1.png | 38.62% | 74.06% | 51.7% / 19.6% | 72.8% / 60.7% | Enhanced |  Yes |
| 2.jpg | 84.73% | 82.97% | 68.0% / 66.2% | 68.4% / 63.7% | Raw | No (enhanced was actually better) |
| 3.png | 78.42% | 71.56% | 97.0% / 92.3% | 96.0% / 85.0% | Raw | Yes |
| 4.jpg | 28.42% | 18.06% | 28.6% / 3.7% | 49.7% / 16.8% | Raw |  No (enhanced was actually better) |

**Key findings:**

- Preprocessing gave the biggest boost on **1.png**, nearly doubling both OCR confidence and ground-truth accuracy — confirming enhancement helps most on low-contrast/tilted images.
- **3.png** was already a clean, high-quality image, so preprocessing slightly *hurt* accuracy — correctly detected and reverted to raw.
- On **2.jpg** and **4.jpg**, the confidence-based selector picked *raw* even though ground truth shows *enhanced* was more accurate. This happened because confidence score and detection retention ratio don't always track true accuracy — especially on **4.jpg**, where enhancement lost 82% of detections (dense two-column resume text merging during preprocessing) but the fewer detections it *did* keep were more correct.
- **4.jpg** is the hardest document overall (lowest accuracy on both raw and enhanced), due to its small, dense multi-column text layout.
- Overall, ground-truth scoring shows the automated selector agreed with true accuracy in **2 out of 4** cases — highlighting why ground-truth evaluation is necessary rather than relying on OCR confidence alone.
