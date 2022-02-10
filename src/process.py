"""Data processing.

Requires: pandas.
"""

import pandas as pd


def preview_raw() -> None:
    """Generates a head preview of the dataset."""

    raw_df = pd.read_csv("data/raw/fetal_health.csv")

    print("\n===== Features =====\n")
    print(", ".join(list(raw_df)))

    print("\n===== Summary =====\n")
    print(raw_df.head())
