# Todo Application - Phase I

A command-line todo application that stores tasks in memory using Python. The application implements all 5 basic features: Add, Delete, Update, View, and Mark Complete/Incomplete.

## Requirements

- **Python**: 3.13 or higher
- **OS**: Linux/macOS or Windows with WSL 2
- **Package Manager**: UV (optional but recommended)

## Installation

### Using UV (Recommended)

```bash
# Install UV (if not already installed)
curl -LsSf https://astral.sh/uv/install.sh | sh

# Clone the repository
git clone <repository-url>
cd todo-app

# Create virtual environment and install dependencies
uv sync
```

### Using Python Virtual Environment

```bash
# Clone the repository
git clone <repository-url>
cd todo-app

# Create virtual environment
python3.13 -m venv .venv

# Activate virtual environment
# On Linux/macOS:
source .venv/bin/activate
# On Windows:
.venv\Scripts\activate

# Install dependencies (none required, but optional dev tools)
# pip install -e ".[dev]"
```

## Usage

### Available Commands

#### Add a Task
```bash
python -m src.main add "Buy groceries" --desc "Milk, eggs, bread"
```

#### View All Tasks
```bash
python -m src.main view
```

#### Update a Task
```bash
python -m src.main update 1 --title "New title" --desc "New description"
```

#### Delete a Task
```bash
python -m src.main delete 1
```

#### Mark Task as Complete
```bash
python -m src.main complete 1
```

#### Mark Task as Incomplete
```bash
python -m src.main incomplete 1
```

#### Get Help
```bash
python -m src.main --help
```

## Example Workflow

```bash
# Add tasks
python -m src.main add "Complete project" --desc "Finish the todo application"
python -m src.main add "Review code" --desc "Review all pull requests"
python -m src.main add "Write tests" --desc "Add unit tests for all features"

# View all tasks
python -m src.main view
# Output:
# 📋 Todo List:
# ============================================================
# [○] #1: Complete project
#      └─ Finish the todo application
# [○] #2: Review code
#      └─ Review all pull requests
# [○] #3: Write tests
#      └─ Add unit tests for all features
# ============================================================

# Mark a task as complete
python -m src.main complete 1

# View updated tasks
python -m src.main view
# Output:
# 📋 Todo List:
# ============================================================
# [✓] #1: Complete project
#      └─ Finish the todo application
# [○] #2: Review code
#      └─ Review all pull requests
# [○] #3: Write tests
#      └─ Add unit tests for all features
# ============================================================

# Update a task
python -m src.main update 2 --title "Code review and approval"

# Delete a completed task
python -m src.main delete 1
```

## Features

- ✓ **Add Tasks**: Create new tasks with title and optional description
- ✓ **View Tasks**: Display all tasks with completion status indicators
- ✓ **Update Tasks**: Modify task title and description
- ✓ **Delete Tasks**: Remove tasks by ID
- ✓ **Mark Complete**: Toggle task completion status
- ✓ **In-Memory Storage**: Fast, instant access (tasks reset on restart)
- ✓ **Clean CLI**: Easy-to-read command interface with clear feedback

## Project Structure

```
.
├── constitution.md              # Project constitution and principles
├── README.md                    # This file
├── CLAUDE.md                    # Claude Code implementation guide
├── pyproject.toml               # Project metadata and dependencies
├── requirements.txt             # Python dependencies
├── src/
│   ├── __init__.py             # Package initialization
│   ├── main.py                 # CLI entry point and command handlers
│   └── todo.py                 # Core Task and TodoApp classes
└── specs_history/              # Historical specification files
    ├── spec_add_task.json
    ├── spec_delete_task.json
    ├── spec_update_task.json
    ├── spec_view_tasks.json
    └── spec_mark_complete.json
```

## Development

### Running Tests
```bash
python -m pytest tests/ -v
```

### Code Quality
- **Style**: PEP 8 compliant
- **Documentation**: Comprehensive docstrings
- **Type Hints**: Used throughout codebase

## Architecture

### Task Class
Represents a single todo item with:
- `id`: Unique identifier (integer)
- `title`: Task title (string)
- `description`: Optional detailed description (string)
- `completed`: Completion status (boolean)
- `created_at`: Creation timestamp (datetime)

### TodoApp Class
Main application class managing:
- Task collection (stored in memory)
- Task ID generation
- CRUD operations: Add, View, Update, Delete
- Status management: Complete/Incomplete

## Future Enhancements

- [ ] File-based persistence (JSON/SQLite)
- [ ] Task priorities and categories
- [ ] Due dates and reminders
- [ ] Recurring tasks
- [ ] Multi-user support
- [ ] Web interface
- [ ] Task search and filtering

## License

MIT License

## Contributors

- Development Team

## Support

For issues, questions, or contributions, please open an issue on the GitHub repository.

"# Phase-I-Todo-In-Memory-Python-Console-App" 
