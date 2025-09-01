import questionary
from rich.console import Console

from src.event import Event
from src.user import User

from src.ui.name_validator import NameValidator
from src.ui.lister import Lister
from src.ui.menus.menu import Menu


class EventMenu(Menu):
    def __init__(self, user: User, console: Console):
        Menu.__init__(self, user, console)
        self.name = "event management"

        self.actions = {
            "Return to User Menu": {
                "func": self.go_back,
                "args": []},

            "View Shelter's Events": {
                "func": self.show_events,
                "args": []},

            "Cancel Event": {
                "func": self.cancel_event,
                "args": []},

            "Complete Event": {
                "func": self.complete_event,
                "args": []}
        }

    def get_event_name(self) -> Event | None:
        self.console.print()
        name: str = questionary.text("Type the event's name:",
                                     validate=NameValidator,
                                     qmark=">>").ask()

        if Event.__contains__(name):
            return Event.data[name]

        self.console.print("\nEvent not found.")
        questionary.press_any_key_to_continue().ask()
        return None

    def cancel_event(self):
        event = self.get_event_name()

        if event is None:
            return

        event.cancel()
        self.console.log(f"\n{event.name} cancelled.\n")

        questionary.press_any_key_to_continue().ask()

    def complete_event(self):
        event = self.get_event_name()

        if event is None:
            return

        event.complete()
        self.console.log(f"\n{event.name} completed.\n")

        questionary.press_any_key_to_continue().ask()

    def show_events(self):
        events = Event.by_shelter(self.user.username)
        Lister(f"{self.user.name}'s events",
               events, self.console).detailed_list()
