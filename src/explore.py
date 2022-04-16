"""Data processing.

Requires: pandas.
"""

from os.path import exists

import dataframe_image as dfi
import pandas as pd
from pandas import DataFrame
from scipy.stats import shapiro

from tui import print_heading
from visualise import FIGURE_DIR, PlotParams, plot_hist


def preview_raw() -> None:
    """Generates a head preview of the dataset."""

    df: DataFrame = pd.read_csv("data/fetal_health.csv")

    print_heading("Features and Data Types")
    print(df.dtypes)

    print_heading("Null Count")
    print(df.isnull().sum())

    print_heading("Unique Value Count")
    print(df.nunique())

    print_heading("Summary")
    print(df.head())

    # Saves overall as an image if not exist already
    filename: str = "dataset-statistics"
    if filename is not None:
        figure_exists: bool = exists(f"{FIGURE_DIR}{filename}")

        if not figure_exists:
            dfi.export(
                df.drop(columns=["fetal_health"], axis=1).describe(),
                f"{FIGURE_DIR}{filename}.png",
            )


def distribution_subplots() -> None:
    """Creates a subplot of distributions and saves the figure.

    Pulls out the fetal health and creates subgroups of historgrams.
    """

    df: DataFrame = pd.read_csv("data/fetal_health.csv")

    for column in df.drop(columns=["fetal_health"], axis=1)[["baseline value"]].columns:
        # Subsets in to 3 fetal health categories for each column
        X = [
            df[df["fetal_health"] == 1][column].values,
            df[df["fetal_health"] == 2][column].values,
            df[df["fetal_health"] == 3][column].values,
        ]

        # Statistical analysis with test for normality
        normality = shapiro(df[column].values)
        df_describe = df[[column]].describe()
        df_describe = pd.concat(
            [
                df_describe,
                pd.DataFrame(
                    [[normality.statistic, normality.pvalue]],
                    columns=[column],
                    index=pd.Index(["shapiro-statistic", "shapiro-p"]),
                ),
            ]
        )

        # Sets up plotting data for histogram
        data = PlotParams(
            title=f"Histogram distribution of {column.replace('_', ' ')}",
            x_label=f"{column.replace('_', ' ').capitalize()}",
            y_label="Frequency",
            x_values=X,
            desc=df_describe,
            show=False,
        )
        plot_hist(
            data,
            filename=f"{column.replace('_', '-')}",
        )
