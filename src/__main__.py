"""Main runtime."""

from process import preview_raw, get_cols
from visualise import PlotParams, plot_hist
from tui import print_title, print_menu, get_option
from model import eval_features, mlp_classify
from _typing import GetColsValue, AxisValues


def selected_features_subplots() -> None:
    """Creates a subplot and saves the figure.

    Pulls out the fetal health and creates subgroups of historgrams.
    """

    df: GetColsValue = get_cols(
        [
            "accelerations",
            "prolongued_decelerations",
            "abnormal_short_term_variability",
            "histogram_mean",
            "fetal_health",
        ],
        as_df=True,
    )
    print(f"\n{df.describe()}\n")

    for column in df.drop(columns=["fetal_health"], axis=1).columns:
        X: list[AxisValues] = [
            df[df["fetal_health"] == 1][column].values,
            df[df["fetal_health"] == 2][column].values,
            df[df["fetal_health"] == 3][column].values,
        ]

        data = PlotParams(
            title=f"Histogram distribution of {column.replace('_', ' ')}",
            x_label=f"{column.replace('_', ' ').capitalize()}",
            y_label="Frequency",
            x_values=X,
        )
        plot_hist(data, f"{column.replace('_', '-')}-hist-subplot.png")


def explore_options() -> None:
    """Handles explore submenu selection."""

    print_menu(menu_type="Explore")
    explore_option: int = get_option()
    if explore_option == 1:
        preview_raw()
    elif explore_option == 2:
        selected_features_subplots()
    elif explore_option == 3:
        pass


def model_options() -> None:
    """Handles model submenu selection."""

    print_menu(menu_type="Model")
    model_option: int = get_option()
    if model_option == 1:
        eval_features()
    elif model_option == 2:
        mlp_classify()
    elif model_option == 3:
        pass


if __name__ == "__main__":
    print_title()
    while True:
        print_menu()
        option: int = get_option()
        if option == 1:
            explore_options()
        if option == 2:
            model_options()
        elif option == 3:
            break
