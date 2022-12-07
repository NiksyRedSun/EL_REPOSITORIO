from dataclasses import dataclass
from psycopg2 import pool
import psycopg2.extras
import json
import psycopg2
import psycopg2.extras
from dotenv import load_dotenv
import os
from person_exceptions import PersonException


load_dotenv()

connections_pool = psycopg2.pool.ThreadedConnectionPool(
    1,
    100,
    host=os.getenv("host"),
    port=os.getenv("port"),
    user=os.getenv("user"),
    dbname=os.getenv("dbname"))


@dataclass
class person_repository:
    def __guard_is_not_empty(self, person):
        if person is None:
            raise ValueError('There was no any person')

    def get(self, person=None):
        connection = connections_pool.getconn()
        with connection:
            cursor = connection.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
            if person is not None:
                cursor.execute(f"SELECT * FROM person WHERE id = {person.id}")
                rows = cursor.fetchone()
                if rows:
                    return json.dumps(rows)
                else:
                    raise PersonException(f'Person with id {person.id} not found')
            else:
                cursor.execute("SELECT * FROM person")
                rows = cursor.fetchall()
                return json.dumps(rows)


    def delete(self, person):
        self.__guard_is_not_empty(person)
        connection = connections_pool.getconn()
        with connection:
            cursor = connection.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
            cursor.execute(f"SELECT * FROM person WHERE id = {person.id}")
            rows = cursor.fetchone()
            if rows:
                cursor.execute(f"DELETE FROM person WHERE id = {person.id}")
                return json.dumps({'success':True, 'code':200})
            else:
                raise PersonException(f'Person with id {person.id} not found')


    def create(self, person):
        self.__guard_is_not_empty(person)
        connection = connections_pool.getconn()
        with connection:
            cursor = connection.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
            cursor.execute("INSERT INTO person(name, age) VALUES (%s, %s);", (person.name, person.age))
            cursor.execute("SELECT MAX(id) AS current_id FROM person")
            return json.dumps(cursor.fetchone())


    def update(self, person):
        self.__guard_is_not_empty(person)
        connection = connections_pool.getconn()
        with connection:
            cursor = connection.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
            cursor.execute(f"SELECT * FROM person WHERE id = {person.id};")
            rows = cursor.fetchone()
            if rows:
                cursor.execute("UPDATE person SET name = %s, age = %s WHERE id = %s;", (person.name, person.age, person.id))
                return json.dumps({'success':True, 'code':200})
            else:
                raise PersonException(f'Person with id {person.id} not found')