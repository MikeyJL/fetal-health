"""Visualises the data."""

import matplotlib.pyplot as plt


def plot_scatter(x_values, y_values):
    """Generates a scatter plot with given data.

    Args:
        x (ndarray[float]): Data along the x-axis.
        y (ndarray[float]): Data along the y-axis.
    """

    plt.scatter(x_values, y_values)
    plt.show()


def plot_hist(x_values):
    """Generates histogram(s) from given values.

    Args:
        x_values (list[list[float]]): A matrix of values.
    """

    fig, axs = plt.subplots(1, len(x_values), figsize=(12, 9))
    for index, x in enumerate(x_values):
        axs[index].hist(x)
    fig.suptitle("Histogram plot")
    plt.show()
