import cv2
camera = cv2.VideoCapture(0)
# Check webcam
if not camera.isOpened():
    print("Cannot access webcam.")
    exit()

while True:
    # Capture one frame
    success, frame = camera.read()
    if not success:
        break
    cv2.imshow("Live Webcam", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release webcam
camera.release()
cv2.destroyAllWindows()