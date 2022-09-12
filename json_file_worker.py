import json
from time import process_time_ns
from person import Person
from generic_json_encoder import GenericEncoder
from typing import Dict, List


def toJson(data, fileName) -> None:
    with open(fileName, 'w') as file:
        json.dump(data, file, cls=GenericEncoder)


def fromJson(fileName) -> Dict[str, Person]:
    with open(fileName, 'r') as file:
        fileValues: Dict[str, dict] = json.load(file)
        personValues = list(
            map(lambda x: Person(**x), fileValues.values()))
        return { person.name : person for person in personValues }

