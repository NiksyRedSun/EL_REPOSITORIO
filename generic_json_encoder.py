from json import JSONEncoder

''' Описывает как преобразовать любой объект в справочник '''

class GenericEncoder(JSONEncoder):
    def default(self, o):
        return o.__dict__ 