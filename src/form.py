from src.question import Question


class Form:
    all: list['Form'] = []

    def __init__(self, questions: list[Question] = []):
        self.__questions: list[Question] = questions
        self.all.append(self)

    def add_question(self, name: str, options: list[str], right: str):
        if name in [q.name for q in self.__questions]:
            raise ValueError(f"question '{name}' already exists")

        self.__questions.append(Question(name, options, right))

    def __len__(self) -> int:
        return len(self.__questions)

    def __getitem__(self, index: int) -> Question:
        return self.__questions[index]

    def __delitem__(self, index: int) -> None:
        del self.__questions[index]
        return None

    def __iter__(self):
        return iter(self.__questions)

    def __str__(self) -> str:
        return f"Adoption Application Form with {len(self)} questions"

    def formatted_list(self) -> list[str]:
        form: list[str] = ["Adoption Application Form", ""]

        for q in self.__questions:
            form.extend(q.formatted_list())
            form.append("")

        return form
