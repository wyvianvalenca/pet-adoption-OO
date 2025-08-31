import questionary
from rich.console import Console

from src.shelter import Shelter
from src.ui.name_validator import NameValidator

from src.ui.menus.menu import Menu
from src.ui.menus.pet_menu import PetMenu
from src.ui.menus.social_menu import SocialMenu
from src.ui.menus.listing_menu import ListingMenu


class ShelterMenu(Menu):
    def __init__(self, user: Shelter, console: Console):
        Menu.__init__(self, user, console)
        self.name = "shelter menu"

        self.actions.update({
            "Add Pet Type": {
                "func": self.add_pet_type,
                "args": []},

            "Create Event": {
                "func": self.wip,
                "args": []}
        })

        self.add_menu("Manage Pets", PetMenu(user, console), [])
        self.add_menu("Social Feed", SocialMenu(user, console), [])
        self.add_menu("List System Items", ListingMenu(user, console), [])

    def add_pet_type(self):
        pet_type: str = questionary.text("Type a pet type:",
                                         validate=NameValidator,
                                         qmark=">>").ask()

        self.user.add_allowed_pet_type(pet_type)
