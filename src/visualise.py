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


# pylint: disable=too-many-instance-attributes
@dataclass
class PlotParams:
    """Generic plot parameters for visualisation."""

    # pylint: disable=too-many-arguments
    def __init__(
        self,
        title: str,
        x_values: Any,
        y_values: Any | None = None,
        x_label: str | None = None,
        y_label: str | None = None,
        x_labels: list[str] | None = None,
        desc: DataFrame | None = None,
        show: bool = False,
    ) -> None:
        self.title: str = title
        self.x_values: Any = x_values
        self.y_values: Any | None = y_values
        self.x_label: str | None = x_label
        self.y_label: str | None = y_label
        self.x_labels: list[str] | None = x_labels
        self.desc: DataFrame | None = desc
        self.show: bool = show


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

    # Prepares subplots
    fig, axs = plt.subplots(1, len(data.x_values), figsize=(12, 9))

    # For each subset, plot on its own axis
    for index, x in enumerate(data.x_values):
        if len(data.x_values) > 1:
            axs[index].hist(x)
        else:
            axs.hist(x)

        # Add subplot labels
        if data.x_labels is not None:
            axs[index].set_xlabel(data.x_labels[index])

    # Main figure titles and labels
    fig.suptitle(data.title)
    if data.x_label is not None:
        fig.supxlabel(data.x_label)
    if data.y_label is not None:
        fig.supylabel(data.y_label)

    # Save file logic
    if filename is not None:

        # Check if the column specific directory exists
        try:
            mkdir(f"{FIGURE_DIR}{filename}")
            log.info("%s directory created.", filename)
        except OSError as e:
            log.info("%s directory already exists.", filename)
            log.error(e)

        # Check if figure and stats images already exists
        figure_exists: bool = exists(
            f"{FIGURE_DIR}{filename}/{filename}-hist{'-subplot' if len(data.x_values) > 1 else ''}.png"
        )
        stats_exists: bool = exists(f"{FIGURE_DIR}{filename}/{filename}-stats.png")

        # Saves the figure if not already exists
        if not figure_exists:
            plt.savefig(
                f"{FIGURE_DIR}{filename}/{filename}-hist{'-subplot' if len(data.x_values) > 1 else ''}.png"
            )

        # Saves the stats table if not already exists
        if not stats_exists and data.desc is not None:
            dfi.export(data.desc, f"{FIGURE_DIR}{filename}/{filename}-stats.png")

    # Shows plot if specified
    if data.show:
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

    # Prepares plot
    fig, ax = plt.subplots(1, 1, figsize=(12, 9))

    # Sets figure title and labels
    fig.suptitle(data.title)
    if data.x_label is not None:
        ax.set_xlabel(data.x_label)
    if data.y_label is not None:
        ax.set_ylabel(data.y_label)

    plt.plot(data.x_values, data.y_values)

    # Save file logic
    if filename is not None:
        figure_exists: bool = exists(f"{FIGURE_DIR}{filename}")

        # Saves the figure if not already exists
        if not figure_exists:
            plt.savefig(f"{FIGURE_DIR}{filename}")

    # Shows plot if specified
    if data.show:
        plt.show()


def box_plot(
    data: PlotParams,
    filename: str | None = None,
) -> None:
    """Creates a box plot.

    Args:
        data (PlotParams): Data for the plot.
        filename (str, optional): The name of the figure. Defaults to None.
    """

    fig: Figure
    ax: Axes

    # Prepares plot
    fig, ax = plt.subplots(1, 1, figsize=(12, 9))

    # Sets figure title and labels
    fig.suptitle(data.title)
    ax.set_ylabel(data.y_label)
    ax.yaxis.grid(True)
    if data.x_labels is not None:
        ax.set_xticks([i + 1 for i in range(len(data.x_labels))], labels=data.x_labels)

    plt.boxplot(data.x_values)

    # Save file logic
    if filename is not None:

        # Check if the column specific directory exists
        try:
            mkdir(f"{FIGURE_DIR}{filename}")
            log.info("%s directory created.", filename)
        except OSError as e:
            log.info("%s directory already exists.", filename)
            log.error(e)

        # Checks if the figure exists
        figure_exists: bool = exists(
            f"{FIGURE_DIR}{filename}/{filename}-boxplot{'-group' if len(data.x_values) > 1 else ''}"
        )

        # Saves the figure if not already exists
        if not figure_exists:
            plt.savefig(
                f"{FIGURE_DIR}{filename}/{filename}-boxplot{'-group' if len(data.x_values) > 1 else ''}"
            )

    # Shows plot if specified
    if data.show:
        plt.show()
