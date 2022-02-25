"""Main runtime."""

# from process import preview_raw, get_cols
# from visualise import plot_hist
from tui import print_title, print_main_menu, get_option

if __name__ == "__main__":
    print_title()
    print_main_menu()

    get_option()

    # preview_raw()
    # df = get_cols(["baseline value", "fetal_health"], as_df=True)

    # X = [
    #     df[df["fetal_health"] == 1]["baseline value"].values,
    #     df[df["fetal_health"] == 2]["baseline value"].values,
    #     df[df["fetal_health"] == 3]["baseline value"].values,
    # ]

    # plot_hist(X)
