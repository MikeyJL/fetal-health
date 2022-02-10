"""Data processing.

Requires: pandas.
"""

import pandas as pd


def preview_raw() -> None:
    """Generates a head preview of the dataset."""

    print(pd.read_csv("data/raw/fetal_health.csv").head())
