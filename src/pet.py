from datetime import date

from src.application import Application
from src.form import Form
from src.pet_profile import PetProfile
from src.question import Question
from src.address import Address
from src.adopter import Adopter


class Pet:
    all: dict[str, 'Pet'] = {}

    def __init__(self, name: str, pet_type: str,
                 birth: date | None = None,
                 address: Address | None = None,
                 desc: str | None = None,
                 breed: str | None = None,
                 color: str | None = None):

        self.__pet_type: str = pet_type
        self.__profile: PetProfile = PetProfile(name, birth, address,
                                                desc, breed, color)
        self.__status: str = "rescued"
        self.__form: Form = Form(
            [Question(
                f"Are you sure you want to adopt {name}?",
                ["Yes", "No"],
                "Yes")])

        self.__applications: list[Application] = []
        self.__tutor: Adopter | None = None

        self.all[name] = self

    def start_treatment(self) -> None:
        self.__status = "in treatment"
        return None

    def start_adoption(self) -> None:
        self.__status = "available for adoption"
        return None

    def add_template_question(self, question: str,
                              options: list[str],
                              answer: str) -> None:

        self.__form.add_question(question, options, answer)
        return None

    def apply_adoption(self, applicant: str, answers: list[str]) -> None:
        new_app: Application = Application(
            applicant, self.__profile.name, self.__form, answers)
        self.__applications.append(new_app)
