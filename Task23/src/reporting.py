import json
from pathlib import Path
from typing import Dict, List, Tuple

import pandas as pd


def save_similarity_report_csv(
    all_results: Dict[str, List[Tuple[str, float]]],
    output_path: Path,
):
    """
    Save similarity results as CSV.
    """

    rows = []

    for query_image, results in all_results.items():

        for rank, (image_name, score) in enumerate(
            results,
            start=1,
        ):

            rows.append(
                {
                    "query_image": query_image,
                    "similar_image": image_name,
                    "cosine_similarity": round(
                        score,
                        4,
                    ),
                    "rank": rank,
                }
            )

    dataframe = pd.DataFrame(rows)

    dataframe.to_csv(
        output_path,
        index=False,
    )


def save_similarity_report_json(
    all_results: Dict[str, List[Tuple[str, float]]],
    output_path: Path,
):
    """
    Save similarity results as JSON.
    """

    report = []

    for query_image, results in all_results.items():

        query_results = []

        for rank, (image_name, score) in enumerate(
            results,
            start=1,
        ):

            query_results.append(
                {
                    "rank": rank,
                    "image": image_name,
                    "cosine_similarity": round(
                        score,
                        4,
                    ),
                }
            )

        report.append(
            {
                "query_image": query_image,
                "results": query_results,
            }
        )

    with open(
        output_path,
        "w",
        encoding="utf-8",
    ) as file:

        json.dump(
            report,
            file,
            indent=4,
        )


def save_duplicate_report_json(
    duplicate_pairs: List[dict],
    output_path: Path,
):
    """
    Save perceptual-hash duplicate results as JSON.
    Handles NumPy numeric types.
    """

    report = []

    for pair in duplicate_pairs:

        report.append(
            {
                "image_1": str(pair["image_1"]),
                "image_2": str(pair["image_2"]),
                "hamming_distance": int(
                    pair["hamming_distance"]
                ),
                "near_duplicate": True,
            }
        )

    with open(
        output_path,
        "w",
        encoding="utf-8",
    ) as file:

        json.dump(
            report,
            file,
            indent=4,
            default=int,
        )