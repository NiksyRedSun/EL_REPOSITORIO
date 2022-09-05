from flask import Flask, request
app = Flask(__name__)

class Person:
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
print(slovnik)
print(niksy.name)