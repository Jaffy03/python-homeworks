import os
class Employee:
    def __init__(self, employee_id, name, position, salary):
        self.employee_id = employee_id
        self.name = name
        self.position = position
        self.salary = salary
    
    def __str__(self):
        return f"{self.employee_id}, {self.name}, {self.position}, {self.salary}"

class EmployeeManager:
    def __init__(self, file_path="employees.txt"):
        self.file_path = file_path
        
        if not os.path.exists(self.file_path):
            with open(self.file_path, 'w') as file:
                file.write('')
    
    def add_employee(self, employee):
        with open("employees.txt", 'a') as file:
            file.write(str(employee) + "\n")
        print("Added successfully")
    
    def view_records(self):
        if os.path.getsize(self.file_path) == 0:
            print("No employee records found")
            return
        with open(self.file_path) as file:
            for line in file:
                print(line.strip())
    
    def id_search(self, employee_id):
        with open(self.file_path) as file:
            for line in file:
                emp_data = line.strip().split(", ")
                if emp_data[0] == str(employee_id):
                    print("Employee Found:")
                    print(line.strip())
                    return
        print(f"No employee found with ID: {employee_id}")
    
    def update_employee(self, employee_id, new_name, new_position, new_salary):
        temp_file = self.file_path +'.tmp'
        updated = False
        with open(self.file_path) as file, open(temp_file, 'w') as temp:
            for line in file:
                emp_data = line.strip().split(", ")
                if emp_data[0] == str(employee_id):
                    temp.write(f"{employee_id}, {new_name}, {new_position}, {new_salary}\n")
                    updated = True
                else:
                    temp.write(line)
        if updated:
            os.replace(temp_file, self.file_path)
            print("Updated successfully!")
        else:
            os.remove(temp_file)
            print("No employee found with corresponding ID")
    
    def delete_employee(self, employee_id):
        temp_file = self.file_path +'.tmp'
        deleted = False
        with open(self.file_path) as file, open(temp_file, 'w') as temp:
            for line in file:
                emp_data = line.strip().split(", ")
                if emp_data[0] == str(employee_id):
                    deleted = True
                else:
                    temp.write(line)
        if deleted:
            os.replace(temp_file, self.file_path)
            print("Deleted successfully!")
        else:
            os.remove(temp_file)
            print("No employee found with corresponding ID")

def display_menu():
    print("\nWelcome to the Employee Records Manager!")
    print("1. Add new employee record")
    print("2. View all employee records")
    print("3. Search for an employee by Employee ID")
    print("4. Update an employee's information")
    print("5. Delete an employee record")
    print("6. Exit")

def main():
    manager = EmployeeManager()
    while True:
        display_menu()
        choice = input("Enter your choice: ")
        if choice == "1":
            employee_id = input("Enter Employee ID: ")
            name = input("Enter Name: ")
            position = input("Enter Position: ")
            salary = input("Enter Salary: ")
            employee = Employee(employee_id, name, position, salary)
            manager.add_employee(employee)
        elif choice == "2":
            manager.view_records()
        elif choice == "3":
            employee_id = input("Enter Employee ID to search: ")
            manager.id_search(employee_id)
        elif choice == "4":
            employee_id = input("Enter Employee ID to update: ")
            new_name = input("Enter new Name: ")
            new_position = input("Enter new Position: ")
            new_salary = input("Enter new Salary: ")
            manager.update_employee(employee_id, new_name, new_position, new_salary)
        elif choice == "5":
            employee_id = input("Enter Employee ID to delete: ")
            manager.delete_employee(employee_id)
        elif choice == "6":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

main()
        
                     