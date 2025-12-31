"""Deprecated: legacy module kept for reference.

This file is retained for backward compatibility but the active
implementation lives in `src/todo.py`. Use `src/main.py` to run
the interactive menu-driven application.
"""

print("WARNING: legacy module todo_app/todo_app.py is deprecated. Use src package.")


def main():
    """Main function to handle command-line arguments and run the application."""
    parser = argparse.ArgumentParser(description="Command-line Todo Application")
    subparsers = parser.add_subparsers(dest="command", help="Available commands")
    
    # Add command
    add_parser = subparsers.add_parser("add", help="Add a new task")
    add_parser.add_argument("description", type=str, help="Task description")
    
    # Delete command
    delete_parser = subparsers.add_parser("delete", help="Delete a task")
    delete_parser.add_argument("id", type=int, help="Task ID to delete")
    
    # Update command
    update_parser = subparsers.add_parser("update", help="Update a task")
    update_parser.add_argument("id", type=int, help="Task ID to update")
    update_parser.add_argument("description", type=str, help="New task description")
    
    # View command
    subparsers.add_parser("view", help="View all tasks")
    
    # Complete command
    complete_parser = subparsers.add_parser("complete", help="Mark a task as complete")
    complete_parser.add_argument("id", type=int, help="Task ID to mark complete")
    
    # Help command is handled by argparse
    
    args = parser.parse_args()
    
    # Create the todo application
    app = TodoApp()
    
    # Load any existing tasks from a file if needed
    # (For this implementation, tasks are stored in memory only)
    
    try:
        if args.command == "add":
            task = app.add_task(args.description)
            print(f"Added task #{task.id}: {task.description}")
        
        elif args.command == "delete":
            if app.delete_task(args.id):
                print(f"Deleted task #{args.id}")
            else:
                print(f"Error: Task #{args.id} not found")
        
        elif args.command == "update":
            if app.update_task(args.id, args.description):
                print(f"Updated task #{args.id} to: {args.description}")
            else:
                print(f"Error: Task #{args.id} not found")
        
        elif args.command == "view":
            tasks = app.view_tasks()
            if not tasks:
                print("No tasks found.")
            else:
                print("Todo List:")
                for task in tasks:
                    status = "✓" if task.completed else "○"
                    print(f"[{status}] #{task.id}: {task.description}")
        
        elif args.command == "complete":
            if app.mark_complete(args.id):
                print(f"Marked task #{args.id} as complete")
            else:
                print(f"Error: Task #{args.id} not found")
        
        elif args.command is None:
            parser.print_help()
        
        else:
            parser.print_help()
            
    except Exception as e:
        print(f"An error occurred: {e}")
        return 1
    
    return 0


if __name__ == "__main__":
    exit(main())