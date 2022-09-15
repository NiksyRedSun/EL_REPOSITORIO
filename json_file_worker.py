import json
from person import Person
from generic_json_encoder import GenericEncoder
from typing import Dict

''' Описывает как преобразовать данные в файл и обратно '''


def to_json(data, fileName: str) -> None:
    with open(fileName, 'w') as file:
        json.dump(data, file, cls=GenericEncoder)


def from_json(fileName: str) -> Dict[str, Person]:
    try:
        with open(fileName, 'r') as file:
            fileValues: Dict[str, dict] = json.load(file)
            personValues = list(
                map(lambda x: Person(**x), fileValues.values()))
            return {person.name: person for person in personValues}
    except Exception:
        return {}
