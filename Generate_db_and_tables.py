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

def execute(conn, sql):
    try:
        cur = conn.cursor()
        cur.execute(sql)
    except Error as e:
        print(e)


if __name__ == "__main__":

    create_customers_date = """
        CREATE TABLE IF NOT EXISTS Dane_klientow (
            Numer_umowy integer PRIMARY KEY,
            Odbiorca text NOT NULL,
            Nadawca text NOT NULL
    );
    """

    create_transportation_date = """
        CREATE TABLE IF NOT EXISTS Dane_transportowe (
            Nr_listu integer PRIMARY KEY,
            Numer_umowy integer NOT NULL,
            Przewoźnik text NOT NULL,
            Status text NOT NULL,
            FOREIGN KEY (Numer_umowy) REFERENCES Dane_klientow (Numer_umowy) 
    );
    """
    db_file = "Baza_danych.db"

    conn = create_connection(db_file)

    if conn is not None:
        execute(conn, create_customers_date) 
        execute(conn, create_transportation_date) 