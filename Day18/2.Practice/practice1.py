import cv2

######## Step 1: Open the video
video = cv2.VideoCapture("videoo.mp4")
if not video.isOpened():
    print("Error: Cannot open video.")
    exit()

######## Step 2: Get video information
fps = video.get(cv2.CAP_PROP_FPS)
w = int(video.get(cv2.CAP_PROP_FRAME_WIDTH))
h = int(video.get(cv2.CAP_PROP_FRAME_HEIGHT))
totalFrames = int(video.get(cv2.CAP_PROP_FRAME_COUNT))

print("Video Information")
print("-------------------")
print("FPS:", fps)
print("Width:", w)
print("Height:", h)
print("Total Frames:", totalFrames)

####### Step 3: Create Video Writer
fourcc = cv2.VideoWriter_fourcc(*'XVID')
output = cv2.VideoWriter("output.avi", fourcc, fps, (w, h), False) # False means grayscale video

############ Step 4: Read video frame by frame
while True:
    success, frame = video.read()
    # Stop when video ends
    if not success:
        break
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    edges = cv2.Canny(gray, 100, 200)
    cv2.imshow("Canny Edge Detection", edges)
    output.write(edges)
    # Press q to stop
    if cv2.waitKey(30) & 0xFF == ord('q'):
        break

########## Step 5: Release resources
video.release()
output.release()
cv2.destroyAllWindows()
print("Processing Completed!")