from typing_extensions import override
from .user import User


class Shelter(User):
    all: dict[str, 'Shelter'] = {}

    @classmethod
    def username_available(cls, username: str) -> bool:
        if username in cls.all.keys():
            return False

        return True

    @override
    @classmethod
    def login(cls, username: str) -> 'Shelter':
        return cls.all[username]

    def __init__(self, username: str, name: str):
        User.__init__(self, username, name)
        self.__allowed_pet_types: list[str] = []
        # self.__pets: list[Pet] = []
        # self.__events: list[Event] = []

        self.all[username] = self

    @property
    def allowed_pet_types(self) -> str:
        return ", ".join(self.__allowed_pet_types)

    def add_allowed_pet_type(self, pet_type: str) -> None:
        if len(pet_type) == 0:
            raise ValueError("pet type can't be empty")

        self.__allowed_pet_types.append(pet_type)
        return None

    def is_allowed(self, pet_type: str) -> bool:
        return pet_type in self.__allowed_pet_types

    def formatted_profile(self) -> list[str]:
        shelter_info: list[str] = self.__profile.formatted_list()
        shelter_info.append(
            f"    > [bold]Allowed[/] pets: {self.allowed_pet_types}")
        return shelter_info
