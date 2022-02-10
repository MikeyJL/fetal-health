"""Main runtime."""

from process import preview_raw, get_cols
from visualise import plot_scatter

if __name__ == "__main__":
    preview_raw()

    acc, base = get_cols(["histogram_mean", "baseline value"])

    plot_scatter(acc, base)
