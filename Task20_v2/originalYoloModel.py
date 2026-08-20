from ultralytics import YOLO
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
UNSEEN_DIR = BASE_DIR / "unseen_images"
RESULTS_DIR = BASE_DIR / "unseen_results"
COCO_OUTPUT = RESULTS_DIR / "original_coco_model"
COCO_OUTPUT.mkdir(parents=True, exist_ok=True)
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
print("ORIGINAL YOLOv8n-Seg COCO PRETRAINED MODEL")
print("\nLoading yolov8n-seg.pt...")
model = YOLO("yolov8n-seg.pt")
print(f"\nNumber of unseen images: {len(unseen_images)}")
for image in unseen_images:
    print(" -", image.name)
print("\nRunning predictions...\n")
for image_path in unseen_images:
    print(f"Processing: {image_path.name}")
    results = model.predict(
        source=str(image_path),
        imgsz=320,
        conf=0.25,
        device="cpu",
        save=True,
        project=str(COCO_OUTPUT),
        name="predictions",
        exist_ok=True,
        verbose=False
    )
    for result in results:
        if result.boxes is None or len(result.boxes) == 0:
            print("   No objects detected.")
            continue
        for box in result.boxes:
            class_id = int(box.cls[0])
            confidence = float(box.conf[0])
            class_name = model.names[class_id]
            print(
                f"   Detected: {class_name} "
                f"(confidence: {confidence:.2f})"
            )
    print()
print("=" * 70)
print("COCO MODEL TEST COMPLETED")
print("\nPredictions saved at:")
print(
    COCO_OUTPUT / "predictions"
)
