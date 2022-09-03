from flask import Flask, request
from types import SimpleNamespace
import json
app = Flask(__name__)

class Person:                               #класс кстати может быть представлен как справочник
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def info(self):
        info = 'Hi, I\'m ' + (self.name).capitalize() + ' ' + 'and I\'m ' + str(self.age)
        return info

    def short_info(self):
        short_info = 'Name: ' + (self.name).capitalize() + ',' + ' ' + 'age: ' + str(self.age)
        return short_info

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
                                                #  with - ключевое слово. Позволяет не думать о закрытии файла, после записи данных (json.dump)
                                                # default - параметр, по умолчанию вызови то что описано в параметре (unknown_object - параметр)
with open('my.json', 'w') as file:
    data = json.dumps(slovnik, default = lambda unknown_object: unknown_object.__dict__)
    json.dump(data, file)                   # 'w' и 'r' аргументы для записи и чтения. dump - чисто для сериализации/ json.dump(data, file) - запиши дату в файл

with open('my.json', 'r') as file:              # __dict__ представление пользовательских полей экземпляра внутри справочника
    data = json.load(file)                                #считай в json файл
    data = json.loads(data)
    print(data)
    print(type(data))
    print(data[niksy.name])
    print(niksy.short_info())