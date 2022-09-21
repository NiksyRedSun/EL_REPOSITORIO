from dataclasses import dataclass
''' Модель человека в системе '''
@dataclass
class Person:
    name: str
    age:  int

    # Всегда когда будет приводиться Person к строке будет вызываться эта перегрузка
    def __repl__(self) -> str:
        return f"Person {self.name}, with age {self.age}"
