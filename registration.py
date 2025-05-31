import sqlite3

connection = sqlite3.connect("company_employees.db")

cursor = connection.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS company_employees (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        position TEXT,
        salary DECIMAL(10, 2),
        dept TEXT
    )
""")

print("Welcome")

class Employee():

    def __init__(self):
        self.connection = sqlite3.connect("company_employees.db")
        self.cursor = self.connection.cursor()
        
    def add_employee(self):
        while True:
            print("Let's set up an employee in the company")
            name = input("First, what is their name?: ")
            position = input("What about their position here?: ")
            salary = float(input("How much is their salary here?: "))
            dept = input("And what dept are they going to work in?: ")

            if name and position and salary and dept:
                self.cursor.execute("INSERT INTO company_employees (name, position, salary, dept) VALUES (?, ?, ?, ?)", (name, position, salary, dept))
                self.connection.commit()
                print("Your new employee has been successfully added")

            print('Type "yes" to continue your operation')
            print("Or")
            print('Type "no" to cancel it')   

            option = input('Would you like to add another one?: ')
            if option != "yes":
                print("Okay, I hope to see you later")
                break

    def update_employees(self):
        options = ["1. name", "2. position", "3. salary", "4- dept"]
        for item in options:
            print(item)

        option = int(input("Which category would you like to update?: "))
        changed_name = input("Type here the name of the employee that you want to update: ")

        self.cursor.execute("SELECT * FROM company_employees WHERE name = ?", (changed_name,))
        employee_exist = self.cursor.fetchone()

        if employee_exist is not None:

            if option == 1: 
                print("Let's set their new name then")
                new_name = input("Tell me their new name: ")
                if new_name:
                    self.cursor.execute("UPDATE company_employees SET name = ? WHERE name = ?", (new_name, changed_name))
                    self.connection.commit()
                    print(f"The employee {new_name} has been updated")

            elif option == 2:
                print("Let's set their new position then")
                new_position = input("Tell me their new position: ")
                if new_position:
                    self.cursor.execute("UPDATE company_employees SET position = ? WHERE name = ?", (new_position, changed_name))
                    self.connection.commit()
                    print(f"The employee {changed_name} has been updated")

            elif option == 3:
                print("Let's set their new salary then")
                new_salary = float(input("Tell me their new salary: "))
                if new_salary:
                    self.cursor.execute("UPDATE company_employees SET salary = ? WHERE name = ?", (new_salary, changed_name))
                    self.connection.commit()
                    print(f"The employee {changed_name} has been updated")

            elif option == 4:
                print("Let's set their new dept then")
                new_dept = input("Tell me their new dept: ")
                if new_dept:
                    self.cursor.execute("UPDATE company_employees SET dept = ? WHERE name = ?", (new_dept, changed_name))
                    self.connection.commit()
                    print(f"The employee {changed_name} has been updated")

        else:
            print("Type something valid")

    def show_employees(self):
        print("Let's see the employees of the company")
        self.cursor.execute("SELECT * FROM company_employees")
        employees = self.cursor.fetchall()

        if employees:
            for employee in employees:
                print(f"ID: {employee[0]}")
                print(f"Name: {employee[1].capitalize()}")
                print(f"Position: {employee[2].capitalize()}")
                print(f"Salary: {employee[3]: .2f}R$")
                print(f"Department: {employee[4].upper()}")
                print("-" * 30)
        else:
            print("No employee found in your database") 

    def delete_employees(self):
        print("Let's delete some employees then")
        deleted_employee = input("Tell me the name of the person you want to delete: ")

        self.cursor.execute("SELECT * FROM company_employees WHERE name = ?", (deleted_employee,))
        employee = self.cursor.fetchone()

        if employee is not None:
            self.cursor.execute("DELETE FROM company_employees WHERE name = ?", (deleted_employee,))
            self.connection.commit()
            print(f"The employee {deleted_employee} has been deleted")
        else:
            print(f"The employee {deleted_employee} hasn't been found in your company")

worker = Employee()
worker.add_employee()
worker.update_employees()
worker.show_employees()
worker.delete_employees()