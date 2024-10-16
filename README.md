# Task Manager CLI Application

## Project Description
The **Task Manager** is a command-line interface (CLI) application that allows users to manage tasks easily. Users can add, view, delete, and mark tasks as completed. The application also supports saving tasks to a file and loading them back when the application is reopened, making it persistent across sessions.

## Features
- **Add Task**: Create a new task with a title.
- **View Tasks**: Display all tasks with their ID, title, and completion status (✔️ for completed, ❌ for pending).
- **Delete Task**: Remove a task by its ID.
- **Mark Task as Complete**: Mark a specific task as completed by its ID.
- **Save Tasks**: Save all tasks to a `tasks.json` file for persistence.
- **Load Tasks**: Load tasks from `tasks.json` when the application starts.

## How to Run the Application
1. **Clone the repository** or download the project files to your local machine.
2. **Navigate to the project directory**:
    ```bash
    cd task_manager
    ```
3. **Run the application**:
    ```bash
    python task_manager.py
    ```

## Command-Line Interface (CLI) Options
When running the application, the following options will be available in the CLI menu:

1. **Add Task**: Adds a new task. You will be prompted to enter a task title.
2. **View Tasks**: Displays all tasks with their IDs and statuses.
3. **Delete Task**: Deletes a task by its ID.
4. **Mark Task as Complete**: Marks a task as completed by its ID.
5. **Save Tasks**: Saves the current tasks to a JSON file.
6. **Exit**: Saves the tasks and exits the application.

## Example Usage
1. Start the task manager:
    ```
    Task Manager
    1. Add Task
    2. View Tasks
    3. Delete Task
    4. Mark Task as Complete
    5. Save Tasks
    6. Exit
    Choose an option: 
    ```
2. Add a task:
    ```
    Choose an option: 1
    Enter task title: Buy groceries
    Added task: Task(id=1, title='Buy groceries', completed=False)
    ```
3. View tasks:
    ```
    Choose an option: 2
    1: Buy groceries [❌]
    ```

## Requirements
- Python 3.x

## Files Included
- **task_manager.py**: The main script for the task manager.
- **tasks.json**: The file where tasks are saved (automatically generated).

## License
This project is licensed under the MIT License.

