import json
import csv

def load_tasks(filename):
    with open(filename) as file:
        tasks = json.load(file)
    return tasks

def display_tasks(tasks):
    print("ID,Task,Completed,Priority")
    for task in tasks:
        print(f"{task['id']},{task['task']},{task['completed']},{task['priority']}")

def save_tasks(filename, tasks):
    with open(filename, 'w') as file:
        json.dump(tasks, file, indent=4)
    print(f"\nTasks saved to {filename}")

def calculate_statistics(tasks):
    total_tasks = len(tasks)
    completed_tasks = sum(1 for task in tasks if task['completed'])
    pending_tasks = total_tasks - completed_tasks
    average_priority = sum(task['priority'] for task in tasks) / total_tasks

    print("\nTask Statistics:")
    print(f"Total tasks: {total_tasks}")
    print(f"Completed tasks: {completed_tasks}")
    print(f"Pending tasks: {pending_tasks}")
    print(f"Average priority: {average_priority:.2f}")

def convert_to_csv(tasks, csv_filename):
    with open(csv_filename, 'w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=['ID', 'Task', 'Completed', 'Priority'])
        writer.writeheader()
        for task in tasks:
            writer.writerow({
                'ID': task['id'],
                'Task': task['task'],
                'Completed': task['completed'],
                'Priority': task['priority']
            })
    print(f"\nTask data converted to {csv_filename}")

if __name__ == "__main__":
    json_file = 'tasks.json'
    csv_file = 'tasks.csv'

    tasks = load_tasks(json_file)
    display_tasks(tasks)
    calculate_statistics(tasks)

    for task in tasks:
        if task['id'] == 1:
            task['completed'] = True
    save_tasks(json_file, tasks)

    convert_to_csv(tasks, csv_file)