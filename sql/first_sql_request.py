import json

import psycopg2
import psycopg2.extras

con = psycopg2.connect(host='localhost',
                        port=5432,
                        user='postgres',
                        dbname='postgres')
con.autocommit = True

with con:
    cur = con.cursor(cursor_factory=psycopg2.extras.RealDictCursor) # объект курсор - также известный как "исполнитель запросов"
    # query = f"INSERT INTO public.person (name, age) VALUES ('Toby', 49)"
    # cur.execute(query)
    # rows = cur.fetchall()  # fetchall() - получи все значения из запроса и fetchone() - получи одно значение
    query = f"SELECT * FROM person"
    cur.execute(query)
    # rows = cur.fetchall()
    print(json.dumps(cur.fetchone()))
    print(json.dumps(cur.fetchone()))
    print(json.dumps(cur.fetchone()))