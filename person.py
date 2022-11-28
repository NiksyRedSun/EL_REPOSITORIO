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


@dataclass()
class Person:
    id: int = None
    name: str = None
    age:  int = None


@dataclass
class person_repository:


    def show(self, person=None):
        connection = connections_pool.getconn()
        with connection:
            cursor = connection.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
            if person is not None:
                cursor.execute(f"SELECT * FROM person WHERE id = {person.id}")
                rows = cursor.fetchall()
                if rows:
                    return json.dumps(rows)
                else:
                    return 'We have a search problem with this id'
            else:
                cursor.execute("SELECT * FROM person")
                rows = cursor.fetchall()
                return json.dumps(rows)


    def delete(self, person):
        if person is None: raise ValueError('There was no any person')
        connection = connections_pool.getconn()
        with connection:
            cursor = connection.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
            cursor.execute(f"SELECT * FROM person WHERE id = {person.id}")
            rows = cursor.fetchall()
            if rows:
                cursor.execute(f"DELETE FROM person WHERE id = {person.id}")
                cursor.execute(f"SELECT * FROM person")
                return f'This person was deleted but you can see a table : {json.dumps(cursor.fetchall())}'
            else:
                return 'We have a search problem with this id'


    def create(self, person):
        if person is None: raise ValueError('There was no any person')
        connection = connections_pool.getconn()
        with connection:
            cursor = connection.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
            cursor.execute(f"INSERT INTO person(name, age) VALUES (%s, %s);", (person.name, person.age))
            cursor.execute(f"SELECT * FROM person")
            return f"{person.name} added successfully but you can see a table : {json.dumps(cursor.fetchall())}"


    def update(self, person):
        if person is None: raise ValueError('There was no any person')
        connection = connections_pool.getconn()
        with connection:
            cursor = connection.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
            cursor.execute(f"SELECT * FROM person WHERE id = {person.id};")
            rows = cursor.fetchall()
            if rows:
                cursor.execute(f"UPDATE person SET name = %s, age = %s WHERE id = %s;", (person.name, person.age, person.id))
                cursor.execute(f"SELECT * FROM person WHERE id = {person.id}")
                return f'We have a result: {json.dumps(cursor.fetchall())}'
            else:
                return 'You are trying to change unregistered person'








