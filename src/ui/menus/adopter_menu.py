from datetime import date
import questionary
from rich.console import Console

from src.adopter import Adopter

from src.application import Application
from src.donation import Donation
from src.shelter import Shelter
from src.ui.lister import Lister

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
                "func": self.show_applications,
                "args": []},

            "Donate to a Shelter": {
                "func": self.donate,
                "args": []}
        })

        self.add_menu("Social Feed", SocialMenu(user, console), [])
        self.add_menu("System Items", ListingMenu(user, console), [])

    def donate(self):
        self.console.print()
        shelters = [f"{shelter}" for shelter in Shelter.data.values()]

        self.console.print()
        name: str = questionary.select("Which shelter do you want to donate to?",
                                       choices=shelters).ask()
        name = name.split(" - ")[0][1:]

        ammount: str = questionary.text("How much to you want to donate?",
                                        validate=lambda text: True if float(text) > 0 else "Ammount must be positive").ask()

        d = Donation(self.user.username, name, float(ammount), date.today())

        self.console.print(f"\nDonation registered!\n >{d}")

        questionary.press_any_key_to_continue().ask()

    def show_applications(self):
        apps: list[Application] = Application.get_apps_applicant(
            self.user.username)

        self.console.print()
        Lister(f"{self.user.name}'s Adoption Applications",
               apps, self.console).detailed_list()
