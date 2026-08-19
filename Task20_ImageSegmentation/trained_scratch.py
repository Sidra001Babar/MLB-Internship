from ultralytics import YOLO
import time
from pathlib import Path

baseDir = Path(__file__).resolve().parent
dataYaml = baseDir / "Laptop_Dataset" / "data.yaml"

print("MODEL 1: YOLOv8n-Segmentation - Training From Scratch")
model = YOLO("yolov8n-seg.yaml")
start_time = time.time()
results = model.train(
    data=str(dataYaml),
    epochs=50,
    imgsz=320,
    batch=4,
    device="cpu",
    pretrained=False,
    name="laptop_seg_scratch",
    save=True,
    val=True,
    single_cls=True,
    verbose=True
)
end_time = time.time()
training_time = end_time - start_time
print("TRAINING COMPLETED")
print(f"Training time: {training_time:.2f} seconds")
print(f"Training time: {training_time / 60:.2f} minutes")