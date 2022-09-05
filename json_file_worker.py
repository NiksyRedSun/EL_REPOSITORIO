import json
from person import Person

def saving(slovnik):
    with open('my.json', 'w') as file:
        data = json.dumps(slovnik, default= lambda unknown_object:unknown_object.__dict__)
        json.dump(data, file)

def loading():
    with open('my.json', 'r') as file:
        data = json.load(file)
        value = json.loads(data)
        slovnik = {}
        for user_key in value:
            current_person = Person(value[user_key]['name'], value[user_key]['age'])
            slovnik[user_key] = current_person
    return slovnik















