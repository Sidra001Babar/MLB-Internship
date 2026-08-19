from ultralytics import YOLO
from pathlib import Path
import time
import csv


# PROJECT PATHS

BASE_DIR = Path(__file__).resolve().parent
# Unseen images
UNSEEN_DIR = BASE_DIR / "unseen_images"
# Existing trained models
MODEL1_DIR = BASE_DIR / "model1results"
MODEL2_DIR = BASE_DIR / "model2results"
# Output directory for unseen-image predictions
RESULTS_DIR = BASE_DIR / "unseen_results"
MODEL1_OUTPUT = RESULTS_DIR / "model1_scratch"
MODEL2_OUTPUT = RESULTS_DIR / "model2_pretrained"

# Create output directories
MODEL1_OUTPUT.mkdir(parents=True, exist_ok=True)
MODEL2_OUTPUT.mkdir(parents=True, exist_ok=True)


# Find best.pt

model1_files = list(MODEL1_DIR.rglob("best.pt"))
model2_files = list(MODEL2_DIR.rglob("best.pt"))

if not model1_files:
    raise FileNotFoundError(
        f"Model 1 best.pt not found inside:\n{MODEL1_DIR}"
    )

if not model2_files:
    raise FileNotFoundError(
        f"Model 2 best.pt not found inside:\n{MODEL2_DIR}"
    )

MODEL1_PATH = model1_files[0]
MODEL2_PATH = model2_files[0]


# Find unseen images

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


print("UNSEEN IMAGE TEST")

print(f"\nNumber of unseen images: {len(unseen_images)}")

for image in unseen_images:
    print(" -", image.name)


print("\nModel 1:")
print(MODEL1_PATH)

print("\nModel 2:")
print(MODEL2_PATH)


# FUNCTION: unseen image inference

def run_unseen_test(model_path, output_dir, model_name):

    print("\n" + "=" * 70)
    print(model_name)
    print("=" * 70)

    model = YOLO(str(model_path))

    total_time = 0.0
    image_times = []

    for image_path in unseen_images:

        start_time = time.perf_counter()

        model.predict(
            source=str(image_path),
            imgsz=320,
            conf=0.25,
            device="cpu",
            save=True,
            project=str(output_dir),
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

    return total_time, average_time, image_times


# MODEL 1

model1_total, model1_average, model1_times = run_unseen_test(
    MODEL1_PATH,
    MODEL1_OUTPUT,
    "MODEL 1 - YOLOv8n-Seg FROM SCRATCH"
)


# MODEL 2

model2_total, model2_average, model2_times = run_unseen_test(
    MODEL2_PATH,
    MODEL2_OUTPUT,
    "MODEL 2 - YOLOv8n-Seg COCO PRETRAINED"
)


# SAVE INFERENCE RESULTS

csv_path = RESULTS_DIR / "unseen_inference_results.csv"

with open(csv_path, "w", newline="") as f:

    writer = csv.writer(f)

    writer.writerow([
        "Model",
        "Total Inference Time (seconds)",
        "Average Inference Time (ms/image)"
    ])

    writer.writerow([
        "YOLOv8n-seg Scratch",
        f"{model1_total:.4f}",
        f"{model1_average * 1000:.2f}"
    ])

    writer.writerow([
        "YOLOv8n-seg COCO Pretrained",
        f"{model2_total:.4f}",
        f"{model2_average * 1000:.2f}"
    ])


# FINAL MESSAGE

print("UNSEEN IMAGE TEST COMPLETED")

print("\nPredictions saved in:")
print(RESULTS_DIR)

print("\nModel 1 average inference:")
print(f"{model1_average * 1000:.2f} ms/image")

print("\nModel 2 average inference:")
print(f"{model2_average * 1000:.2f} ms/image")

print("\nNo validation mAP was recalculated.")
print("Existing training and validation results remain unchanged.")