from typing_extensions import override


class Address:
    def __init__(self, street: str, district: str, number: str,
                 postal_code: int, city: str, state: str):
        self.street: str = street
        self.district: str = district
        self.number: str = number
        self.postal_code: int = postal_code
        self.city: str = city
        self.state: str = state

    @override
    def __str__(self) -> str:
        return (f"{self.street}, {self.number}, {self.district} - "
                + f"{self.city}/{self.state.upper()}")
