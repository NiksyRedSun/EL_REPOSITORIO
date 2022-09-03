import json
from json import JSONEncoder

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

with open('my.json', 'r') as file:
    data = json.load(file)
    value = json.loads(data)
    user = 'niksy'
    user = Person(value[str(user)]['name'], value[str(user)]['age'])
    print(type(user))




