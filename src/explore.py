"""Data processing.

Requires: pandas.
"""

from os.path import exists

import dataframe_image as dfi
import pandas as pd
from pandas import DataFrame
from scipy.stats import shapiro, f_oneway, kruskal

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
        normality_row = pd.DataFrame(
            [[normality.statistic], [normality.pvalue]],
            columns=[column],
            index=pd.Index(["shapiro-statistic", "shapiro-p"]),
        )

        df_describe = pd.concat([df_describe, normality_row])

        # Parametric test
        if normality.pvalue > 0.05:
            anova = f_oneway(X[0], X[1], X[2])
            anova_row = pd.DataFrame(
                [[anova.statistic], [anova.pvalue]],
                columns=[column],
                index=pd.Index(["anova-statistic", "anova-p"]),
            )
            df_describe = pd.concat([df_describe, anova_row])

        # Non-parametric test
        else:
            k_wallis = kruskal(X[0], X[1], X[2])
            k_wallis_row = pd.DataFrame(
                [[k_wallis.statistic], [k_wallis.pvalue]],
                columns=[column],
                index=pd.Index(["k-wallis-statistic", "k-wallis-p"]),
            )
            df_describe = pd.concat([df_describe, k_wallis_row])

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
