import json
from pathlib import Path

import torch
from PIL import Image
from transformers import (
    BlipProcessor,
    BlipForConditionalGeneration,
)

from app.config import (
    BLIP_MODEL_NAME,
    BLIP_MAX_NEW_TOKENS,
    DEVICE,
    SUPPORTED_IMAGE_EXTENSIONS,
)


class ImageCaptioner:

    def __init__(self):

        print("Loading BLIP model...")

        self.device = torch.device(DEVICE)

        print(
            f"Using device: {self.device}"
        )

        self.processor = (
            BlipProcessor.from_pretrained(
                BLIP_MODEL_NAME
            )
        )

        self.model = (
            BlipForConditionalGeneration
            .from_pretrained(
                BLIP_MODEL_NAME
            )
        )

        self.model.to(self.device)

        self.model.eval()

        print(
            "BLIP model loaded successfully."
        )

    def generate_caption(
        self,
        image_path,
    ):
        
        # Generate a caption for one image.
        image = (
            Image.open(image_path)
            .convert("RGB")
        )

        inputs = self.processor(
            images=image,
            return_tensors="pt",
        )

        inputs = {
            key: value.to(self.device)
            for key, value in inputs.items()
        }

        with torch.no_grad():

            output = self.model.generate(
                **inputs,
                max_new_tokens=BLIP_MAX_NEW_TOKENS,
            )

        caption = self.processor.decode(
            output[0],
            skip_special_tokens=True,
        )

        return caption.strip()

    def process_folder(
        self,
        input_dir,
    ):
        # Generate captions for all images.
        input_dir = Path(input_dir)
        image_files = sorted(
            [
                path
                for path in input_dir.iterdir()
                if (
                    path.is_file()
                    and path.suffix.lower()
                    in SUPPORTED_IMAGE_EXTENSIONS
                )
            ]
        )

        if not image_files:

            raise ValueError(
                "No supported images found."
            )
        if len(image_files) < 20:

            raise ValueError(
                f"Dataset contains only "
                f"{len(image_files)} images. "
                f"At least 20 images are required."
            )

        if len(image_files) > 25:

            raise ValueError(
                f"Dataset contains "
                f"{len(image_files)} images. "
                f"Maximum allowed is 25."
            )

        print("BLIP IMAGE CAPTIONING")
        print(
            f"Images found: {len(image_files)}"
        )
        results = []

        for index, image_path in enumerate(
            image_files,
            start=1,
        ):

            print(
                f"[{index}/{len(image_files)}] "
                f"{image_path.name}"
            )

            caption = (
                self.generate_caption(
                    image_path
                )
            )

            print(
                f"Caption: {caption}"
            )

            results.append(
                {
                    "image": image_path.name,
                    "caption": caption,
                }
            )
        return results