"""Visualises the data."""

from dataclasses import dataclass
from os import mkdir
from os.path import exists
import logging as log
from typing import Any

from pandas import DataFrame
import matplotlib.pyplot as plt
import dataframe_image as dfi
from matplotlib.pyplot import Figure, Axes

log.basicConfig(level=log.INFO, format="[%(levelname)s] %(message)s")

FIGURE_DIR = "figures/"


@dataclass
class PlotParams:
    """Generic plot parameters for visualisation."""

    # pylint: disable=too-many-arguments
    def __init__(
        self,
        title: str,
        x_label: str,
        y_label: str,
        x_values: Any,
        y_values: Any | None = None,
        desc: DataFrame | None = None,
    ) -> None:
        self.title: str = title
        self.x_label: str = x_label
        self.y_label: str = y_label
        self.x_values: Any = x_values
        self.y_values: Any | None = y_values
        self.desc: DataFrame | None = desc


def plot_hist(data: PlotParams, filename: str | None = None) -> None:
    """Generates histogram(s) from given values.

    Optionally can save it to the figures directory.

    Args:
        data (PlotParams): Data for the plot.
        filename (str, optional): The name of the figure. Defaults to None.
    """

    fig: Figure
    axs: Axes
    index: int

    fig, axs = plt.subplots(1, len(data.x_values), figsize=(12, 9))
    for index, x in enumerate(data.x_values):
        axs[index].hist(x)
    fig.suptitle(data.title)
    fig.supxlabel(data.x_label)
    fig.supylabel(data.y_label)

    if filename is not None:
        try:
            mkdir(f"{FIGURE_DIR}{filename}")
            log.info("%s directory created.", filename)
        except OSError as e:
            log.error(e)
            log.info("%s directory already exists.", filename)

        figure_exists: bool = exists(f"{FIGURE_DIR}{filename}/${filename}.png")
        stats_exists: bool = exists(f"{FIGURE_DIR}{filename}/${filename}-stats.png")

        if not figure_exists:
            plt.savefig(f"{FIGURE_DIR}{filename}/{filename}.png")

        if not stats_exists and data.desc is not None:
            dfi.export(data.desc, f"{FIGURE_DIR}{filename}/{filename}-stats.png")

        log.info(
            "%s saved to figures" if not figure_exists else "%s already exists.",
            filename.replace("_", " ").capitalize(),
        )
        log.info(
            "%s stats saved to figures"
            if not stats_exists
            else "%s stats already exists.",
            filename.replace("_", " ").capitalize(),
        )

    plt.show()


def simple_plot(
    data: PlotParams,
    filename: str | None = None,
) -> None:
    """Creates a simple line plot.

    Args:
        data (PlotParams): Data for the plot.
        filename (str, optional): The name of the figure. Defaults to None.
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
