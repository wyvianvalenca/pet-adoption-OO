import os

from rich.align import Align
from rich.console import Console
from rich.panel import Panel
from rich.prompt import Prompt

from src.adopter import Adopter
from src.shelter import Shelter
from src.user import User

console = Console()

ASCII_ART: str = """
    Art by Joan Stark
          ,_     _,       _     /)---(\\            /~~~\\
          |\\\___//|       \\\   (/ . . \\)          /  .. \\
          |=6   6=|        \\\__)-\\(.)/           (_,\\  |_)
          \\=._Y_.=/        \\_       (_           /   \\@/     /^^^\\
           )  `  (    ,    (___/-(____)   _     /      \\    / . . \\
          /       \\  ((                   \\\   /  `    |    V\\ Y /V
          |       |   ))     WELCOME TO    \\\/  \\   | _\\     / - \\
         /| |   | |\\_//    Pet Adoption!    \\   /__'|| \\\_   |    \\
    jgs  \\| |._.| |/-`                       \\_____)|_).\\_). ||(__v
          '"'   '"'
"""

WELCOME_PANEL: Panel = Panel(Align.center(ASCII_ART),
                             title="Pet Adoption App", style="violet")


def clear_screen():
    # Check the operating system
    if os.name == 'nt':  # For Windows
        _ = os.system('cls')
    else:  # For Linux, macOS, and other Unix-like systems
        _ = os.system('clear')


def welcome(message: str) -> str:
    console.print(WELCOME_PANEL)

    user_type: str = Prompt.ask("\n How do you want to access the system?",
                                console=console,
                                choices=["Adopter", "Shelter"])
    clear_screen()
    return user_type


def login(user_type: str) -> User:
    console.print(WELCOME_PANEL)

    username: str = Prompt.ask("Username", console=console)
    while True:
        try:
            if user_type == "Adopter":
                return Adopter.login(username)
            else:
                return Shelter.login(username)
        except IndexError:
            console.print("User not found.")


if __name__ == "__main__":
    user_type = welcome(WELCOME_MESSAGE)
    user = login(user_type)
