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

# SKŁADNIA:    UPDATE tabela SET argument1 = x, argument2 = y, argument3 = z WHERE id = 3

def update(conn, table, pk, **kwargs):
    parameters = [f"{k} = ?" for k in kwargs]
    parameters = ", ".join(parameters)
    values = tuple(v for v in kwargs.values())
    values += (pk, )

    sql = f"UPDATE {table} SET {parameters} WHERE Nr_listu = ?"
    
    try:
        cur = conn.cursor()
        cur.execute(sql, values)
        conn.commit()
        print("Funkcję update zrealizowano prawidłowo")
    except sqlite3.OperationalError as e:
        print(e)


    
if __name__ == "__main__":
    db_file = "Baza_danych.db"
    conn = create_connection(db_file)
    table = "Dane_transportowe"
    pk = "234567891"
    kwargs = {"status" : "W drodze", "Przewoźnik" : "TNT"}

    up = update(conn, table, pk, **kwargs)





    