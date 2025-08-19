from datetime import date
from typing_extensions import override

from .address import Address


class Profile:
    def __init__(self, name: str, birth: date, address: Address,
                 description: str):
        self.name: str = name
        self.birth: date = birth
        self.address: Address = address
        self.description: str = description

    def as_list(self) -> list[str]:
        profile_info: list[str] = [f"{self.name.upper()}",
                                   f"    > {self.birth.isoformat()}",
                                   f"    > {self.address}",
                                   f"    > {self.description}"]
        return profile_info

    @override
    def __str__(self) -> str:
        return f"{self.name.title()}'s profile"
