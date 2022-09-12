# - get all people (name,surname) who earn more than x amount. Surnames should be alpabetically in order.
# SELECT name, surname, salary FROM Darbuotojai WHERE salary > 150000 ORDER BY surname

# - get all people the age between age(x) and age(y) . Get by the names in order (alpha)
# SELECT age FROM Darbuotojai WHERE age BETWEEN 20 AND 50

# - specific task: get all people who earn no more than 200k but no less than 100k, and ages are between 25 and 50, gruoped by name and surname and order from highest to lowest income.
## SELECT name, surname, salary, age FROM Darbuotojai WHERE salary BETWEEN 100000 AND 200000 AND age BETWEEN 25 AND 50 ORDER BY salary DESC

# - get all people salary the age between age(x) and age(y) . Get by the names in order (alpha)
# SELECT salary FROM Darbuotojai WHERE age BETWEEN 20 AND 29

from main import *

class Client():
    def __init__(self):
        self.db = self.initialise_db()
        self.table_name = input("enter table name : ")
        self.interface()
        

    def initialise_db(self) -> 'My_db':
        db_name = input("\n\nenter DB name : ")
        return My_db(db_name)

    def interface(self) -> None:
        first_input = int(input("Hey, welcome to our HR system, press button bellow and choose what would you like to do : \n\n\
        Print ppl name who earn specific salary press- 1\n\n\tPrint all workers name press- 2\n\n\tDelete specific user press- 3\n\n\
        if you want to create db press- 4\n\n\tCreate  table in exicting DB - 5 \n\n\tPopulate exicting table with rando values -6 \n\n\
        Get all ppl names and surname who earn more that specific amount(sorted in alphabetical order) - 7 \n\n\
        Get all ppl names in age range -8\n\n\tGet ppl who earn between 100k and 200k, and between 25 and 50 - 9\n\n\
        Populate existing table with 500 ppl - 10\n\n\tGet average salary by Age groups - 11\n\n"))
        print(first_input)

        if first_input == 1:
            amount= input("Program will show you people which earns greater salary, than your given amount, enter amount: ")
            print(self.db.rich_ppl(self.table_name, amount))
            
        elif first_input == 2:
            print(self.db.find_all_users(self.table_name))

        elif first_input == 3:
            surname= input('Enter person surname : ')
            self.db.delete_user(table_name=self.table_name, surname=surname)

        elif first_input == 4:
            db_name = input("\n\nenter DB name : ")
            My_db(db_name)
            
        elif first_input == 5:
            self.db.create_table(table_name=self.table_name)

        elif first_input == 6:
            [self.db.random_entries(table_name=self.table_name) for _ in range(50)]

        elif first_input == 7:
            salary = input("We will show you ppl who earn more that your provided salary, enter amount: ")
            print(self.db.querie_1(table_name=self.table_name, salary=salary))

        elif first_input == 8:
            min_age = input("enter min age: ")
            max_age = input("enter min age: ")
            print(self.db.querie_2(table_name = self.table_name, min_age=min_age, max_age=max_age))

        elif first_input == 9:
            print(self.db.querie_3(table_name=self.table_name))

        elif first_input == 10:
            [self.db.random_entries(table_name=self.table_name) for _ in range(500)]

        elif first_input == 11:
            [self.average_salary(min_age = (x*10 if x != 1 else 18), max_age=(y*10+9)) for x, y in zip(range(1,9), range(1,10))]

        else:
            print("You need to choose between 1 - 11 ")

    def average_salary(self, min_age:int, max_age:int) -> float:
        answ = [item for t in ([x for x in (self.db.querie_4(table_name = self.table_name, min_age=min_age, max_age=max_age))]) for item in t]
        print(f"in age between {min_age} and {max_age} salary is {(round(sum(answ)/len(answ),2))}")


if __name__ == "__main__":
    interface = Client()
