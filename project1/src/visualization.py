import cv2


import cv2


def drawDetections(image, results):

    annotatedImage = image.copy()

    boxes = results[0].boxes


    for box in boxes:

        coordinates = box.xyxy.cpu().numpy()[0]

        x1, y1, x2, y2 = map(
            int,
            coordinates
        )

        classId = int(
            box.cls.cpu().numpy()[0]
        )


        confidence = float(
            box.conf.cpu().numpy()[0]
        )


        if classId == 0:

            color = (255,0,0)
            label = "Empty"

        else:

            color = (0,0,255)
            label = "Occupied"



        cv2.rectangle(
            annotatedImage,
            (x1,y1),
            (x2,y2),
            color,
            2
        )


        cv2.putText(
            annotatedImage,
            f"{label} {confidence:.2f}",
            (x1,y1-5),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.4,
            color,
            1
        )


    return annotatedImage
def drawStatistics(image, statistics):

    outputImage = image.copy()


    # Text values
    total = statistics["Total Spaces"]
    empty = statistics["Empty Spaces"]
    occupied = statistics["Occupied Spaces"]
    percentage = statistics["Occupancy Percentage"]


    # Create background panel
    cv2.rectangle(
        outputImage,
        (10, 10),
        (250, 150),
        (0, 0, 0),
        -1
    )


    # Add title

    cv2.putText(
        outputImage,
        "Parking Status",
        (20, 35),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.8,
        (255,255,255),
        2
    )


    # Total spaces

    cv2.putText(
        outputImage,
        f"Total: {total}",
        (20,65),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.5,
        (255,255,255),
        1
    )


    # Occupied

    cv2.putText(
        outputImage,
        f"Occupied: {occupied}",
        (20,90),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.5,
        (0,0,255),
        1
    )


    # Empty

    cv2.putText(
        outputImage,
        f"Available: {empty}",
        (20,115),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.5,
        (0,255,0),
        1
    )


    # Percentage

    cv2.putText(
        outputImage,
        f"Occupancy: {percentage}%",
        (20,140),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.5,
        (255,255,255),
        1
    )


    return outputImage