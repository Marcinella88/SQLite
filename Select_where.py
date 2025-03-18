import sqlite3
from sqlite3 import Error

def create_connection(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        print(f"Połączono z bazą o nazwie: {db_file}, wersja SQLite {sqlite3.version}")
    except Error as e:
        print(e)
    return conn

def select_where(conn, table, **query):
   cur = conn.cursor()
   qs = []
   values = ()
   for k, v in query.items():
       qs.append(f"{k}=?")
       values += (v,)
   q = " AND ".join(qs)
   cur.execute(f"SELECT * FROM {table} WHERE {q}", values)
   rows = cur.fetchall()
   return rows


if __name__ == "__main__":
    db_file = "Baza_danych.db"
    conn = create_connection(db_file)

    query = {"Status":"W drodze","Przewoźnik":"TNT"}
    table = "Dane_transportowe"

    rows = select_where(conn, table, **query)
    print(rows)
