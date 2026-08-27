import json

from app.config import (
    IMAGE_DIR,
    OUTPUT_DIR,
    IMAGE_INDEX_JSON,
    SEARCH_RESULTS_JSON,
)

from app.captioner import ImageCaptioner
from app.clip_model import CLIPImageEncoder
from app.search import ImageSearchEngine

from app.visualizer import (
    create_all_images_grid,
    create_search_results_grid,
)


def build_index():
    print()
    print("BUILDING IMAGE INDEX")
    # STEP 1: Generate BLIP captions
    print()
    print("STEP 1: Generating BLIP captions...")

    captioner = ImageCaptioner()

    caption_records = (
        captioner.process_folder(
            IMAGE_DIR
        )
    )
    # STEP 2: Generate CLIP embeddings
    print()
    print(
        "STEP 2: Generating CLIP embeddings..."
    )

    encoder = CLIPImageEncoder()

    image_index = (
        encoder.process_folder(
            IMAGE_DIR,
            caption_records,
        )
    )
    # STEP 3: Save combined image index
    print()
    print(
        "STEP 3: Saving combined image index..."
    )

    OUTPUT_DIR.mkdir(
        parents=True,
        exist_ok=True,
    )

    with open(
        IMAGE_INDEX_JSON,
        "w",
        encoding="utf-8",
    ) as file:

        json.dump(
            image_index,
            file,
            indent=4,
            ensure_ascii=False,
        )

    print(
        f"Image index saved to: "
        f"{IMAGE_INDEX_JSON}"
    )
    # STEP 4: Create all-images caption grid
    print()
    print(
        "STEP 4: Creating image caption grid..."
    )

    create_all_images_grid(
        image_index
    )
    # COMPLETE
    print()
    print("IMAGE INDEX BUILD COMPLETE")
    print(
        f"Images processed: "
        f"{len(image_index)}"
    )

    print(
        f"Index file: "
        f"{IMAGE_INDEX_JSON}"
    )


def load_index():
    """
    Load the previously generated image index.
    """

    if not IMAGE_INDEX_JSON.exists():

        raise FileNotFoundError(
            "Image index not found. "
            "Please build the index first."
        )

    with open(
        IMAGE_INDEX_JSON,
        "r",
        encoding="utf-8",
    ) as file:

        return json.load(file)


def load_search_history():
    if not SEARCH_RESULTS_JSON.exists():

        return []

    try:

        with open(
            SEARCH_RESULTS_JSON,
            "r",
            encoding="utf-8",
        ) as file:

            history = json.load(
                file
            )
        if isinstance(
            history,
            dict,
        ):

            history = [
                history
            ]

        return history

    except (
        json.JSONDecodeError,
        OSError,
    ):

        return []


def run_search():
    # STEP 1: Load image index
    image_index = load_index()
    # STEP 2: Initialize CLIP search engine
    search_engine = (
        ImageSearchEngine(
            image_index
        )
    )
    print()
    print("NATURAL LANGUAGE IMAGE SEARCH")
    print(
        "Type 'exit' to stop."
    )
    # STEP 3: Search loop

    while True:
        query = input(
            "\nEnter search query: "
        ).strip()
        # EXIT
        if query.lower() == "exit":

            print()
            print(
                "Search ended."
            )

            break

        # EMPTY QUERY
        if not query:

            print(
                "Please enter a query."
            )

            continue

        try:

            # STEP 4: Perform CLIP search
            results = (
                search_engine.search(
                    query
                )
            )
            # STEP 5: Load complete history
            search_history = (
                load_search_history()
            )

            # STEP 6: Create cumulative grid
            create_search_results_grid(
                search_history
            )

            # STEP 7: Display current results
            print()
            print("=" * 70)

            print(
                f'Top {len(results)} results '
                f'for: "{query}"'
            )

            print("=" * 70)

            for result in results:

                print()

                print(
                    f"Rank       : "
                    f"{result['rank']}"
                )

                print(
                    f"Image      : "
                    f"{result['image']}"
                )

                print(
                    f"Similarity : "
                    f"{result['similarity']}"
                )

                print(
                    f"Caption    : "
                    f"{result['caption']}"
                )

        except Exception as error:

            print()
            print(
                f"Search error: {error}"
            )


def main():

    print()
    print("CAPTION & SEARCH PHOTO GALLERY")

    print()
    print(
        "1. Build / rebuild image index"
    )

    print(
        "2. Search images"
    )

    print(
        "3. Exit"
    )

    choice = input(
        "\nChoose an option: "
    ).strip()

    # BUILD INDEX

    if choice == "1":

        build_index()

    # SEARCH

    elif choice == "2":

        run_search()

    # EXIT

    elif choice == "3":

        print(
            "Goodbye."
        )

    # INVALID OPTION

    else:

        print(
            "Invalid option."
        )


if __name__ == "__main__":

    main()