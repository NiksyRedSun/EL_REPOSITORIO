from dataclasses import dataclass
from psycopg2 import pool
import psycopg2.extras
import json
import psycopg2
import psycopg2.extras

connections_pool = psycopg2.pool.ThreadedConnectionPool(1, 100,
                                                        host='localhost',  # метод connect() создает подключение к экземпляру базы данных PSQL
                                                        port=5432,
                                                        user='postgres',
                                                        dbname='postgres')

@dataclass
class persons:
    def show_all_persons(self):
        connection = connections_pool.getconn()
        with connection:
            cursor = connection.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
            cursor.execute(f"SELECT * FROM person")
            rows = cursor.fetchall()
            return json.dumps(rows)

    def post_one_person(self, name, age):
        connection = connections_pool.getconn()
        with connection:
            cursor = connection.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
            cursor.execute(f"INSERT INTO person(name, age) VALUES (%s, %s);", (name, age))
            cursor.execute(f"SELECT * FROM person")
            return f"{name} успешно добавлен, но чтобы убедиться гляньте на содержимое таблицы: {json.dumps(cursor.fetchall())}"


class person(persons):
    def __init__(self, id):
        self.person_id = id

    def show_one_person(self):
        connection = connections_pool.getconn()
        with connection:
            cursor = connection.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
            cursor.execute(f"SELECT * FROM person WHERE id = %s", self.person_id)
            rows = cursor.fetchall()
            if rows:
                return json.dumps(rows)
            else:
                return 'We have a search problem with this id'

    def delete_one_person(self):
        connection = connections_pool.getconn()
        with connection:
            cursor = connection.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
            cursor.execute(f"SELECT * FROM person WHERE id = %s", self.person_id)
            rows = cursor.fetchall()
            if rows:
                cursor.execute(f"DELETE FROM person WHERE id = %s", self.person_id)
                cursor.execute(f"SELECT * FROM person")
                return f'В общем-то он удален, но чтобы убедиться гляньте на содержимое таблицы: {json.dumps(cursor.fetchall())}'
            else:
                return 'We have a search problem with this id'

    def change_person_profile(self, name, age):
        connection = connections_pool.getconn()
        with connection:
            cursor = connection.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
            cursor.execute(f"SELECT * FROM person WHERE id = {self.person_id};") #обратить внимание, не работает через отправку параметров кортежем
            rows = cursor.fetchall()
            if rows:
                cursor.execute(f"UPDATE person SET name = %s, age = %s WHERE id = %s;", (name, age, self.person_id))
                cursor.execute(f"SELECT * FROM person WHERE id = {self.person_id}")
                return f'В результате получилось: {json.dumps(cursor.fetchall())}'
            else:
                return 'You are trying to change unregistered person'








