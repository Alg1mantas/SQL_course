# Create Console program :
# which would ask to:
# - create database ++++++++++++
# - create table (column names: name, surname. age, salary) ++++
# - populate table with 50 elements (name, surname auto generated, age from 18 to 99, salary from 50 000 to 250000 (with a step size of 25000))


# - print the names of people who earn more than entered value (in a prompt)


# - print all users (names and surnames)  +++++
# - delete user by surname ++++
# OOP, application should be runned a module .

import sqlite3
from sqlite3 import DatabaseError
import names
import random


class My_db:
    def __init__(self, db_name) -> None:
        self._conn = sqlite3.connect(db_name+".db")
        self._cursor = self._conn.cursor()


    def create_table(self, table_name:str) -> None:
        try:
            with self._conn:
                self._cursor.execute(f"""CREATE TABLE IF NOT EXISTS
                {table_name} (
                name text,
                surname text,
                age integer,
                salary integer
                )""")
        except DatabaseError:
            print("Unable to create table! Database error.")
        except Exception as e:
            print(f"Unable to create table!. Error msg: {e}")


    def random_entries(self, table_name:str) -> None:
        with self._conn:
            self._cursor.execute(f"INSERT INTO {table_name}  VALUES ('{names.get_first_name()}', '{names.get_last_name()}', {random.randint(18, 99)}, {(random.randint(2, 10)) * 25000})")



    def rich_ppl(self, table_name:str, amount: int) -> list:
        with self._conn:
            self._cursor.execute(f"SELECT name From {table_name} WHERE salary > {amount}")
            return self._cursor.fetchall()


    def find_all_users(self, table_name:str) -> list:
        with self._conn:
            self._cursor.execute(f"SELECT name, surname From {table_name}")
            return self._cursor.fetchall()


    def delete_user(self,table_name:str, surname:str) -> None:
        with self._conn:
            self._cursor.execute(f"DELETE from '{table_name}' WHERE surname='{surname}'")


    def querie_1(self, table_name:str, salary:int) -> list:
        with self._conn:
            self._cursor.execute(f"SELECT name, surname, salary FROM '{table_name}' WHERE salary > '{salary}' ORDER BY surname")
            return self._cursor.fetchall()

    def querie_2(self,table_name:str, min_age:int, max_age:int) -> list:
        with self._conn:
            self._cursor.execute(f"SELECT name, age FROM '{table_name}' WHERE age BETWEEN '{min_age}' AND '{max_age}'")
            return self._cursor.fetchall()

    def querie_3(self, table_name: str) -> list:
        with self._conn:
            self._cursor.execute(f"SELECT name, surname, salary, age FROM '{table_name}' WHERE salary BETWEEN 100000 AND 200000 AND age BETWEEN 25 AND 50 ORDER BY salary DESC")
            return self._cursor.fetchall()

    def querie_4(self,table_name:str, min_age:int, max_age:int) -> list:
        with self._conn:
            self._cursor.execute(f"SELECT salary FROM '{table_name}' WHERE age BETWEEN '{min_age}' AND '{max_age}'")
            return self._cursor.fetchall()

def main():
    db = My_db(db_name="Workers")
    # db.create_table(table_name="Managers")
    # db.random_entries(table_name="Managers")
    # number_list = [ db.random_entries(table_name="Managers") for x in range(50) ]
    # print(db.rich_ppl(table_name="Managers", amount=200000))
    # print(db.find_all_users(table_name="Managers"))
    # db.delete_user(table_name= "Managers", surname="Spicer")




if __name__ == "__main__":
    main()
    print("Done")