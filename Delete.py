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

def delete_where(conn, table, **kwargs):
    qs = []
    values = tuple()
    for k, v in kwargs.items():
        qs.append(f"{k}=?")
        values += (v,)
    q = " AND ".join(qs)
    
    sql = f"DELETE FROM {table} WHERE {q}"

    cur = conn.cursor()
    cur.execute(sql, values)
    conn.commit()
    print("Wykonano funkcję DELETE")


if __name__ == "__main__":
    db_file = "Baza_danych.db"
    conn = create_connection(db_file)
    table = "Dane_transportowe"
    kwargs = {"status" : "W drodze", "Przewoźnik" : "DHL"}

    d = delete_where(conn, table,**kwargs)
