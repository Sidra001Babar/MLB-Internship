import cv2
import os

inputFolder = "input_videos"
outputFolder = "output_videos"
os.makedirs(outputFolder, exist_ok=True)
# Get all video files
video_files = os.listdir(inputFolder)
# Process each video
for video_name in video_files:
    input_path = os.path.join(inputFolder, video_name)
    # Create output file name
    proceesedVideo = "processed_" + video_name.split(".")[0] + ".avi"
    output_path = os.path.join(outputFolder, proceesedVideo)
    # Open video
    video = cv2.VideoCapture(input_path)
    if not video.isOpened():
        print("Cannot open", video_name)
        continue
    # Video properties
    fps = video.get(cv2.CAP_PROP_FPS)
    w = int(video.get(cv2.CAP_PROP_FRAME_WIDTH))
    h = int(video.get(cv2.CAP_PROP_FRAME_HEIGHT))
    total_frames = int(video.get(cv2.CAP_PROP_FRAME_COUNT))
    print("\nProcessing:", video_name)
    print("FPS:", fps)
    print("w:", w)
    print("h:", h)
    print("Total Frames:", total_frames)
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    output = cv2.VideoWriter(output_path, fourcc, fps, (w, h), False)
    while True:
        success, frame = video.read()
        if not success:
            break
        grayed = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        blured = cv2.GaussianBlur(grayed, (5,5), 0)
        edges = cv2.Canny(blured, 100, 200)
        cv2.imshow("Original Video", frame)
        cv2.imshow("Processed Video", edges)
        output.write(edges)
        if cv2.waitKey(30) & 0xFF == ord('q'):
            break
    video.release()
    output.release()
cv2.destroyAllWindows()
print("\nAll videos processed successfully!")