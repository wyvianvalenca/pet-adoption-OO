class Question:
    def __init__(self, name: str, options: list[str], preferred_answer: str):
        self.name: str = name
        self.options: list[str] = options
        self.preferred_answer: str = preferred_answer

    def as_list(self) -> list[str]:
        question_info: list[str] = [f"> {self.name}"]
        question_info.extend([f"    - {option}" for option in self.options])

        return question_info
