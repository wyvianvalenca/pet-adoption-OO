import questionary
from rich.console import Console

from src.ui.profile_updater import ProfileUpdater
from src.user import User
from src.pet import Pet

from src.ui.name_validator import NameValidator
from src.ui.lister import Lister
from src.ui.menus.menu import Menu


class PetMenu(Menu):
    def __init__(self, user: User, console: Console):
        Menu.__init__(self, user, console)
        self.name = "pet menu"

        self.updater: ProfileUpdater = ProfileUpdater(user, console)

        self.actions = {
            "Return to User Menu": {
                "func": self.go_back,
                "args": []},

            "View Shelter's Pets": {
                "func": self.show_pets,
                "args": []},

            "Register New Pet": {
                "func": self.create_pet,
                "args": []},

            "Update Pet Profile": {
                "func": self.update_pet_profile,
                "args": []},

            "Add Question to Pet's Form": {
                "func": self.wip,
                "args": []},

            "View Pet's Adoption Applications": {
                "func": self.wip,
                "args": []},

        }

    def show_pets(self):
        pets = Pet.by_shelter(self.user.username)
        Lister(f"{self.user.name}'s pets",
               pets,
               self.console).detailed_list()

    def get_pet_name(self) -> Pet | None:
        name: str = questionary.text("Type the pet's name:",
                                     validate=NameValidator,
                                     qmark=">>").ask()

        if Pet.__contains__(name):
            return Pet.data[name]

        return None

    def update_pet_profile(self):
        pet: Pet | None = self.get_pet_name()

        if pet is None:
            return

        self.updater.update_updater(pet)
        self.updater.update_profile()

    def create_pet(self):
        name: str = questionary.text("Type the pet's name:",
                                     validate=NameValidator,
                                     qmark=">>").ask()

        pet_type: str = questionary.text("Type the pet's type (species):",
                                         validate=NameValidator,
                                         qmark=">>").ask()

        if not self.user.is_allowed(pet_type):
            self.console.print(
                f"{self.user.name} does not shelters {pet_type}")
            return

        new_pet: Pet = Pet(name, self.user.username, pet_type)

        update: bool = questionary.confirm(
            f"Do you want to update {name}'s profile?").ask()

        if update:
            self.updater.update_updater(new_pet)
            self.updater.update_profile()
