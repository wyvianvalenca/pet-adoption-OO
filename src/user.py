from datetime import date

from src.address import Address
from src.user_profile import Profile


class User:
    def __init__(self, username: str, name: str, birth: date,
                 address: Address, description: str):
        self.username: str = username
        self.profile: Profile = Profile(name, birth, address, description)
        self.allowed_post_types: list[str] = ["forum", "comment"]
        self.posts: list['Post'] = []
