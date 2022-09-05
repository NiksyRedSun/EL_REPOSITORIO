import json
from json import JSONEncoder

class Person:
    def __init__(self, name, age, *args, **kwargs):
        self.name = name
        self.age = age

    
niksy = Person('niksy', 25)
andrew = Person('andrew', 25)
zheka = Person('zheka', 25)
ilya = Person('ilya', 25)

slovnik = {
    niksy.name:niksy,
    andrew.name:andrew,
    zheka.name:zheka,
    ilya.name:ilya,
}

with open('my.json', 'w') as file:
    data = json.dumps(slovnik, default= lambda unknown_object:unknown_object.__dict__)
    json.dump(data, file)

with open('my.json', 'r') as file:
    data = json.load(file) # получили JSON (это справочник людей в виде JSON)
    value = json.loads(data) # получили честный справочник людей. Люди пока что тоже справочники
    new_niksy = value[niksy.name]  # получили конкретного человека. new_niksy - это все еще справочник
    person = Person(**new_niksy) # передаем справчочник в конструктор особым образом, ничего добавлять не надо - это опять же реализовано за нас
    print(person.age) # получаем пользователя
    print(andrew.age)