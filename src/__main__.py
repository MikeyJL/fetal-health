"""Main runtime."""

from process import preview_raw, get_cols
from visualise import plot_hist
from tui import print_title, print_menu, get_option


def baseline_subplots() -> None:
    """Creates a subplot and saves the figure.

    Pulls out the fetal health and creates subgroups of historgrams.
    """

    df = get_cols(["baseline value", "fetal_health"], as_df=True)
    print(f"\n{df.describe()}\n")

    X = [
        df[df["fetal_health"] == 1]["baseline value"].values,
        df[df["fetal_health"] == 2]["baseline value"].values,
        df[df["fetal_health"] == 3]["baseline value"].values,
    ]
    plot_hist(X, "baseline-hist-subplot.png")


def explore_options() -> None:
    """Handles explore submenu selection."""

    print_menu(menu_type="Explore")
    explore_option = get_option()
    if explore_option == 1:
        baseline_subplots()
    elif explore_option == 2:
        pass
    elif explore_option == 3:
        pass


if __name__ == "__main__":
    print_title()
    while True:
        print_menu()
        option = get_option()
        if option == 1:
            preview_raw()
        elif option == 2:
            explore_options()
        elif option == 3:
            break
