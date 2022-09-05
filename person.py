from dataclasses import dataclass

@dataclass
class Person:
    name: str
    age:  int

    def info(self):
        info = 'Hi, I\'m ' + (self.name).capitalize() + ' ' + 'and I\'m ' + str(self.age)
        return info

    def short_info(self):
        short_info = 'Name: ' + (self.name).capitalize() + ',' + ' ' + 'age: ' + str(self.age)
        return short_info
