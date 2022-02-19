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
        features (List[str], optional): A list of features to pull from the raw dataframe. Defaults to None.

    Returns:
        Tuple[ndarray[float]]: A tuple of features with its respective values.
    """

    raw_df = pd.read_csv("data/raw/fetal_health.csv")

    if features:
        return tuple(raw_df[feature].values for feature in features)

    return tuple(raw_df[feature].values for feature in list(raw_df))
