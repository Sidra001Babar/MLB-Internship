from ultralytics import YOLO
import time
from pathlib import Path

baseDir = Path(__file__).resolve().parent
dataYaml = baseDir / "Laptop_Dataset" / "data.yaml"
resultDir = baseDir / "model2results"

print("MODEL 2: YOLOv8n-Segmentation - COCO Pretrained")
model = YOLO("yolov8n-seg.pt")
start_time = time.time()
results = model.train(
    data=str(dataYaml),
    epochs=50,
    imgsz=320,
    batch=4,
    device="cpu",
    pretrained=True,
    project=str(resultDir),
    name="training",
    save=True,
    val=True,
    single_cls=True,
    verbose=True
)
end_time = time.time()
training_time = end_time - start_time
print("MODEL 2 TRAINING COMPLETED")
print(f"Training time: {training_time:.2f} seconds")
print(f"Training time: {training_time / 60:.2f} minutes")

print("\nBest model saved at:")
print(
    resultDir /
    "training" /
    "weights" /
    "best.pt"
)