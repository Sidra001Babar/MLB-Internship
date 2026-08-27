import math

import matplotlib.pyplot as plt
from PIL import Image, ImageOps

from app.config import (
    IMAGE_DIR,
    ALL_IMAGES_GRID,
    SEARCH_RESULTS_GRID,
    GRID_COLUMNS,
    GRID_IMAGE_WIDTH,
    GRID_IMAGE_HEIGHT,
    GRID_IMAGE_SIZE,
)


def prepare_image(image_path):
    """
    Load an image and resize it to a fixed size
    while preserving its aspect ratio.

    Empty areas are padded so every image has
    exactly the same dimensions.
    """

    image = Image.open(
        image_path
    ).convert("RGB")

    image = ImageOps.pad(
        image,
        GRID_IMAGE_SIZE,
        method=Image.Resampling.LANCZOS,
    )

    return image


def create_all_images_grid(image_records):
    """
    Create a grid containing every image and
    its BLIP-generated caption.
    """

    if not image_records:
        return

    total_images = len(image_records)

    columns = GRID_COLUMNS

    rows = math.ceil(
        total_images / columns
    )

    figure, axes = plt.subplots(
        rows,
        columns,
        figsize=(
            columns * GRID_IMAGE_WIDTH,
            rows * GRID_IMAGE_HEIGHT,
        ),
    )

    # Normalize axes into a flat list
    if total_images == 1:

        axes = [axes]

    else:

        try:
            axes = axes.flatten()

        except AttributeError:
            axes = [axes]

    for index, record in enumerate(
        image_records
    ):

        axis = axes[index]

        image_path = (
            IMAGE_DIR / record["image"]
        )

        try:

            image = prepare_image(
                image_path
            )

            axis.imshow(image)

            axis.axis("off")

            caption = record.get(
                "caption",
                "",
            )

            axis.set_title(
                f"{record['image']}\n\n"
                f"{caption}",
                fontsize=10,
                wrap=True,
            )

        except Exception as error:

            axis.text(
                0.5,
                0.5,
                f"Error loading image\n"
                f"{record['image']}\n\n"
                f"{error}",
                ha="center",
                va="center",
            )

            axis.axis("off")

    # Hide unused cells
    for index in range(
        total_images,
        len(axes),
    ):

        axes[index].axis("off")

    figure.suptitle(
        "All Images with BLIP Captions",
        fontsize=18,
    )

    figure.tight_layout(
        rect=(0, 0, 1, 0.96)
    )

    figure.savefig(
        ALL_IMAGES_GRID,
        dpi=150,
        bbox_inches="tight",
    )

    plt.close(figure)

    print(
        f"All-images grid saved to: "
        f"{ALL_IMAGES_GRID}"
    )


def create_search_results_grid(search_history):

    if not search_history:
        print(
            "No search history available for grid."
        )
        return
    # GRID SETTINGS
    columns = GRID_COLUMNS
    # Every query gets:
    # 1 row for query
    # 2 rows for 5 images when using 4 columns
    rows_for_results = math.ceil(
        5 / columns
    )

    rows_per_query = (
        1 + rows_for_results
    )

    total_queries = len(
        search_history
    )

    total_rows = (
        total_queries
        * rows_per_query
    )

    # CREATE FIGURE
    figure, axes = plt.subplots(
        total_rows,
        columns,
        figsize=(
            columns * GRID_IMAGE_WIDTH,
            total_rows * GRID_IMAGE_HEIGHT,
        ),
    )

    # NORMALIZE AXES
    if hasattr(axes, "flatten"):
        axes = axes.flatten()
    else:
        axes = [axes]
    # PROCESS EACH QUERY
    axis_position = 0

    for query_number, query_record in enumerate(
        search_history,
        start=1,
    ):

        query = query_record.get(
            "query",
            "",
        )

        results = query_record.get(
            "results",
            [],
        )
        # QUERY HEADER
        header_axes = axes[
            axis_position:
            axis_position + columns
        ]

        # Put query in first cell
        header_axes[0].text(
            0.5,
            0.5,
            f'Query {query_number}\n\n'
            f'"{query}"',
            ha="center",
            va="center",
            fontsize=16,
            fontweight="bold",
        )

        header_axes[0].axis(
            "off"
        )

        # Hide remaining header cells
        for axis in header_axes[1:]:

            axis.axis(
                "off"
            )

        axis_position += columns

        # RESULT IMAGES

        result_axes = axes[
            axis_position:
            axis_position
            + (
                rows_for_results
                * columns
            )
        ]

        for index, result in enumerate(
            results[:5]
        ):

            axis = result_axes[
                index
            ]

            image_path = (
                IMAGE_DIR
                / result["image"]
            )

            try:

                image = prepare_image(
                    image_path
                )

                axis.imshow(
                    image
                )

                axis.axis(
                    "off"
                )

                axis.set_title(
                    f"Rank {result['rank']} | "
                    f"Similarity: "
                    f"{result['similarity']}\n\n"
                    f"{result['image']}\n"
                    f"{result['caption']}",
                    fontsize=10,
                    wrap=True,
                )

            except Exception as error:

                axis.text(
                    0.5,
                    0.5,
                    f"Error loading image\n"
                    f"{result['image']}\n\n"
                    f"{error}",
                    ha="center",
                    va="center",
                )

                axis.axis(
                    "off"
                )

        # Hide unused result cells
        for index in range(
            len(results),
            len(result_axes),
        ):

            result_axes[index].axis(
                "off"
            )

        axis_position += (
            rows_for_results
            * columns
        )

    # TITLE
    figure.suptitle(
        "Image Search Results History",
        fontsize=20,
        fontweight="bold",
    )

    # LAYOUT
    figure.tight_layout(
        rect=(
            0,
            0,
            1,
            0.97,
        )
    )

    # MAKE SURE OUTPUT DIRECTORY EXISTS
    SEARCH_RESULTS_GRID.parent.mkdir(
        parents=True,
        exist_ok=True,
    )

    # SAVE
    figure.savefig(
        SEARCH_RESULTS_GRID,
        dpi=150,
        bbox_inches="tight",
    )

    plt.close(
        figure
    )

    print()
    print(
        "Search-results grid saved to:"
    )

    print(
        SEARCH_RESULTS_GRID
    )