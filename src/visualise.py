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
