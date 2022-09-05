from dataclasses import dataclass
import json
from dataclasses import dataclass

@dataclass
class Person:
    name: str
    age:  int


a = Person(1, 's')
with open('my.json', 'r') as file:
    data = json.load(file)
    value = json.loads(data)
    slovnik = {}
    for user_name in value:
        user_as_dict: dict = value[user_name]
        new_person = Person(name = user_as_dict['name'],  age = user_as_dict['age'])
        slovnik[new_person.name] = new_person
    print(slovnik)
    for i in slovnik:
        print(i)












