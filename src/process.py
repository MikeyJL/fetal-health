"""Data processing.

Requires: pandas.
"""

import pandas as pd


def preview_raw():
    """Generates a head preview of the dataset."""

    raw_df = pd.read_csv("data/raw/fetal_health.csv")

    print("\n===== Features =====\n")
    print(", ".join(list(raw_df)))

    print("\n===== Summary =====\n")
    print(raw_df.head())


def get_cols(features=None):
    """Gets the specified columns or returns the entire dataFrame.

    Args:
        features (List[string], optional): A list of features to pull from the raw dataframe. Defaults to None.

    Returns:
        DataFrame: The full or partial dataframe.
    """

    raw_df = pd.read_csv("data/raw/fetal_health.csv")

    if features:
        return raw_df[features]

    return raw_df
