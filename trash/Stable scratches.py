# load / dump и dumps/loads - обратные действия
# dict - представление пользовательских полей экземпляра в виде справочника
with open('my.json', 'w') as file:
    # data = json.dumps(slovnik, default=  lambda o: o.dict)
    #по умолчанию если не можешь представить в виде JSON -- default
    # ЛЮБОЙ ТАКОЙ ОБЪЕКТ - labmda + имя переменной
    data = json.dumps(slovnik, default= lambda unknown_object:unknown_object.dict)
    json.dump(data, file)