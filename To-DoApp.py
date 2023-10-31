import json
import os
from datetime import datetime

# Define the file where tasks will be saved
TASKS_FILE = "tasks.json"

# Load tasks from a file if it exists
def load_tasks():
    if os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, "r") as file:
            return json.load(file)
    else:
        return []

# Save tasks to a file
def save_tasks(tasks):
    with open(TASKS_FILE, "w") as file:
        json.dump(tasks, file, indent=4)

# Print all tasks
def list_tasks(tasks):
    if not tasks:
        print("No tasks found.")
    else:
        for index, task in enumerate(tasks, 1):
            print(f"{index}. {task['title']} (Due: {task['due_date']})")

# Add a new task
def add_task(tasks):
    title = input("Enter task title: ")
    due_date = input("Enter due date (YYYY-MM-DD): ")
    
    try:
        datetime.strptime(due_date, "%Y-%m-%d")
    except ValueError:
        print("Invalid date format. Use YYYY-MM-DD.")
        return

    tasks.append({"title": title, "due_date": due_date})
    save_tasks(tasks)
    print("Task added successfully.")

# Update a task
def update_task(tasks):
    list_tasks(tasks)
    choice = int(input("Enter the task number to update: ")) - 1

    if 0 <= choice < len(tasks):
        new_title = input("Enter new title (or leave blank to keep the same): ")
        new_due_date = input("Enter new due date (YYYY-MM-DD) (or leave blank to keep the same): ")

        if new_title:
            tasks[choice]["title"] = new_title
        if new_due_date:
            try:
                datetime.strptime(new_due_date, "%Y-%m-%d")
                tasks[choice]["due_date"] = new_due_date
            except ValueError:
                print("Invalid date format. Task not updated.")
                return

        save_tasks(tasks)
        print("Task updated successfully.")
    else:
        print("Invalid task number.")

# Main function
def main():
    tasks = load_tasks()
    
    while True:
        print("\nTO-DO LIST APPLICATION")
        print("1. List Tasks")
        print("2. Add Task")
        print("3. Update Task")
        print("4. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == "1":
            list_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            update_task(tasks)
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
