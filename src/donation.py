from datetime import date
from typing_extensions import override

from src.model import Model


class Donation(Model):
    @classmethod
    def by_donor(cls, donor: str) -> list['Donation']:
        return [don for don in cls.data.values() if don.__donor == donor]

    @classmethod
    def by_receiver(cls, receiver: str) -> list['Donation']:
        return [don for don in cls.data.values() if don.__receiver == receiver]

    @classmethod
    def by_user(cls, user: str) -> list['Donation']:
        return [don for don in cls.data.values() if don.__receiver == user or don.__donor == user]

    def __init__(self, donor: str, receiver: str, ammount: float,
                 donation_date: date):
        self.__donor: str = donor
        self.__receiver: str = receiver
        self.__ammount: float = ammount
        self.__donation_date: date = donation_date

        self.data[f"{donor}-{receiver}-{donation_date.isoformat()}"] = self

    @property
    def donor(self) -> str:
        return self.__donor

    @property
    def receiver(self) -> str:
        return self.__receiver

    @property
    def ammount(self) -> float:
        return self.__ammount

    @property
    def date(self) -> str:
        return self.__donation_date.isoformat()

    @override
    def __str__(self) -> str:
        return f"@{self.__donor} has donated US$ {self.__ammount:.2f} to @{self.__receiver}"

    @override
    def formatted_list(self) -> list[str]:
        return [self.__str__()]

    # overloading comparison operators
    def __gt__(self, other):
        if isinstance(other, Donation):
            return self.ammount > other.ammount
        return NotImplemented

    def __lt__(self, other):
        if isinstance(other, Donation):
            return self.ammount < other.ammount
        return NotImplemented
