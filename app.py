## Kai inicijuojame klase sukuriame DB jeigu jos nera,   metodai basic CRUD operacijos
import sqlite3
from sqlite3 import DatabaseError





class SqlDatabase:
    def __init__(self, db_name: str) -> None:
        self._conn = sqlite3.connect(db_name+".db")
        self._cursor = self._conn.cursor()

    def create_table(self, table_name: str, columns: str) -> None:
        try:
            with self._conn:
                self._cursor.execute(f"""CREATE TABLE IF NOT EXISTS
                {table_name} (
                {columns}
                )""")
        except DatabaseError:
            print("Unable to create table! Database error.")
        except Exception as e:
            print(f"Unable to create table!. Error msg: {e}")

    def write(self, table_name: str, entry_values: str) -> None:
        with self._conn:
            self._cursor.execute(f"INSERT INTO {table_name} VALUES ({entry_values})")

    def read(self, columns: str, table_name: str, where_clause: str) -> list:
        with self._conn:
            self._cursor.execute(f"SELECT ({columns}) From {table_name} WHERE {where_clause}")
            return self._cursor.fetchall()

    def update(self, table_name: str, update_clause: str, where_clause: str) -> None:
        with self._conn:
            self._cursor.execute(f"UPDATE ({table_name}) SET {update_clause} WHERE {where_clause}'")

    def delete(self, table_name: str, where_clause: str) -> None:
        with self._conn:
            self._cursor.execute(f"DELETE from {table_name} WHERE {where_clause}")

def main():
    db = SqlDatabase("Food")
    db.create_table("People", "name text, surname text, age integer")
    # db.write(table_name="People", entry_values="'Jonas', 'Kazlauskas', 69")
    print(db.read(columns="surname",table_name="People", where_clause="age=69"))
    


if __name__ == "__main__":
    main()
    print("Done")