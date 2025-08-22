from abc import ABC, abstractmethod
from typing_extensions import override

from src.user_profile import Profile


class User(ABC):
    def __init__(self, username: str):
        self.__username: str = username
        self.__profile: Profile
        self.allowed_post_types: list[str] = ["forum", "comment"]

    @property
    def username(self) -> str:
        return self.__username

    @property
    def profile(self) -> list[str]:
        return self.__profile.as_list()

    @property
    def name(self) -> str:
        return self.__profile.name

    # TODO: add methods to create and update profile

    @abstractmethod
    def login():
        pass

    @abstractmethod
    def formatted_profile(self) -> list[str]:
        pass

    @override
    def __str__(self) -> str:
        """inside prints, show only the username"""

        return self.__username
