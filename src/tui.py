"""Lets the user input values and shows menus."""

# pylint: disable="anomalous-backslash-in-string"
TITLE = """
  _____    _        _   _   _            _ _   _     
 |  ___|__| |_ __ _| | | | | | ___  __ _| | |_| |__  
 | |_ / _ \ __/ _` | | | |_| |/ _ \/ _` | | __| '_ \ 
 |  _|  __/ || (_| | | |  _  |  __/ (_| | | |_| | | |
 |_|  \___|\__\__,_|_| |_| |_|\___|\__,_|_|\__|_| k|_|
"""
# pylint: enable="anomalous-backslash-in-string"

MAIN_MENU_OPTIONS = [
    "Show group baseline value historgram subplot",
    "Show individual group baseline value histogram",
]


def print_title():
    """Prints the Fetal Health title."""

    print(TITLE)


def print_main_menu():
    """Prints the main menu."""

    print("-------- Main Menu --------")
    print(
        "\n".join(
            [
                f"[{index + 1}] {option}"
                for index, option in enumerate(MAIN_MENU_OPTIONS)
            ]
        )
    )
    print("")
