import cv2
import os

inputRoot = "rawTrafficVideos"
outputRoot = "frames"
os.makedirs(outputRoot, exist_ok=True)
saved = 0   # Global counter

for folder in os.listdir(inputRoot):
    folderPath = os.path.join(inputRoot, folder)
    if not os.path.isdir(folderPath):
        continue
    for videoName in os.listdir(folderPath):
        videoPath = os.path.join(folderPath, videoName)
        cap = cv2.VideoCapture(videoPath)
        frame_no = 0
        while True:
            ret, frame = cap.read()
            if not ret:
                break
            if frame_no % 10 == 0:
                filename = f"image_{saved:05d}.jpg"
                cv2.imwrite(os.path.join(outputRoot, filename), frame)
                saved += 1
            frame_no += 1
        cap.release()
        print(f"{videoName} processed")
print(f"\nTotal frames saved: {saved}")