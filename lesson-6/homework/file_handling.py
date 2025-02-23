#1 task 1
#getting all the lines into function so i can call them easily and separately test
def add_employee():
    id=input("Enter an id: ")
    name=input("Enter a name: ")
    position=input("Enter a position: ")
    salary=input("Enter a salary: ")
    
    record=f"{id}, {name}, {position}, {salary}\n"
    with open("employees.txt", 'a') as file:
        file.write(record)
    print("Added successfully")


#task 2.2
def no_file(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except FileNotFoundError:
            print("No file was found")
            return None
    return wrapper  
@no_file
def view_records():
    with open('employees.txt') as file:
        records = file.readlines()
        if not records:
            print("No employee records found.")
            return

        print("\nEmployee Records:")
        for record in records:
            print(record.strip())

# tast2.3
@no_file
def id_search(e_id):
    found = False
    with open("employees.txt") as file:
        for line in file:
            record=line.strip().split(", ")
            if record[0] == e_id:
                return record        
    return None       


def id_search_text():
    e_id = input("Enter Employee ID to search: ")
    rec=id_search(e_id)
    if rec:
        print(f"\nEmployee found: {rec}")
    else:
        print("Employee not found")

#task 2.4
def update_employee():
    e_id = input("Enter Employee ID to search: ")
    record = id_search(e_id)
    if not record:
        print("Employee not found")
        return
    print("\nCurrent details: ")
    print(f"Employee ID: {record[0]}")
    print(f"Name: {record[1]}")
    print(f"Position: {record[2]}")
    print(f"Salary: {record[3]}")

    name = input("Enter new name (leave blank to keep current): ")
    position = input("Enter new position (leave blank to keep current): ")
    salary = input("Enter new salary (leave blank to keep current): ")
    
    #update if fields are not empty
    if name: 
        record[1] = name

    if position: 
        record[2] = position
    if salary: 
        record[3] = salary
        # Read all records
    with open("employees.txt", "r") as file:
        records = file.readlines()

    # Write updated records back to the file
    with open("employees.txt", "w") as file:
        for line in records:
            if line.strip().split(", ")[0] == e_id:
                file.write(f"{record[0]}, {record[1]}, {record[2]}, {record[3]}\n")
            else:
                file.write(line)
    print("Employee record updated successfully!")    
    
#task 2.5    
def delete_employee():
    e_id= input("Enter Employee ID to delete: ")
    record = id_search(e_id)
    if not record:
        print("Employee not found")
        return
    with open('employees.txt') as file:
        records = file.readlines()
    
    with open('employees.txt', 'w') as file:
        for line in records:
            if line.strip().split(', ')[0] != e_id:
                file.write(line)
    print("Employee record deleted successfully!")
    
def main():
    while True: 
        print("\nMenu Options")
        print("1. Add new employee record")
        print("2. View all employee records")
        print("3. Search for an employee by Employee ID")
        print("4. Update an employee's information") 
        print("5. Delete an employee record")
        print("6. Exit")
        
        choice= input("Enter your choice(1-6): ").strip()
        if choice =='1':
            add_employee()
        elif choice =='2':
            view_records()
        elif choice == '3':
            id_search_text()
        elif choice == '4':
            update_employee()
        elif choice == '5':
            delete_employee()
        elif choice == '6':
            print("Exiting program!")
            break
        else:
            print("Invalid choice. Enter a number between 1 and 6.")  
main()           
    