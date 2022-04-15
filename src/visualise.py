"""Visualises the data."""

from dataclasses import dataclass
from os.path import exists
import logging as log
from typing import Any
import matplotlib.pyplot as plt
from matplotlib.pyplot import Figure, Axes
from _typing import AxisValues

log.basicConfig(level=log.INFO, format="[%(levelname)s] %(message)s")

FIGURE_DIR = "figures/"


@dataclass
class PlotParams:
    """Generic plot parameters for visualisation."""

    # pylint: disable=too-many-arguments
    def __init__(
        self, x_values: Any, y_values: Any, title: str, x_label: str, y_label: str
    ) -> None:
        self.x_values: Any = x_values
        self.y_values: Any = y_values
        self.title: str = title
        self.x_label: str = x_label
        self.y_label: str = y_label


def plot_hist(x_values: list[AxisValues], filename: str | None = None) -> None:
    """Generates histogram(s) from given values.

    Optionally can save it to the figures directory.

    Args:
        x_values (list[AxisValues]): A matrix of values.
        filename (str, optional): The name of the figure. Defaults to None.
    """

    fig: Figure
    axs: Axes
    index: int
    x: AxisValues

    fig, axs = plt.subplots(1, len(x_values), figsize=(12, 9))
    for index, x in enumerate(x_values):
        axs[index].hist(x)
    fig.suptitle("Histogram plot")

    if filename is not None:
        figure_exists: bool = exists(f"{FIGURE_DIR}{filename}")

        if not figure_exists:
            plt.savefig(f"{FIGURE_DIR}{filename}")

        log.info(
            "Figure saved to figures" if not figure_exists else "Figure already exists."
        )

    plt.show()


def simple_plot(
    data: PlotParams,
    filename: str | None = None,
) -> None:
    """Creates a simple line plot.

    Args:
        data (PlotParams): Data for the plot.
        filename (str): Save the file as specified name.
    """

    fig: Figure
    ax: Axes

    fig, ax = plt.subplots(1, 1, figsize=(12, 9))
    fig.suptitle(data.title)
    ax.set_xlabel(data.x_label)
    ax.set_ylabel(data.y_label)
    plt.plot(data.x_values, data.y_values)

    if filename is not None:
        figure_exists: bool = exists(f"{FIGURE_DIR}{filename}")

        if not figure_exists:
            plt.savefig(f"{FIGURE_DIR}{filename}")

        log.info(
            "Figure saved to figures" if not figure_exists else "Figure already exists."
        )

    plt.show()
