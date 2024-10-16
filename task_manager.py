import json
import os

# Global list to hold tasks
tasks = []

# Class representing a task with id, title, and completion status
class Task:
    def __init__(self, task_id, title, completed=False):
        self.id = task_id
        self.title = title
        self.completed = completed

    def __repr__(self):
        return f"Task(id={self.id}, title='{self.title}', completed={self.completed})"

# Function to add a new task to the task list
def add_task(title):
    task_id = len(tasks) + 1  # Assign task ID incrementally
    task = Task(task_id, title)  # Create a new Task instance
    tasks.append(task)  # Add task to the global task list
    print(f"Added task: {task}")  # Inform the user

# Function to display all tasks
def view_tasks():
    if not tasks:
        print("No tasks available.")  # Inform user if there are no tasks
        return
    # Iterate through the task list and display each task with its status
    for task in tasks:
        status = "✔️" if task.completed else "❌"
        print(f"{task.id}: {task.title} [{status}]")

# Function to delete a task by ID
def delete_task(task_id):
    global tasks  # Access global tasks list
    tasks = [task for task in tasks if task.id != task_id]  # Remove task by filtering out the given ID
    print(f"Deleted task with ID: {task_id}")

# Function to mark a task as complete by ID
def mark_task_complete(task_id):
    for task in tasks:
        if task.id == task_id:  # If task ID matches, mark as completed
            task.completed = True
            print(f"Marked task {task_id} as complete.")
            return
    print(f"Task with ID {task_id} not found.")  # Inform if task not found

# Function to save the task list to a JSON file
def save_tasks(filename='tasks.json'):
    # Write tasks to a JSON file by serializing each task's dictionary representation
    with open(filename, 'w') as f:
        json.dump([task.__dict__ for task in tasks], f)
    print("Tasks saved to file.")

# Function to load tasks from a JSON file
def load_tasks(filename='tasks.json'):
    if os.path.exists(filename):  # Check if the file exists
        with open(filename, 'r') as f:
            task_list = json.load(f)  # Load tasks from file
            for task_data in task_list:
                # Rename 'id' to 'task_id' when creating Task instances
                task_data['task_id'] = task_data.pop('id')
                task = Task(**task_data)  # Convert JSON objects to Task instances
                tasks.append(task)  # Add tasks to the global list
        print("Tasks loaded from file.")
    else:
        print("No saved tasks found.")  # Inform user if no tasks are found

# User credentials dictionary
users = {
    "test@example.com": "password123"
}

# Function for user login
def login():
    email = input("Enter your email: ")
    password = input("Enter your password: ")

    if email in users and users[email] == password:
        print("Login successful!")
        return True
    else:
        print("Invalid credentials!")
        return False

# Main function to create the command-line interface (CLI)
def main():
    if not login():  # Prompt login before continuing
        return  # Exit if login fails

    load_tasks()  # Load tasks from file when the program starts

    while True:
        # Display menu options for the user
        print("\nTask Manager")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Delete Task")
        print("4. Mark Task as Complete")
        print("5. Save Tasks")
        print("6. Exit")
        choice = input("Choose an option: ")

        # Process user choice and call the corresponding function
        if choice == '1':
            title = input("Enter task title: ")
            add_task(title)
        elif choice == '2':
            view_tasks()
        elif choice == '3':
            task_id = int(input("Enter task ID to delete: "))
            delete_task(task_id)
        elif choice == '4':
            task_id = int(input("Enter task ID to mark as complete: "))
            mark_task_complete(task_id)
        elif choice == '5':
            save_tasks()  # Save tasks to file
        elif choice == '6':
            save_tasks()  # Save tasks and exit the program
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")  # Handle invalid input

if __name__ == '__main__':
    main()  # Run the program
