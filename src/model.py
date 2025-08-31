from abc import ABC, abstractmethod
from typing_extensions import Self


class Model(ABC):
    def __init_subclass__(cls):
        cls.data: dict[str, Self] = {}
        return super().__init_subclass__()

    @abstractmethod
    def formatted_list(self) -> list[str]:
        """returns all info in a formated list"""
        pass
