import json
import psycopg2
import psycopg2.extras


def get_all():
    cursor = connection.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
    query = f"SELECT * FROM person"
    cursor.execute(query)
    rows = cursor.fetchall()
    print(json.dumps(rows))


def get_one():
    cursor = connection.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
    id = int(input('Впишите id, который вас интересует: '))
    query = f"SELECT * FROM person WHERE id = {id}"
    cursor.execute(query)
    rows = cursor.fetchall()
    print(json.dumps(rows))


def post():
    cursor = connection.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
    name = str(input('Имя: '))
    age = int(input('Возраст: '))
    query = f"INSERT INTO person(name, age) VALUES ('{name}', {age});"
    cursor.execute(query)
    query = f"SELECT * FROM person"
    cursor.execute(query)
    rows = cursor.fetchall()
    print(f'{name} успешно оказался в той самой таблице')
    print(json.dumps(rows))


def put():
    cursor = connection.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
    id = int(input('Впишите id, который вас интересует: '))
    query = f"SELECT * FROM person WHERE id = {id}"
    cursor.execute(query)
    print(json.dumps(cursor.fetchall()))
    name = str(input('Новое имя? '))
    age = int(input('Новый возраст? '))
    query = f"UPDATE person SET name = '{name}', age = {age} WHERE id = {id}"
    cursor.execute(query)
    query = f"SELECT * FROM person WHERE id = {id}"
    cursor.execute(query)
    print('В результате получилось: ')
    print(json.dumps(cursor.fetchall()))


def delete():
    cursor = connection.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
    id = int(input('Впишите id, который подлежит удалению: '))
    query = f"DELETE FROM person WHERE id = {id}"
    cursor.execute(query)
    print('В общем-то он удален, но чтобы убедиться гляньте на содержимое таблицы:')
    cursor.execute(f"SELECT * FROM person")
    print(json.dumps(cursor.fetchall()))


connection = psycopg2.connect(host='localhost',  # метод connect() создает подключение к экземпляру базы данных PSQL
                                  port=5432,
                                  user='postgres',
                                  dbname='postgres')
connection.autocommit = True
command = str(input('Задайте команду на выбор (GET_ONE, GET_ALL, POST, PUT, DELETE): '))

with connection:
    if command == 'GET_ALL': get_all()
    if command == 'GET_ONE': get_one()
    if command == 'POST': post()
    if command == 'PUT': put()
    if command == 'DELETE': delete()