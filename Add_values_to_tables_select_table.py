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

def add_customers_date(conn, customers):
    sql = """ INSERT INTO Dane_klientow (Numer_umowy, Odbiorca, Nadawca) VALUES (?,?,?) """

    cur = conn.cursor()
    cur.execute(sql, customers)
    conn.commit()
    print("Dodano dane klienta!")
    return cur.lastrowid

def add_transportation_date(conn, transportation):
    sql = """ INSERT INTO Dane_transportowe (Nr_listu, Numer_umowy, Przewoźnik, Status) VALUES (?,?,?,?) """

    cur = conn.cursor()
    cur.execute(sql, transportation)
    conn.commit()
    print("Dodano dane transportowe!")
    return cur.lastrowid

def select_all(table):

    cur = conn.cursor()
    cur.execute(f"SELECT * FROM {table}")
    print(f"Cała zawartość tabeli: {table}")
    rows = cur.fetchall()
    return rows

if __name__ == "__main__":
    db_file = "Baza_danych.db"
    conn = create_connection(db_file)

    customers = (103, "Ambroży Adamski", "Anna Aniewska")
    transportation = (456789123, 103, "TNT", "W drodze")
    tableK = "Dane_klientow"
    tableT = "Dane_transportowe"

    #add_cust = add_customers_date(conn, customers)
    add_trans = add_transportation_date(conn, transportation)

    rows = select_all(tableK)
    print(rows)
    rows = select_all(tableT)
    print(rows)

