# Todo App - Quick Command Reference

## Installation

```bash
# Windows WSL 2 Setup (if needed)
wsl --install
wsl --set-default-version 2
wsl --install -d Ubuntu-22.04

# Setup in Linux/macOS/WSL
python3.13 -m venv .venv
source .venv/bin/activate
```

## Command Examples

### Add a Task
```bash
# With description
python -m src.main add "Buy groceries" --desc "Milk, eggs, bread, butter"

# Without description
python -m src.main add "Walk the dog"
```

### View All Tasks
```bash
python -m src.main view
```

### Update a Task
```bash
# Update title only
python -m src.main update 1 --title "New title"

# Update description only
python -m src.main update 1 --desc "New description"

# Update both
python -m src.main update 1 --title "New title" --desc "New description"
```

### Delete a Task
```bash
python -m src.main delete 1
```

### Mark Task as Complete
```bash
python -m src.main complete 1
```

### Mark Task as Incomplete
```bash
python -m src.main incomplete 1
```

### Get Help
```bash
python -m src.main --help
python -m src.main add --help
python -m src.main update --help
```

## Demo

Run the feature demonstration:
```bash
python demo.py
```

This shows all features working together.

## Project Files

- `src/todo.py` - Core application logic
- `src/main.py` - Command-line interface
- `demo.py` - Feature demonstration
- `README.md` - Full documentation
- `CLAUDE.md` - Implementation guide
- `constitution.md` - Project charter
- `specs_history/` - Feature specifications

## Example Workflow

```bash
# Add tasks
python -m src.main add "Complete project" --desc "Finish todo app"
python -m src.main add "Review code"
python -m src.main add "Write tests" --desc "Add unit tests"

# View tasks
python -m src.main view

# Mark task 1 as complete
python -m src.main complete 1

# Update task 2
python -m src.main update 2 --title "Code review and approval"

# View updated list
python -m src.main view

# Delete task 3
python -m src.main delete 3

# View final list
python -m src.main view
```

## Notes

- Tasks are stored in memory only
- Each command runs independently
- Task IDs are auto-incrementing
- Use `demo.py` to see persistent state across operations
