from pathlib import Path
############# PROJECT DIRECTORIES
# Project root
BASE_DIR = Path(__file__).resolve().parent.parent

# Dataset containing the 24 images
DATASET_DIR = BASE_DIR / "dataset"
# Output directories
OUTPUT_DIR = BASE_DIR / "outputs"
GRID_DIR = OUTPUT_DIR / "grids"
REPORT_DIR = OUTPUT_DIR / "reports"
# IMAGE SETTINGS
# MobileNetV2 expects 224 x 224 images
IMAGE_SIZE = (224, 224)
######## SIMILARITY SETTINGS

# Number of similar images to return
TOP_K = 5
# DUPLICATE SETTINGS
PHASH_THRESHOLD = 8
# SUPPORTED IMAGE EXTENSIONS
SUPPORTED_EXTENSIONS = {
    ".jpg",
    ".jpeg",
    ".png",
    ".bmp",
    ".webp",
}
########### QUERY IMAGES

# Images used for CNN similarity search
SIMILARITY_QUERIES = [
    "5.jpg",
    "10.jpg",
    "11.jpg",
    "18.jpg",
]

# Image used for the mandatory modified-image test
DUPLICATE_TEST_IMAGE = "21.jpg"
# CREATE OUTPUT DIRECTORIES
GRID_DIR.mkdir(parents=True, exist_ok=True)
REPORT_DIR.mkdir(parents=True, exist_ok=True)