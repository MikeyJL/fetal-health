"""Main runtime."""


from explore import preview_raw, distribution_subplots
from tui import print_title, print_menu, get_option
from model import eval_features, svm_train


def explore_options() -> None:
    """Handles explore submenu selection."""

    print_menu(menu_type="Explore")
    explore_option: int = get_option()
    if explore_option == 1:
        preview_raw()
    elif explore_option == 2:
        distribution_subplots()
    elif explore_option == 3:
        pass


def model_options() -> None:
    """Handles model submenu selection."""

    print_menu(menu_type="Model")
    model_option: int = get_option()
    if model_option == 1:
        eval_features()
    elif model_option == 2:
        svm_train()
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
