from ultralytics import YOLO

model = YOLO("yolov8n.pt")
image_path = r"D:\Downloads\vehicles.v1-abc.yolov8\test\images"

results = model.predict(
    source=image_path,
    conf=0.5,
    save=True,
    show=True
)

print("Object Detection Completed!")

for result in results:

    print(f"\nImage: {result.path}")

    for box in result.boxes:

        class_id = int(box.cls)
        class_name = model.names[class_id]
        confidence = float(box.conf)

        print(f"{class_name} : {confidence:.2f}")

    print("-" * 40)

    