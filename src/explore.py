"""Exploration options and logic."""

import logging as log
from os.path import exists
from pathlib import Path

import dataframe_image as dfi
import pandas as pd
from pandas import DataFrame
from scipy.stats import shapiro, f_oneway, kruskal, kurtosis

from tui import print_heading
from visualise import FIGURE_DIR, PlotParams, box_plot, plot_hist, show_correlation

log.basicConfig(level=log.INFO, format="[%(levelname)s] %(message)s")
PROCESSED_DATA_DIR = "data/processed/"


def save_csv(data: DataFrame, filename: str) -> None:
    """Saves DataFrame as a CSV file.

    Args:
        data (DataFrame): DataFrame to save.
        filename (str): The name of the file.
    """

    # Check if the csv already exists
    data_exists: bool = exists(f"{PROCESSED_DATA_DIR}{filename}.csv")

    # Saves the csv if not already exists
    if not data_exists:
        filepath = Path(f"{PROCESSED_DATA_DIR}{filename}.csv")
        data.to_csv(filepath)


def preview_raw() -> None:
    """Generates a head preview of the dataset."""

    df: DataFrame = pd.read_csv("data/raw/fetal_health.csv")

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

    show_correlation(df)


def distribution_subplots() -> None:
    """Creates a subplot of distributions and saves the figure.

    Pulls out the fetal health and creates subgroups of historgrams.
    """

    df: DataFrame = pd.read_csv("data/raw/fetal_health.csv")

    for column in df.drop(columns=["fetal_health"], axis=1).columns:
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

        # Kurtosis
        kurt = kurtosis(df[column].values)
        kurt_row = pd.DataFrame(
            [kurt],
            columns=[column],
            index=pd.Index(["kurtosis"]),
        )
        df_describe = pd.concat([df_describe, kurt_row])

        # Saves statistical data to csv
        save_csv(df_describe, filename=column.replace("_", "-").replace(" ", "-"))

        # Sets up plotting data for boxplot.
        data = PlotParams(
            title=f"Distribution of {column.replace('_', ' ')}",
            y_label=f"{column.replace('_', ' ').capitalize()}",
            x_values=[df[column].values],
            show=False,
        )
        box_plot(
            data,
            filename=column.replace("_", "-").replace(" ", "-"),
        )

        # Sets up plotting data for group boxplot.
        data = PlotParams(
            title=f"Fetal health group distribution of {column.replace('_', ' ')}",
            x_labels=["Normal", "Suspect", "Pathological"],
            y_label=f"{column.replace('_', ' ').capitalize()}",
            x_values=X,
            show=False,
        )
        box_plot(
            data,
            filename=column.replace("_", "-").replace(" ", "-"),
        )

        # Sets up plotting data for histogram
        data = PlotParams(
            title=f"Distribution of {column.replace('_', ' ')}",
            x_label=f"{column.replace('_', ' ').capitalize()}",
            y_label="Frequency",
            x_values=[df[column].values],
            show=False,
        )
        plot_hist(
            data,
            filename=column.replace("_", "-").replace(" ", "-"),
        )

        # Sets up plotting data for histogram subplots for fetal_health
        data = PlotParams(
            title=f"Fetal health group distribution of {column.replace('_', ' ')}",
            x_label=f"{column.replace('_', ' ').capitalize()}",
            x_labels=["Normal", "Suspect", "Pathological"],
            y_label="Frequency",
            x_values=X,
            desc=df_describe,
            show=False,
        )
        plot_hist(
            data,
            filename=column.replace("_", "-").replace(" ", "-"),
        )
