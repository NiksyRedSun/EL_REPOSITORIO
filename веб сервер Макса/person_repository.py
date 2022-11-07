''' Repository Описывает CRUD операции над Person'ами '''

from json_file_worker import from_json, to_json
import os
from dotenv import load_dotenv
from typing import Dict
from person import Person

# Получить справочник переменных окружения
load_dotenv()

# Получить переменную из файла настроек окружения
JSON_FILE_PATH = os.getenv('json_file_path')


# Стартовое состояние
current_state = from_json(JSON_FILE_PATH)


def get_all() -> Dict[str, Person]:
    return current_state


def get_by_key(key: str) -> Person or None:
    return current_state.get(key, None)


def delete_by_key(key: str) -> None:
    del current_state[key]
    _override_state(current_state)


def add_user(user_name: str, user_age: int) -> None:
    if (user_name in current_state):
        raise KeyError('Already exists such person')
    person = Person(user_name, user_age)
    _set_person(person)


def update_user(user_name: str, user_age: int) -> None:
    if (user_name not in current_state):
        raise KeyError('There is no such person')
    person = Person(user_name, user_age)
    _set_person(person)


# Это "приватные" функции (начинаются с _) - они не будут видны вне этого файла
def _set_person(person: Person) -> None:
    current_state[person.name] = person
    _override_state(current_state)


def _override_state(next_state: Dict[str, Person]) -> None:
    to_json(next_state, JSON_FILE_PATH)
