"""Visualises the data."""

from os.path import exists
import logging as log
import matplotlib.pyplot as plt
from _typing import AxisValues

log.basicConfig(level=log.INFO, format="[%(levelname)s] %(message)s")

FIGURE_DIR = "reports/figures/"


def plot_scatter(x_values: AxisValues, y_values: AxisValues) -> None:
    """Generates a scatter plot with given data.

    Args:
        x (AxisValues): Data along the x-axis.
        y (AxisValues): Data along the y-axis.
    """

    plt.scatter(x_values, y_values)
    plt.show()


def plot_hist(x_values: list[AxisValues], filename: str = None) -> None:
    """Generates histogram(s) from given values.

    Optionally can save it to the reports/figures directory.

    Args:
        x_values (list[AxisValues]): A matrix of values.
        filename (str, optional): The name of the figure. Defaults to None.
    """

    fig, axs = plt.subplots(1, len(x_values), figsize=(12, 9))
    for index, x in enumerate(x_values):
        axs[index].hist(x)
    fig.suptitle("Histogram plot")

    if filename is not None:
        figure_exists = exists(f"{FIGURE_DIR}{filename}")

        if not figure_exists:
            plt.savefig(f"{FIGURE_DIR}{filename}")

        log.info(
            "Figure saved to reports/figures"
            if not figure_exists
            else "Figure already exists."
        )

    plt.show()
