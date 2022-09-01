## Kai inicijuojame klase sukuriame DB jeigu jos nera,   metodai basic CRUD operacijos
import sqlite3
from sqlite3 import DatabaseError





class SqlDatabase:
    def __init__(self, db_name: str) -> None:
        self._conn = sqlite3.connect(db_name)
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

    def create(self, table_name: str, entry_values: str) -> None:
        with self._conn:
            self._cursor.execute(f"INSERT INTO {table_name} VALUES ({entry_values})")

    def read(self):
        pass

    def update(self):
        pass

    def delete(self):
        pass

def main():
    dtbs = SqlDatabase("Food")
    


if __name__ == "__main__":
    main()