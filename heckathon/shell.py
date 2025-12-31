"""
Interactive Todo Application Shell
Allows running commands one at a time with persistent state
"""

from src.todo import TodoApp
import sys


def print_header():
    """Print the application header."""
    print("\n" + "=" * 70)
    print("[TODO] Interactive Todo Application Shell")
    print("=" * 70)
    print("Type commands below. State persists between commands.\n")


 
 def print_help():
    """Print available commands."""
    print("\n" + "-" * 70)
    print("Available Commands:")
    print("-" * 70)
    print("  add <title> [<desc>]       - Add new task")
    print("  view                        - View all tasks")
    print("  complete <id>               - Mark task as complete")
    print("  incomplete <id>             - Mark task as incomplete")
    print("  update <id> <title>         - Update task title")
    print("  delete <id>                 - Delete task")
    print("  help                        - Show this help")
    print("  exit / quit                 - Exit the app")
    print("-" * 70)


def handle_add(app, args):
    """Handle add command."""
    if len(args) < 2:
        print("[ERROR] Usage: add <title> [<description>]")
        return
    
    title = args[1]
    desc = " ".join(args[2:]) if len(args) > 2 else ""
    
    task = app.add_task(title, desc)
    print(f"[OK] Added task #{task.id}: {task.title}")
    if task.description:
        print(f"  Description: {task.description}")


def handle_view(app):
    """Handle view command."""
    tasks = app.view_tasks()
    if not tasks:
        print("No tasks found.")
    else:
        print("\n[TASKS] Todo List:")
        print("=" * 70)
        for task in tasks:
            status = "X" if task.completed else "O"
            print(f"[{status}] #{task.id}: {task.title}")
            if task.description:
                print(f"     -> {task.description}")
        print("=" * 70)


def handle_complete(app, args):
    """Handle complete command."""
    if len(args) < 2:
        print("[ERROR] Usage: complete <task_id>")
        return
    
    try:
        task_id = int(args[1])
        if app.mark_complete(task_id):
            print(f"[OK] Marked task #{task_id} as complete")
        else:
            print(f"[ERROR] Task #{task_id} not found")
    except ValueError:
        print("[ERROR] Task ID must be a number")


def handle_incomplete(app, args):
    """Handle incomplete command."""
    if len(args) < 2:
        print("[ERROR] Usage: incomplete <task_id>")
        return
    
    try:
        task_id = int(args[1])
        task = app.get_task_by_id(task_id)
        if task:
            task.completed = False
            print(f"[OK] Marked task #{task_id} as incomplete")
        else:
            print(f"[ERROR] Task #{task_id} not found")
    except ValueError:
        print("[ERROR] Task ID must be a number")


def handle_update(app, args):
    """Handle update command."""
    if len(args) < 3:
        print("[ERROR] Usage: update <task_id> <new_title> [<new_desc>]")
        return
    
    try:
        task_id = int(args[1])
        title = args[2]
        desc = " ".join(args[3:]) if len(args) > 3 else None
        
        if app.update_task(task_id, title, desc):
            print(f"[OK] Updated task #{task_id}")
            updated = app.get_task_by_id(task_id)
            print(f"  New title: {updated.title}")
            if updated.description:
                print(f"  New description: {updated.description}")
        else:
            print(f"[ERROR] Task #{task_id} not found")
    except ValueError:
        print("[ERROR] Task ID must be a number")


def handle_delete(app, args):
    """Handle delete command."""
    if len(args) < 2:
        print("[ERROR] Usage: delete <task_id>")
        return
    
    try:
        task_id = int(args[1])
        if app.delete_task(task_id):
            print(f"[OK] Deleted task #{task_id}")
        else:
            print(f"[ERROR] Task #{task_id} not found")
    except ValueError:
        print("[ERROR] Task ID must be a number")


def main():
    """Main interactive shell."""
    app = TodoApp()
    print_header()
    print_help()
    
    while True:
        try:
            user_input = input("\n> ").strip()
            
            if not user_input:
                continue
            
            # Parse command
            parts = user_input.split(maxsplit=1)
            command = parts[0].lower()
            args = user_input.split()
            
            # Handle commands
            if command == "exit" or command == "quit":
                print("\n[EXIT] Goodbye! Tasks have been reset.")
                break
            
            elif command == "help":
                print_help()
            
            elif command == "add":
                handle_add(app, args)
            
            elif command == "view":
                handle_view(app)
            
            elif command == "complete":
                handle_complete(app, args)
            
            elif command == "incomplete":
                handle_incomplete(app, args)
            
            elif command == "update":
                handle_update(app, args)
            
            elif command == "delete":
                handle_delete(app, args)
            
            else:
                print(f"[ERROR] Unknown command: '{command}'. Type 'help' for available commands.")
        
        except KeyboardInterrupt:
            print("\n\n[EXIT] Goodbye!")
            break
        except Exception as e:
            print(f"[ERROR] {e}")


if __name__ == "__main__":
    main()
