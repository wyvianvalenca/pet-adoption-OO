from ctypes import Union
import os

import questionary

from rich.align import Align
from rich.console import Console
from rich.panel import Panel
from rich.prompt import Prompt

import initial_info

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


def welcome() -> Adopter | Shelter | None:
    while True:
        clear_screen()

        console.print(WELCOME_PANEL)

        user_type: str = questionary.select("Choose your role!",
                                            choices=["Adopter", "Shelter"]).ask()

        if not user_type:
            console.print("Goodbye!")
            return None

        print()

        user_access: str = questionary.select("How do you want to access PetApp?",
                                              choices=["Login", "Sign Up"]).ask()

        if user_access == "Login":
            user = login(user_type)
        elif user_access == "Sign Up":
            user = sign_up(user_type)
        else:
            continue

        if user:
            return user


def sign_up(user_type: str) -> Adopter | Shelter:
    while True:
        username: str = questionary.text("Choose an username: ").ask()

        if user_type == "Adopter":
            if Adopter.username_available(username):
                first_name: str = questionary.text(
                    "What's your first name?").ask()
                last_name: str = questionary.text(
                    "What's your last name?").ask()
                name: str = first_name.title() + last_name.title()
                return Adopter(username, name)

        elif user_type == "Shelter":
            if Shelter.username_available(username):
                name: str = questionary.text(
                    "What's the shelter's name?").ask()
                return Shelter(username, name)

        console.print("Username taken.\n", style="red")


def login(user_type: str) -> Adopter | Shelter | None:
    username: str = questionary.text("Type your username: ").ask()

    if user_type == "Adopter":
        if not Adopter.username_available(username):
            return Adopter.login(username)
    elif user_type == "Shelter":
        if not Shelter.username_available(username):
            return Shelter.login(username)

    console.print("User not found.\n")
    questionary.press_any_key_to_continue().ask()
    return None


def main():
    user = welcome()
    if not user:
        return

    print(user)


if __name__ == "__main__":
    initial_info.create_users()

    main()
