# Praca z bazą danych SQLite

# importujemy moduł sqlite3 i Error z sqlite3
import sqlite3
from sqlite3 import Error

# Funkcje tworząca połączenie z bazą danych lub tworząca bazę danych jeśli bazy o takiej nazwie brakuje w lokalizacji.

def create_connection(db_file):
    conn = None                                         # zmienna będąca połączeniem z bazą
    try:
        conn = sqlite3.connect(db_file)                 # zmienia przyjmuje funkcję connect - łączenie się z bazą
        print(f"Połączono z bazą o nazwie {db_file}, wersja sqlite: {sqlite3.version}")
    except Error as e:                                  # jeśli wystąpi błąd z połączeniem wyświetli się błąd z bazy błędów
        print(e)
    return conn

# TWORZYMY FUNKCJĘ która posłuży nam do tworzenia zapytań w SQL
# funckja będzie miałą dwa parametry:
    # parametr conn - połączenie z bazą
    # parametr - treść zapytania SQL

def execute_sql(conn, sql):
    try:
       c = conn.cursor()   # wywołujemy funkcję cursor na conn czyli na elemencie łączącym z bazą i przypisujemy do zmiennej c
       c.execute(sql)      # wywołujemy na zmienna c funkcję execute wykonaj z parametrem sql
    except Error as e:
        print(e)

# TWORZYMY FUNKCJĘ która będzie dodawać dane do tabeli projekty za pomocą polecenia sql które będzie zbudowane z dwóch krotek i będzie wykorzystywało sparametryzowane zapytanie.

def add_project(conn, project):
    sql = """ INSERT INTO projects(nazwa, start_date, end_date) VALUES(?,?,?) """
    cur = conn.cursor()
    cur.execute(sql, project)
    conn.commit()
    return cur.lastrowid

def add_task(conn, task):
    sql = """ INSERT INTO tasks (project_id, nazwa, opis, status, start_date, end_date) VALUES (?,?,?,?,?,?) """

    cur=conn.cursor()
    cur.execute(sql, task)
    conn.commit()
    return cur.lastrowid

if __name__ == "__main":


# TWORZYMY ZMIENNE które posłużą nam do stworzenia tabeli: "projekty" i tabeli: "zadania"

create_projects_sql = """
    CREATE TABLE IF NOT EXISTE projects (
    id integer PRIMARY KEY,
    nazwa text NOT NULL,
    start_date text,
    end_date text    
    );
    """

create_tasks_sql = """
    CREATE TABLE IF NOT EXISTE tasks (
        id integer PRIMARY KEY,
        project_id integer NOT NULL,
        nazwa VARCHAR(250) NOT NULL,
        opis text,
        status VARCHAR(15) NOT NULL,
        start_date text NOT NULL,
        end_date text NOT NULL
        FOREIGN KEY (project_id) REFERENCES projects (id)
    );
    """

db_file ="Baza_sql"
conn = create_connection(db_file)
project = ("Powtórka z angola", "2025-03-17", "2025-03-18")
pr_id = add_project(conn, project)

task = (pr_id, "Czasowniki regularne", "Zapamiętaj czasowniki ze strony 30", "started", "2025-03-17 11:00:00", "2025-03-18 12:00:00")

task_id = add_task(conn, task)



if conn is not None:
    execute_sql(conn, create_projects_sql)
    execute_sql(conn, create_tasks_sql)
    conn.close()




    



