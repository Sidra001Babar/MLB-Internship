import os
import cv2

from detector import ParkingDetector
from config import imageFolder, outputFolder
from visualization import drawDetections, drawStatistics
from statistics import calculateStatistics


detector = ParkingDetector()


imageList = os.listdir(imageFolder)


for imageName in imageList:


    imagePath = os.path.join(
        imageFolder,
        imageName
    )


    image = cv2.imread(imagePath)


    if image is None:
        continue


    results = detector.detect(image)



    # Calculate parking statistics
    stats = calculateStatistics(results)


    print("\n###########")
    print(imageName)
    print("############")


    for key,value in stats.items():
        print(
            f"{key}: {value}"
        )



    annotatedImage = drawDetections(
        image,
        results
    )
    annotatedImage = drawStatistics(
    annotatedImage,
    stats
)
    annotatedImage = cv2.resize(
    annotatedImage,
    (1280,1280)
)

    outputPath = os.path.join(
        outputFolder,
        imageName
    )


    cv2.imwrite(
        outputPath,
        annotatedImage
    )


    print(
        f"{imageName} processed."
    )


print("\nAll images processed successfully.")