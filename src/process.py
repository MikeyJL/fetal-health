"""Data processing.

Requires: pandas.
"""

import pandas as pd
from tui import print_heading


def preview_raw():
    """Generates a head preview of the dataset."""

    raw_df = pd.read_csv("data/raw/fetal_health.csv")

    print_heading("Features")
    print(", ".join(list(raw_df)))

    print_heading("Summary")
    print(raw_df.head())


def get_cols(features=None, as_df=False):
    """Gets the specified columns or returns the entire dataFrame.

    Args:
        features (list[str], optional): A list of features to pull from the raw dataframe. Defaults to None.
        in_row (bool, optional): To return as a row. Defaults to True.

    Returns:
        Tuple[ndarray[float]]: A tuple of features with its respective values.
        Dataframe: A pandas dataframe with selected features.
    """

    raw_df = pd.read_csv("data/raw/fetal_health.csv")

    if as_df:
        return raw_df[features or list(raw_df)]

    return tuple(raw_df[feature].values for feature in features or list(raw_df))
