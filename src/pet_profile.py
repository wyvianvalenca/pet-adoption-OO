from datetime import date
from typing_extensions import override

from src.address import Address
from src.user_profile import Profile


class PetProfile(Profile):
    def __init__(self, name: str,
                 birth: date | None = None,
                 address: Address | None = None,
                 description: str | None = None,
                 breed: str | None = None,
                 color: str | None = None):
        Profile.__init__(self, name, birth, address, description)
        self.breed: str | None = breed
        self.color: str | None = color

    @override
    def as_list(self) -> list[str]:
        info: list[str] = Profile.as_list(self)

        if self.breed:
            info.append(self.breed)

        if self.color:
            info.append(self.color)

        return info

    @override
    def formatted_list(self) -> list[str]:
        profile_info: list[str] = Profile.formatted_list(self)

        if self.breed:
            profile_info.append(f"    > [bold]Breed:[/] {self.breed}")

        if self.color:
            profile_info.append(f"    > [bold]Color:[/] {self.color}")

        return profile_info
