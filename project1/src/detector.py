from ultralytics import YOLO
from config import modelPath, confidenceThreshold
class ParkingDetector:
    def __init__(self):
        self.model = YOLO(modelPath)

    def detect(self, image):
        results = self.model.predict(
            source=image,
            conf=confidenceThreshold,
            verbose=True
        )
        print(image.shape)
        return results