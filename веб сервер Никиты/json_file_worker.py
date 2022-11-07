import json
from json import JSONEncoder
from person import Person

class AnyClassEncoder():
    def default(self, obj):
        return obj.dict

def saving(slovnik):
    with open('my.json', 'w') as file:
        json.dump(slovnik, file, cls=AnyClassEncoder)

def loading():
    with open('my.json', 'r') as file:
        data = json.load(file)
        value = json.loads(data)
        slovnik = {}
        for user_key in value:
            current_person = Person(value[user_key]['name'], value[user_key]['age'])
            slovnik[user_key] = current_person
    return slovnik















