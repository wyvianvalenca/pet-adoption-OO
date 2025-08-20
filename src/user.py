from datetime import date
from typing_extensions import override

from src.address import Address
from src.user_profile import Profile


class User:
    def __init__(self, username: str, name: str, birth: date,
                 address: Address, description: str):
        self.__username: str = username
        self.__profile: Profile = Profile(name, birth, address, description)
        self.allowed_post_types: list[str] = ["forum", "comment"]
        self.posts: list['Post'] = []

    @property
    def username(self) -> str:
        return self.__username

    @property
    def profile(self) -> list[str]:
        return self.__profile.as_list()

    def name(self) -> str:
        return self.__profile.name

    """TO-DO: add methods to update profile"""

    def formatted_profile(self) -> list[str]:
        return self.__profile.formatted_list()

    @override
    def __str__(self) -> str:
        """inside prints, show only the username"""

        return self.__username
