from pathlib import Path


# PROJECT PATHS
BASE_DIR = Path(__file__).resolve().parent.parent
IMAGE_DIR = BASE_DIR / "images"
OUTPUT_DIR = BASE_DIR / "outputs"
EMBEDDINGS_DIR = OUTPUT_DIR / "embeddings"
BLIP_MODEL_NAME = (
    "Salesforce/blip-image-captioning-base"
)

# CPU-friendly CLIP model
CLIP_MODEL_NAME = (
    "openai/clip-vit-base-patch32"
)
DEVICE = "cpu"

# IMAGE SETTINGS
SUPPORTED_IMAGE_EXTENSIONS = {
    ".jpg",
    ".jpeg",
    ".png",
    ".webp",
}

# DATASET SETTINGS

MIN_IMAGES = 20
MAX_IMAGES = 25
# BLIP SETTINGS
BLIP_MAX_NEW_TOKENS = 50
# SEARCH SETTINGS

TOP_K_RESULTS = 5
SIMILARITY_DECIMAL_PLACES = 4

# OUTPUT FILES
# Combined image information:
# image name + BLIP caption + CLIP embedding path
IMAGE_INDEX_JSON = (
    OUTPUT_DIR / "image_index.json"
)

SEARCH_RESULTS_JSON = (
    OUTPUT_DIR / "search_results.json"
)

ABSTRACT_QUERY_EVALUATION_JSON = (
    OUTPUT_DIR
    / "abstract_query_evaluation.json"
)

# VISUAL REPORT SETTINGS
# Grid containing every input image
# with its BLIP-generated caption.

ALL_IMAGES_GRID = (
    OUTPUT_DIR
    / "all_images_with_captions.jpg"
)

# Cumulative grid containing every search
# query and its Top-5 results.

SEARCH_RESULTS_GRID = (
    OUTPUT_DIR
    / "all_search_results.jpg"
)


# GRID SETTINGS
# Number of images displayed horizontally.

GRID_COLUMNS = 4

# Matplotlib figure size per grid cell.

GRID_IMAGE_WIDTH = 4
GRID_IMAGE_HEIGHT = 4
# Every image is padded/resized to this
# exact size while preserving aspect ratio.

GRID_IMAGE_SIZE = (
    300,
    220,
)