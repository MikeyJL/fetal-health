"""Main runtime."""

from process import preview_raw, get_cols
from visualise import plot_hist
from tui import print_title, print_main_menu, get_option


def baseline_subplots():
    """Creates a subplot and saves the figure.

    Pulls out the fetal health and creates subgroups of historgrams.
    """

    df = get_cols(["baseline value", "fetal_health"], as_df=True)
    X = [
        df[df["fetal_health"] == 1]["baseline value"].values,
        df[df["fetal_health"] == 2]["baseline value"].values,
        df[df["fetal_health"] == 3]["baseline value"].values,
    ]
    plot_hist(X, "baseline-hist-subplot.png")


if __name__ == "__main__":
    print_title()
    while True:
        print_main_menu()
        option = get_option()
        if option == 1:
            preview_raw()
        elif option == 2:
            baseline_subplots()
        elif option == 3:
            pass
        elif option == 4:
            break
