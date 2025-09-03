from typing import Any

import questionary


class Query:
    def __init__(self, items: list[dict[str, Any]]):
        self.items: list[dict[str, Any]] = items

    def get_options(self) -> dict[str, list[Any]]:
        """Gets all options"""

        options: dict[str, list[Any]] = {}

        for dictionary in self.items:
            for key, value in dictionary.items():
                if (value is not None and key != "name"):
                    try:
                        if value not in options[key]:
                            options[key].append(str(value))
                    except KeyError:
                        options[key] = [str(value)]

        return options

    def make_form(self) -> list[dict[str, str | list]]:
        options = self.get_options()
        criteria_dicts: list[dict[str, str | list]] = []

        for key, values in options.items():
            criteria_dicts.append({
                "type": "checkbox",
                "name": key,
                "message": f"Choose the {key}s you want to filter:",
                "choices": values
            })

        return criteria_dicts

    def get_user_criteria(self) -> dict[str, list[Any]]:
        criteria = questionary.prompt(self.make_form())
        return criteria

    def filter_items(self) -> list[str]:
        items: list[dict[str, Any]] = self.items.copy()

        user_criterias = self.get_user_criteria()

        for key, criterias in user_criterias.items():
            if len(criterias) > 0:
                for index, dictionary in enumerate(items):
                    if dictionary[key] not in criterias:
                        items.pop(index)

        return [dictionary['name'] for dictionary in items]
