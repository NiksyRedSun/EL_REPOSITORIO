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

connections_pool = pool.ThreadedConnectionPool(
    1,
    100,
    host=os.getenv("host"),
    port=os.getenv("port"),
    user=os.getenv("user"),
    dbname=os.getenv("dbname"))


def _execute_sql_with_no_return(sql_command: str, *args):
    try:
        connection = connections_pool.getconn()
        with connection:
            cursor = connection.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
            cursor.execute(sql_command, *args)
    except:
        raise PersonException('Не удалось выполнить запрос')


def _execute_sql_with_return(sql_command: str, *args):
    try:
        connection = connections_pool.getconn()
        with connection:
            cursor = connection.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
            cursor.execute(sql_command, *args)
            rows = cursor.fetchall()
            return rows
    except:
        raise PersonException('Не удалось выполнить запрос')


@dataclass
class person_repository:

    def __guard_is_not_empty(self, person):
        if person is None:
            raise ValueError('There was no any person')

    def get(self, person=None):
        if person is not None:
            sql_request = f"SELECT * FROM person WHERE id = {person.id}"
        else:
            sql_request = "SELECT * FROM person"
        rows = _execute_sql_with_return(sql_request)
        if rows:
            return json.dumps(rows)
        else:
            raise PersonException(f'Person with id {person.id} not found')

    def delete(self, person):
        self.__guard_is_not_empty(person)
        _execute_sql_with_no_return(f"DELETE FROM person WHERE id = {person.id}")
        return True


    def create(self, person):
        self.__guard_is_not_empty(person)
        rows = _execute_sql_with_return('INSERT INTO person(name, age) VALUES (%s, %s) RETURNING id;', (person.name, person.age))
        return json.dumps(*rows)


    def update(self, person):
        rows = _execute_sql_with_return(f"SELECT * FROM person WHERE id = {person.id};")
        if rows:
            _execute_sql_with_no_return("UPDATE person SET name = %s, age = %s WHERE id = %s;", (person.name, person.age, person.id))
            return True
        else:
            raise PersonException(f'Person with id {person.id} not found')



