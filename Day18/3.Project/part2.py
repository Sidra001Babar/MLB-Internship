import cv2
camera = cv2.VideoCapture(0)
if not camera.isOpened():
    print("Cannot open webcam")
    exit()

while True:

    success, frame = camera.read()
    if not success:
        break
    grayed = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    blured = cv2.GaussianBlur(grayed, (5, 5), 0)
    edges = cv2.Canny(blured, 100, 200)
    cv2.imshow("Original Webcam", frame)
    cv2.imshow("Processed Webcam", edges)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
camera.release()
cv2.destroyAllWindows()