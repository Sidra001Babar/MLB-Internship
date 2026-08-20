from ultralytics import YOLO
from pathlib import Path
import time
import csv

BASE_DIR = Path(__file__).resolve().parent
UNSEEN_DIR = BASE_DIR / "unseen_images"
MODEL2_DIR = BASE_DIR / "model2results"
RESULTS_DIR = BASE_DIR / "unseen_results"
MODEL2_OUTPUT = RESULTS_DIR / "model2_pretrained"
MODEL2_OUTPUT.mkdir(parents=True, exist_ok=True)

model2_files = list(MODEL2_DIR.rglob("best.pt"))

if not model2_files:
    raise FileNotFoundError(
        f"Model 2 best.pt not found inside:\n{MODEL2_DIR}"
    )

MODEL2_PATH = model2_files[0]

unseen_images = sorted(
    [
        p for p in UNSEEN_DIR.iterdir()
        if p.suffix.lower() in [".jpg", ".jpeg", ".png"]
    ]
)
if not unseen_images:
    raise FileNotFoundError(
        f"No unseen images found inside:\n{UNSEEN_DIR}"
    )

print("UNSEEN IMAGE TEST - MODEL 2 ONLY")
print(f"\nNumber of unseen images: {len(unseen_images)}")
for image in unseen_images:
    print(" -", image.name)
print("\nModel 2:")
print(MODEL2_PATH)
print("\nLoading Model 2...")
model = YOLO(str(MODEL2_PATH))
total_time = 0.0
image_times = []
print("MODEL 2 - YOLOv8n-Seg COCO PRETRAINED")
for image_path in unseen_images:
    start_time = time.perf_counter()
    model.predict(
        source=str(image_path),
        imgsz=320,
        conf=0.25,
        device="cpu",
        save=True,
        project=str(MODEL2_OUTPUT),
        name="predictions",
        exist_ok=True,
        verbose=False
    )
    end_time = time.perf_counter()
    inference_time = end_time - start_time
    total_time += inference_time
    image_times.append(inference_time)

    print(
        f"{image_path.name:<20}"
        f"{inference_time * 1000:.2f} ms"
    )

average_time = total_time / len(unseen_images)
print("\nTotal inference time:")
print(f"{total_time:.4f} seconds")

print("\nAverage inference time:")
print(f"{average_time * 1000:.2f} ms/image")
csv_path = RESULTS_DIR / "model2_unseen_inference_results.csv"

with open(csv_path, "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow([
        "Model",
        "Total Inference Time (seconds)",
        "Average Inference Time (ms/image)"
    ])
    writer.writerow([
        "YOLOv8n-seg COCO Pretrained",
        f"{total_time:.4f}",
        f"{average_time * 1000:.2f}"
    ])
print("\n" + "=" * 70)
print("MODEL 2 UNSEEN IMAGE TEST COMPLETED")
print("=" * 70)

print("\nPredictions saved in:")
print(MODEL2_OUTPUT)

print("\nCSV results saved in:")
print(csv_path)

print("\nModel 2 average inference:")
print(f"{average_time * 1000:.2f} ms/image")

print("\nNo validation mAP was recalculated.")
print("Existing training and validation results remain unchanged.")