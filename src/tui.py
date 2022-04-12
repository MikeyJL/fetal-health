"""Lets the user input values and shows menus."""

import logging as log
from _typing import Menu

log.basicConfig(level=log.INFO, format="[%(levelname)s] %(message)s")

# pylint: disable="anomalous-backslash-in-string"
TITLE: str = """
  _____    _        _   _   _            _ _   _     
 |  ___|__| |_ __ _| | | | | | ___  __ _| | |_| |__  
 | |_ / _ \ __/ _` | | | |_| |/ _ \/ _` | | __| '_ \ 
 |  _|  __/ || (_| | | |  _  |  __/ (_| | | |_| | | |
 |_|  \___|\__\__,_|_| |_| |_|\___|\__,_|_|\__|_| k|_|
"""
# pylint: enable="anomalous-backslash-in-string"

MAIN_MENU_OPTIONS: Menu = [
    "Explore dataset",
    "Make prediction",
    "Exit",
]

DATA_EXPLORATION_MENU: Menu = [
    "Dataset overview",
    "Show group baseline value historgram subplot",
    "Show individual group baseline value histogram",
    "Back to Main Menu",
]


def print_title() -> None:
    """Prints the Fetal Health title."""

    print(TITLE)


def print_heading(heading: str) -> None:
    """Prints the heading with seperator."""

    print(f"\n========== {heading} ==========\n")


def __get_menu(menu_type: str) -> Menu:
    """Gets the menu array.

    Args:
        menu_type (str): The menu to return.

    Returns:
        list[str]: The menu selected.
    """

    if menu_type == "Main":
        return MAIN_MENU_OPTIONS
    return DATA_EXPLORATION_MENU


def print_menu(menu_type: str = "Main") -> None:
    """Prints the selected menu."""

    print(f"\n-------- {menu_type} Menu --------")
    print(
        "\n".join(
            [
                f"[{index + 1}] {option}"
                for index, option in enumerate(__get_menu(menu_type))
            ]
        )
    )


def get_option(msg: str = "Please select an option") -> int:
    """Prompts the user for an option and validates it.

    Args:
        msg (str, optional): Shows an input message. Defaults to "Please select an option".

    Returns:
        int: The validated input option.
    """

    value: int | None = None
    while value is None:
        try:
            value = int(input(f"\n{msg}\n>>> "))
        except ValueError as e:
            log.error(e)

    return value
