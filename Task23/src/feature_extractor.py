from pathlib import Path

import numpy as np

from tensorflow.keras.applications import MobileNetV2
from tensorflow.keras.applications.mobilenet_v2 import (
    preprocess_input,
)
from tensorflow.keras.preprocessing import image


class FeatureExtractor:
    """
    Extract visual feature embeddings from images
    using a pretrained MobileNetV2 model.
    """

    def __init__(self):
        print("Loading MobileNetV2 model...")

        self.model = MobileNetV2(
            weights="imagenet",
            include_top=False,
            pooling="avg",
        )

        print("MobileNetV2 loaded successfully.")

    def extract(self, image_path: Path) -> np.ndarray:
        """
        Extract a feature embedding from a single image.
        """

        # Load image and resize to MobileNetV2 input size
        img = image.load_img(
            image_path,
            target_size=(224, 224),
        )

        # Convert image to NumPy array
        img_array = image.img_to_array(img)

        # Add batch dimension
        img_array = np.expand_dims(
            img_array,
            axis=0,
        )

        # Apply MobileNetV2 preprocessing
        img_array = preprocess_input(img_array)

        # Generate embedding
        embedding = self.model.predict(
            img_array,
            verbose=0,
        )

        # Remove batch dimension
        embedding = embedding[0]

        # Normalize embedding
        norm = np.linalg.norm(embedding)

        if norm != 0:
            embedding = embedding / norm

        return embedding