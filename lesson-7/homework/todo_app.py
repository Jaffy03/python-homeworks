import abc
import csv
from datetime import datetime

class Task:
    def __init__(self, task_id, title, description, due_date, status):
        self.task_id = task_id
        self.title = title
        self.description = description
        self.due_date = due_date
        self.status = status
    
    def __str__(self):
        due_date_str = self.due_date if self.due_date else "No Due Date"
        return f"{self.task_id}, {self.title}, {self.description}, {due_date_str}, {self.status}"

class TaskManager:
    def __init__(self):
        self.tasks = []
        self.file_handler = None 
        
    def add_task(self, task):
        #add new task
        self.tasks.append(task)
        print("Task added successfully")
        
    def view_tasks(self):
        if not self.tasks:
            print("Not tasks found")
            return
        print("Tasks:")
        for task in self.tasks:
            print(task)
            
    def update_task(self, task_id, **kwargs):
        """Update a task's details."""
        for task in self.tasks:
            if task.task_id == task_id:
                for key, value in kwargs.items():
                    setattr(task, key, value)
                print("Task updated successfully!")
                return
        print(f"No task found with ID: {task_id}")
    
    def delete_task(self, task_id):
        """Delete a task by its ID."""
        for task in self.tasks:
            if task.task_id == task_id:
                self.tasks.remove(task)
                print("Task deleted successfully!")
                return
        print(f"No task found with ID: {task_id}")
    
    def filter_tasks(self, status):
        """Filter tasks by status."""
        filtered_tasks = [task for task in self.tasks if task.status == status]
        if not filtered_tasks:
            print(f"No tasks found with status: {status}")
            return
        print(f"Tasks with status '{status}':")
        for task in filtered_tasks:
            print(task)
            
    def save_tasks(self):
        """Save tasks to a file."""
        self.file_handler.save(self.tasks)
        print("Tasks saved successfully!")

    def load_tasks(self):
        """Load tasks from a file."""
        self.tasks = self.file_handler.load()
        print("Tasks loaded successfully!")
        
class FileHandler(abc.ABC):
    """Abstract base class for file handlers."""
    @abc.abstractmethod
    def save(self, tasks):
        pass

    @abc.abstractmethod
    def load(self):
        pass        

class CSVFileHandler(FileHandler):
    #File handler for CSV format.
    def __init__(self, file_path='tascs.csv'):
        self.file_path = file_path
    
    def save(self, tasks):
        #save to a CSV file
        with open(self.file_path, 'w', newline = '') as file:
            writer = csv.writer(file)
            writer.writerow(["Task ID", "Title", "Description", "Due Date", "Status"])  # Header
            for task in tasks:
                writer.writerow([task.task_id, task.title, task.description, task.due_date, task.status])
    
    def load(self):
        tasks = []
        try:
            with open(self.file_path, "r") as file:
                reader = csv.reader(file)
                next(reader)  # Skip header
                for row in reader:
                    task_id, title, description, due_date, status = row
                    due_date = due_date if due_date != "None" else None
                    tasks.append(Task(int(task_id), title, description, due_date, status))
        except FileNotFoundError:
            pass
        return tasks

def display_menu():
    #Display the menu options.
    print("\nWelcome to the To-Do Application!")
    print("1. Add a new task")
    print("2. View all tasks")
    print("3. Update a task")
    print("4. Delete a task")
    print("5. Filter tasks by status")
    print("6. Save tasks")
    print("7. Load tasks")
    print("8. Exit")

def file_format(manager):
    #Here for now making file format automatically csv, then it is possible to further modify it and ask user to choose a file format necessary
    manager.file_handler = CSVFileHandler()

def main():
    manager = TaskManager()
    while True:
        display_menu()
        choice = input("Enter your choice: ")
        if choice == "1":
            task_id = int(input("Enter Task ID: "))
            title = input("Enter Title: ")
            description = input("Enter Description: ")
            due_date = input("Enter Due Date (YYYY-MM-DD, optional): ")
            due_date = due_date if due_date else None
            status = input("Enter Status (Pending/In Progress/Completed): ")
            task = Task(task_id, title, description, due_date, status)
            manager.add_task(task)
        elif choice == "2":
            manager.view_tasks()
        elif choice == "3":
            task_id = int(input("Enter Task ID to update: "))
            title = input("Enter new Title (leave blank to skip): ")
            description = input("Enter new Description (leave blank to skip): ")
            due_date = input("Enter new Due Date (YYYY-MM-DD, leave blank to skip): ")
            status = input("Enter new Status (Pending/In Progress/Completed, leave blank to skip): ")
            kwargs = {}
            if title:
                kwargs["title"] = title
            if description:
                kwargs["description"] = description
            if due_date:
                kwargs["due_date"] = due_date
            if status:
                kwargs["status"] = status
            manager.update_task(task_id, **kwargs)
        elif choice == "4":
            task_id = int(input("Enter Task ID to delete: "))
            manager.delete_task(task_id)
        elif choice == "5":
            status = input("Enter status to filter (Pending/In Progress/Completed): ")
            manager.filter_tasks(status)
        elif choice == "6":
            file_format(manager)
            manager.save_tasks()
        elif choice == "7":
            manager.load_tasks()
        elif choice == "8":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")     
main()            
     