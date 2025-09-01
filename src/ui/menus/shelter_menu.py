from datetime import date
import questionary
from rich.console import Console

from src.event import Event
from src.shelter import Shelter

from src.ui.address_creator import create_address
from src.ui.date_creator import create_date
from src.ui.name_validator import NameValidator

from src.ui.menus.menu import Menu
from src.ui.menus.event_menu import EventMenu
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
                "args": []}
        })

        self.add_menu("Manage Events", EventMenu(user, console), [])
        self.add_menu("Manage Pets", PetMenu(user, console), [])
        self.add_menu("Social Feed", SocialMenu(user, console), [])
        self.add_menu("List System Items", ListingMenu(user, console), [])

    def add_pet_type(self):
        pet_type: str = questionary.text("Type a pet type:",
                                         validate=NameValidator,
                                         qmark=">>").ask()

        self.user.add_allowed_pet_type(pet_type)

    def create_event(self):
        self.console.print()
        name: str = questionary.text("Type the event's name:",
                                     validate=NameValidator,
                                     qmark=">>").ask()

        self.console.print()
        address = create_address()
        if address is False:
            return

        self.console.print()
        event_date = create_date()
        if event_date is False:
            return

        event = Event(name, event_date, address, self.user.username)

        self.console.print("\nEvent created!")
        self.console.print(f"  > {event}\n")

        questionary.press_any_key_to_continue().ask()
