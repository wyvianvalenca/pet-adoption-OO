from datetime import date
from typing_extensions import override

from .address import Address


class Profile:
    def __init__(self, name: str, birth: date, address: Address,
                 description: str):
        self.__name: str = name
        self.__birth: date = birth
        self.__address: Address = address
        self.__description: str = description

    @property
    def name(self) -> str:
        return self.__name.title()

    # TODO: add properties and setters with data validation

    def as_list(self) -> list[str]:
        return [self.__name, self.__birth.isoformat(),
                self.__address.__str__(), self.__description]

    def formatted_list(self) -> list[str]:
        profile_info: list[str] = [f"{self.__name.upper()}",
                                   f"    > Description: {self.__description}",
                                   f"    > Idade: {self.__birth.today()}",
                                   f"    > Addres: {self.__address}"]
        return profile_info

    @override
    def __str__(self) -> str:
        return f"{self.__name.title()}'s profile"
