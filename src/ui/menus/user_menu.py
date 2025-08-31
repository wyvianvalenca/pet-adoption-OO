import questionary
from rich.console import Console

from src.donation import Donation
from src.pet import Pet
from src.post import Post
from src.user import User
from src.shelter import Shelter

from src.ui.clean import clear_screen
from src.ui.lister import Lister
from src.ui.posts_ui import PostUI
from src.ui.profile_updater import ProfileUpdater
from src.ui.header import header


class UserMenu:
    def __init__(self, user: User, console: Console):
        self.loop: bool = True
        self.user: User = user
        self.console: Console = console
        self.profile_updater: ProfileUpdater = ProfileUpdater(user, console)
        self.social_feed: PostUI = PostUI(console, user)

        self.actions = {
            "Return to Welcome Page":
                {"func": self.go_back,
                 "args": []},

            "Update Profile":
                {"func": self.profile_updater.update_profile,
                 "args": []},

            "Show Shelters":
                {"func": Lister("shelters", Shelter.data.values(),
                                self.console).detailed_list,
                 "args": []},

            "Show Pets":
            {"func": Lister("pets", Pet.data.values(),
                            self.console).detailed_list,
                    "args": []},

            "Show Events": {"func": self.wip, "args": []},

            "Show My Donations":
                {"func": Lister(f"{user.username}'s donations",
                                Donation.by_user(self.user.username),
                                self.console).simple_list,
                 "args": []},

            "Show Social Field":
                {"func": self.social_feed.show_posts,
                 "args": [list(Post.data.values()), True]},

            "Add Forum Post":
                {"func": self.social_feed.add_post,
                 "args": ["forum"]},

            "Add Educational Post":
                {"func": self.social_feed.add_post,
                 "args": ["educational"]},

            "Add Succes Story Post":
                {"func": self.social_feed.add_post,
                 "args": ["success story"]}
        }

    def wip(self):
        self.console.print("We're still working on this one...")
        questionary.press_any_key_to_continue().ask()

    def go_back(self):
        self.loop = False

    def show_menu(self):
        while self.loop:

            clear_screen()
            self.console.print(header("MAIN MENU"))
            self.console.print()
            option = questionary.select("Choose an option:",
                                        choices=list(self.actions.keys())).ask()

            self.actions[option]['func'](*self.actions[option]['args'])
