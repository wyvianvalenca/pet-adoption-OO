from typing_extensions import override
from .user import User


class Adopter(User):
    all: dict[str, 'Adopter'] = {}

    @classmethod
    def username_available(cls, username: str) -> bool:
        if username in cls.all.keys():
            return False

        return True

    @override
    @classmethod
    def login(cls, username: str) -> 'Adopter':
        return cls.all[username]

    def __init__(self, username: str, name: str):
        User.__init__(self, username, name)
        self.__pets: list[str] = []
        self.all[username] = self

    def formatted_profile(self) -> list[str]:
        return self.__profile.formatted_list()
