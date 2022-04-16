"""Data processing.

Requires: pandas.
"""

from os.path import exists

import dataframe_image as dfi
import pandas as pd
from pandas import DataFrame

from tui import print_heading
from visualise import FIGURE_DIR, PlotParams, plot_hist


def preview_raw() -> None:
    """Generates a head preview of the dataset."""

    raw_df: DataFrame = pd.read_csv("data/fetal_health.csv")

    print_heading("Features and Data Types")
    print(raw_df.dtypes)

    print_heading("Null Count")
    print(raw_df.isnull().sum())

    print_heading("Unique Value Count")
    print(raw_df.nunique())

    print_heading("Summary")
    print(raw_df.head())


def distribution_subplots() -> None:
    """Creates a subplot of distributions and saves the figure.

    Pulls out the fetal health and creates subgroups of historgrams.
    """

    df: DataFrame = pd.read_csv("data/fetal_health.csv")

    filename: str = "features-stats"

    if filename is not None:
        figure_exists: bool = exists(f"{FIGURE_DIR}{filename}")

        if not figure_exists:
            dfi.export(
                df.drop(columns=["fetal_health"], axis=1).describe(),
                f"{FIGURE_DIR}{filename}.png",
            )

    for column in df.drop(columns=["fetal_health"], axis=1).columns:
        X = [
            df[df["fetal_health"] == 1][column].values,
            df[df["fetal_health"] == 2][column].values,
            df[df["fetal_health"] == 3][column].values,
        ]

        data = PlotParams(
            title=f"Histogram distribution of {column.replace('_', ' ')}",
            x_label=f"{column.replace('_', ' ').capitalize()}",
            y_label="Frequency",
            x_values=X,
            desc=df[[column]].describe(),
            show=False,
        )
        plot_hist(
            data,
            f"{column.replace('_', '-')}",
        )
