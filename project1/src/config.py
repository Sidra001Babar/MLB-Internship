import os

baseDir = os.path.dirname(
    os.path.dirname(
        os.path.abspath(__file__)
    )
)

modelPath = os.path.join(
    baseDir,
    "models",
    "best.pt"
)

imageFolder = os.path.join(
    baseDir,
    "dataset",
    "test",
    "images"
)

outputFolder = os.path.join(
    baseDir,
    "output",
    "predictions"
)

os.makedirs(outputFolder, exist_ok=True)

confidenceThreshold = 0.25