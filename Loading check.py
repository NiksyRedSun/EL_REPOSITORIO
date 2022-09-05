import json
from json import JSONEncoder

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def short_info(self):
        short_info = 'Name: ' + (self.name).capitalize() + ',' + ' ' + 'age: ' + str(self.age)
        return short_info

with open('my.json', 'r') as file:
    data = json.load(file)
    value = json.loads(data)
    slovnik = {}
    for user in value:
        locals()[user] = Person(value[user]['name'], value[user]['age'])
        slovnik[locals()[user].name] = locals()[user]
    print(slovnik)
    print(niksy.name, niksy.age)
    print(zheka.name, zheka.age)
    print(str(niksy.short_info()))
    for i in slovnik:
        print(i)












