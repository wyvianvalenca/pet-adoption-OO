from typing_extensions import override
from .question import Question


class Answer:
    def __init__(self, question: Question, user_option: str):
        self.question: Question = question
        self.user_option: str = user_option
        self.is_preferred: bool = self.user_option == self.question.preferred_answer

    @override
    def __str__(self) -> str:
        return f"> {self.question.name} | R: {self.user_option}"
