import questionary
from rich.console import Console

from src.adopter import Adopter

from src.ui.menus.menu import Menu
from src.ui.menus.social_menu import SocialMenu
from src.ui.menus.listing_menu import ListingMenu


class AdopterMenu(Menu):
    def __init__(self, user: Adopter, console: Console):
        Menu.__init__(self, user, console)
        self.name = "adopter menu"

        self.actions.update({
            "Filter Pets": {
                "func": self.wip,
                "args": []},

            "Apply to Adopt a Pet": {
                "func": self.wip,
                "args": []},

            "View Adoption Applications": {
                "func": self.wip,
                "args": []}
        })

        self.add_menu("Social Feed", SocialMenu(user, console), [])
        self.add_menu("System Items", ListingMenu(user, console), [])
