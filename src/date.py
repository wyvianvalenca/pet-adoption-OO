class Date:
    def __init__(self, day: int, month: int, year: int) -> None:
        self._day: int = day
        self._month: int = month
        self._year: int = year

    @property
    def day(self) -> int:
        return self.day

    @property
    def month(self) -> int:
        return self.month

    @property
    def year(self) -> int:
        return self.year

    def formatted(self) -> str:
        return f"{self.day}-{self.month}-{self.year}"
