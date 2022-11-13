from flask import Flask, request
import json
import random
import psycopg2
import psycopg2.extras
from psycopg2 import pool

app = Flask(__name__)

names = ['John', 'Jack', 'Bill', 'Sady', 'Chavier', 'Charles', 'Arthur', 'Leopold', 'Sean', 'Caren']

connections_pool = psycopg2.pool.SimpleConnectionPool(1, 100,
                                                        host='localhost',  # метод connect() создает подключение к экземпляру базы данных PSQL
                                                        port=5432,
                                                        user='postgres',
                                                        dbname='postgres')

# connection.autocommit = True    # важно, нужно для того чтобы все что мы делаем сразу отражалось в БД


def CheckInputs(inputs, requires):
    for param in requires:
            if param not in inputs:
                return (json.dumps({'status': 'data_error', 'message': f'{param} expected'}), 400)
    return 'passed'

@app.route('/')
def start_page():
    return 'You are welcome at SLOVNIK'

@app.route('/users')
def show_users_profile():
    connection = connections_pool.getconn()
    with connection:
        cursor = connection.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
        cursor.execute(f"SELECT * FROM person")
        rows = cursor.fetchall()
        return json.dumps(rows)


@app.route('/user/<id>')
def show_user_profile(id):
    connection = connections_pool.getconn()
    with connection:
        cursor = connection.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
        cursor.execute(f"SELECT * FROM person WHERE id = {id}")
        rows = cursor.fetchall()
        if rows:
            return json.dumps(rows)
        else:
            return 'We have a search problem with this id'


@app.route('/user/<id>', methods=['DELETE'])
def delete_user_profile(id):
    connection = connections_pool.getconn()
    with connection:
        cursor = connection.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
        cursor.execute(f"SELECT * FROM person WHERE id = {id}")
        rows = cursor.fetchall()
        if rows:
            cursor.execute(f"DELETE FROM person WHERE id = {id}")
            cursor.execute(f"SELECT * FROM person")
            return f'В общем-то он удален, но чтобы убедиться гляньте на содержимое таблицы: {json.dumps(cursor.fetchall())}'
        else:
            return 'We have a search problem with this id'


@app.route('/user/post', methods=['POST'])
def post_user_profile():
    connection = connections_pool.getconn()
    with connection:
        inputs = request.get_json()
        check = CheckInputs(inputs, ['name', 'age'])
        if check != 'passed':
            return check
        cursor = connection.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
        name = inputs['name']
        age = inputs['age']
        cursor.execute(f"INSERT INTO person(name, age) VALUES ('{name}', {age});")
        cursor.execute(f"SELECT * FROM person")
        return f"{name} успешно добавлен, но чтобы убедиться гляньте на содержимое таблицы: {json.dumps(cursor.fetchall())}"


@app.route('/postrandom', methods=['POST'])
def post_random_profile():
    connection = connections_pool.getconn()
    if len(names) > 0:
        with connection:
            inputs = request.get_json()
            check = CheckInputs(inputs, ['name', 'age'])
            if check != 'passed':
                return check
            cursor = connection.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
            name = random.choice(names)
            age = random.randint(16, 55)
            cursor.execute(f"INSERT INTO person(name, age) VALUES ('{name}', {age});")
            cursor.execute(f"SELECT * FROM person")
            return f"{name} успешно добавлен, но чтобы убедиться гляньте на содержимое таблицы: {json.dumps(cursor.fetchall())}"
    else:
        return 'There is no free nicknames left'


@app.route('/user/<id>', methods=['PUT'])
def put_user_profile(id):
    connection = connections_pool.getconn()
    with connection:
        inputs = request.get_json()
        check = CheckInputs(inputs, ['name', 'age'])
        if check != 'passed':
            return check
        cursor = connection.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
        query = f"SELECT * FROM person WHERE id = {id}"
        cursor.execute(query)
        rows = cursor.fetchall()
        if rows:
            name = inputs['name']
            age = inputs['age']
            cursor.execute(f"UPDATE person SET name = '{name}', age = {age} WHERE id = {id}")
            cursor.execute(f"SELECT * FROM person WHERE id = {id}")
            return f'В результате получилось: {json.dumps(cursor.fetchall())}'
        else:
            return 'You are trying to change unregistered person'


if __name__ == '__main__':
    app.run(debug = True)