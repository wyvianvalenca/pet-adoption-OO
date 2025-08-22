from .user import User


class Adopter(User):
    all: dict[str, 'Adopter'] = {}

    @classmethod
    def login(cls, username: str) -> 'Adopter':
        return cls.all[username]

    def __init__(self, username: str):
        if username in self.all:
            raise Exception("username taken")

        User.__init__(self, username)
        self.__pets: list[str] = []
        self.all[username] = self

    def formatted_profile(self) -> list[str]:
        return self.__profile.formatted_list()
