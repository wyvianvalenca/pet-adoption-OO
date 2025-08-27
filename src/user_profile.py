from datetime import date
from dateutil import relativedelta
from typing_extensions import override

from .address import Address


class Profile:
    def __init__(self, name: str, birth: date | None = None,
                 address: Address | None = None,
                 desc: str | None = None):
        self.__name: str = name
        self.__birth: date | None = birth
        self.__address: Address | None = address
        self.__description: str | None = desc

    @property
    def name(self) -> str:
        return self.__name.title()

    # TODO: add properties and setters with data validation

    def as_list(self) -> list[str]:
        info: list[str] = [self.__name]

        if self.__birth:
            info.append(self.__birth.isoformat())

        if self.__address:
            info.append(self.__address.__str__())

        if self.__description:
            info.append(self.__description)

        return info

    def formatted_list(self) -> list[str]:
        profile_info: list[str] = [f"{self.__name.upper()}"]

        if self.__birth:
            today = date.today()
            age: int = relativedelta.relativedelta(today, self.__birth).years
            profile_info.append(f"    > [bold]Age:[/] {age}")

        if self.__address:
            profile_info.append(f"    > [bold]Address:[/] {self.__address}")

        if self.__description:
            profile_info.append(
                f"    > [bold]Description:[/] {self.__description}")

        return profile_info

    @override
    def __str__(self) -> str:
        return f"{self.__name.title()}'s profile"
