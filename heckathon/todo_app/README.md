# Todo Application

A command-line todo application that stores tasks in memory using Python. The application implements all 5 basic features: Add, Delete, Update, View, and Mark Complete.

## Installation

This application requires Python 3.7 or higher. No external dependencies are needed.

```bash
# Clone or download the repository
git clone <repository-url>

# Navigate to the project directory
cd todo_app
```

## Usage

The application supports the following commands:

### Add a Task
```bash
python todo_app.py add "Task description here"
```

### View All Tasks
```bash
python todo_app.py view
```

### Update a Task
```bash
python todo_app.py update <task_id> "New task description"
```

### Delete a Task
```bash
python todo_app.py delete <task_id>
```

### Mark a Task as Complete
```bash
python todo_app.py complete <task_id>
```

### Get Help
```bash
python todo_app.py --help
```

## Example

```bash
# Add tasks
python todo_app.py add "Buy groceries"
python todo_app.py add "Walk the dog"

# View tasks
python todo_app.py view
# Output:
# Todo List:
# [○] #1: Buy groceries
# [○] #2: Walk the dog

# Mark a task as complete
python todo_app.py complete 1

# View tasks again
python todo_app.py view
# Output:
# Todo List:
# [✓] #1: Buy groceries
# [○] #2: Walk the dog
```

## Features

- Add new tasks with descriptions
- View all tasks with their completion status
- Update existing task descriptions
- Delete tasks by ID
- Mark tasks as complete
- In-memory storage (tasks are not persisted between runs)
- Command-line interface with clear error messages