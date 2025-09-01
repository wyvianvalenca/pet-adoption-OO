from rich.console import Console

from src.event import Event
from src.user import User
from src.shelter import Shelter
from src.donation import Donation

from src.ui.menus.menu import Menu
from src.ui.lister import Lister
from src.pet import Pet


class ListingMenu(Menu):
    def __init__(self, user: User, console: Console):
        Menu.__init__(self, user, console)

        self.name = "listing menu"

        self.actions = {
            "Return to User Menu":
                {"func": self.go_back,
                 "args": []},

            "Show Shelters":
                {"func": Lister("shelters", Shelter.data.values(),
                                self.console).detailed_list,
                 "args": []},

            "Show Pets":
                {"func": Lister("pets", Pet.data.values(),
                                self.console).detailed_list,
                 "args": []},

            "Show Events":
                {"func": Lister("events", Event.data.values(),
                                self.console).detailed_list,
                 "args": []},

            "Show My Donations":
                {"func": Lister(f"{user.username}'s donations",
                                Donation.by_user(self.user.username),
                                self.console).simple_list,
                 "args": []},
        }
