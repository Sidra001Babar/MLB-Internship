from src.config import (
    DATASET_DIR,
    GRID_DIR,
    REPORT_DIR,
    SIMILARITY_QUERIES,
    DUPLICATE_TEST_IMAGE,
)

from src.duplicate_detector import (
    find_duplicates,
    calculate_phash,
    calculate_hamming_distance,
    is_near_duplicate,
)

from src.feature_extractor import (
    FeatureExtractor,
)

from src.image_loader import (
    get_image_paths,
)

from src.reporting import (
    save_duplicate_report_json,
    save_similarity_report_csv,
    save_similarity_report_json,
)

from src.similarity import (
    find_top_similar,
)

from src.visualizer import (
    create_similarity_grid,
    create_duplicate_grid,
)


def main():

    print("=" * 70)
    print("SIMILAR & DUPLICATE IMAGE FINDER")
    print("=" * 70)

    # STEP 1 — Load dataset

    image_paths = get_image_paths()

    print(
        f"\nFound {len(image_paths)} images."
    )
    # STEP 2 — Load MobileNetV2

    extractor = FeatureExtractor()

    # STEP 3 — Extract embeddings
    print("\nExtracting image embeddings...\n")

    embeddings = {}

    for image_path in image_paths:

        print(
            f"Processing: {image_path.name}"
        )

        embeddings[image_path.name] = (
            extractor.extract(image_path)
        )

    print(
        "\nFeature extraction complete."
    )

    # STEP 4 — Similarity search
    print("\n" + "=" * 70)
    print("SIMILARITY SEARCH")
    print("=" * 70)

    all_similarity_results = {}

    for query_image in SIMILARITY_QUERIES:

        if query_image not in embeddings:

            print(
                f"\nWARNING: {query_image} "
                f"not found in dataset."
            )

            continue

        print(
            f"\nQuery image: {query_image}"
        )

        results = find_top_similar(
            query_name=query_image,
            embeddings=embeddings,
            top_k=5,
        )

        all_similarity_results[
            query_image
        ] = results

        print("\nTop 5 similar images:\n")

        for rank, (
            image_name,
            score,
        ) in enumerate(
            results,
            start=1,
        ):

            print(
                f"{rank}. "
                f"{image_name:<25} "
                f"Similarity: {score:.4f}"
            )

        ######## Create similarity result grid

        query_path = (
            DATASET_DIR / query_image
        )

        grid_path = (
            GRID_DIR
            / f"{query_path.stem}_top5_results.jpg"
        )

        create_similarity_grid(
            query_path=query_path,
            results=results,
            dataset_dir=DATASET_DIR,
            output_path=grid_path,
        )

        print(
            f"\nGrid saved to: {grid_path}"
        )

    ######## STEP 5 — Perceptual hash duplicate detection

    print("\n" + "=" * 70)
    print("PERCEPTUAL HASH DUPLICATE DETECTION")
    print("=" * 70)

    duplicate_pairs = find_duplicates(
        image_paths
    )

    if duplicate_pairs:

        print(
            f"\nFound {len(duplicate_pairs)} "
            f"near-duplicate pairs:\n"
        )

        for pair in duplicate_pairs:

            print(
                f"{pair['image_1']:<25} "
                f"<-> "
                f"{pair['image_2']:<25} "
                f"Distance: "
                f"{pair['hamming_distance']}"
            )

    else:

        print(
            "\nNo near-duplicate pairs found."
        )

    print("\n" + "=" * 70)
    print("MANDATORY MODIFIED IMAGE TEST")
    print("=" * 70)

    original_path = (
        DATASET_DIR / DUPLICATE_TEST_IMAGE
    )

    # Check original exists
    if not original_path.exists():

        print(
            f"\nWARNING: "
            f"{DUPLICATE_TEST_IMAGE} "
            f"not found in dataset."
        )

    else:

        modified_names = [
            "21_brightness.jpg",
            "21_resized.jpg",
            "21_cropped.jpg",
        ]

        # Get original pHash
        original_hash = calculate_phash(
            original_path
        )

        # Find original embedding
        original_embedding = embeddings.get(
            DUPLICATE_TEST_IMAGE
        )

        modified_results = []

        for image_name in modified_names:

            image_path = (
                DATASET_DIR / image_name
            )

            # Check modified image exists
            if not image_path.exists():

                print(
                    f"\nWARNING: "
                    f"{image_name} "
                    f"not found in dataset."
                )

                continue

            # pHash comparison

            modified_hash = calculate_phash(
                image_path
            )

            hamming_distance = (
                calculate_hamming_distance(
                    original_hash,
                    modified_hash,
                )
            )

            near_duplicate = (
                is_near_duplicate(
                    hamming_distance
                )
            )

            # CNN similarity

            cosine_score = 0.0

            if original_embedding is not None:

                modified_results_for_image = (
                    find_top_similar(
                        query_name=DUPLICATE_TEST_IMAGE,
                        embeddings={
                            DUPLICATE_TEST_IMAGE:
                                original_embedding,
                            image_name:
                                embeddings[image_name],
                        },
                        top_k=1,
                    )
                )

                if modified_results_for_image:

                    returned_name, returned_score = (
                        modified_results_for_image[0]
                    )

                    if returned_name == image_name:

                        cosine_score = float(
                            returned_score
                        )

            # Print result
            print(
                f"\n{DUPLICATE_TEST_IMAGE} "
                f"<-> "
                f"{image_name}"
            )

            print(
                f"CNN similarity: "
                f"{cosine_score:.4f}"
            )

            print(
                f"Hamming distance: "
                f"{int(hamming_distance)}"
            )

            print(
                f"pHash near duplicate: "
                f"{near_duplicate}"
            )

            # Store result for grid

            modified_results.append(
                {
                    "image": image_name,
                    "cosine_similarity": float(
                        cosine_score
                    ),
                    "hamming_distance": int(
                        hamming_distance
                    ),
                    "near_duplicate": bool(
                        near_duplicate
                    ),
                }
            )

        # Create duplicate test grid

        if modified_results:

            duplicate_grid_path = (
                GRID_DIR
                / "21_duplicate_test.jpg"
            )

            create_duplicate_grid(
                original_path=original_path,
                modified_results=modified_results,
                dataset_dir=DATASET_DIR,
                output_path=duplicate_grid_path,
            )

            print(
                f"\nDuplicate test grid saved to: "
                f"{duplicate_grid_path}"
            )

    # STEP 7 — Save reports
    print("\n" + "=" * 70)
    print("SAVING REPORTS")
    print("=" * 70)

    # Similarity CSV

    similarity_csv = (
        REPORT_DIR
        / "similarity_report.csv"
    )

    save_similarity_report_csv(
        all_similarity_results,
        similarity_csv,
    )

    print(
        f"\nSimilarity CSV: "
        f"{similarity_csv}"
    )

    # Similarity JSON

    similarity_json = (
        REPORT_DIR
        / "similarity_report.json"
    )

    save_similarity_report_json(
        all_similarity_results,
        similarity_json,
    )

    print(
        f"Similarity JSON: "
        f"{similarity_json}"
    )

    # Duplicate JSON

    duplicate_json = (
        REPORT_DIR
        / "duplicate_report.json"
    )

    save_duplicate_report_json(
        duplicate_pairs,
        duplicate_json,
    )

    print(
        f"Duplicate JSON: "
        f"{duplicate_json}"
    )

    # COMPLETE

    print("PROJECT COMPLETE")

    print(
        "\nResults saved successfully."
    )


if __name__ == "__main__":
    main()