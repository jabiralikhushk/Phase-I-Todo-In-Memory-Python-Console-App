"""
Menu-driven Todo Application CLI

Runs an interactive menu so you can add/list/update/delete/complete tasks
within a single process (state persists while the program runs).
"""

from __future__ import annotations
from .todo import TodoApp


def print_menu() -> None:
    print("===== TODO APPLICATION =====")
    print("1. Add Task")
    print("2. List Tasks")
    print("3. Update Task")
    print("4. Delete Task")
    print("5. Mark Task Complete")
    print("6. Mark Task Incomplete")
    print("7. Exit")


def prompt(prompt_text: str) -> str:
    try:
        return input(prompt_text)
    except EOFError:
        return ""


def run_menu() -> int:
    app = TodoApp()

    while True:
        print()
        print_menu()
        choice = prompt("Enter your choice (1-7): ").strip()
        if not choice:
            continue

        if choice == "1":
            print("---Add New Task---")
            title = prompt("Title: ").strip()
            if not title:
                print("✗ Title cannot be empty.")
                continue
            desc = prompt("Description (optional): ").strip()
            task = app.add_task(title, desc)
            print(f"✓ Added task #{task.id}: {task.title}")

        elif choice == "2":
            print("---Task List---")
            tasks = app.view_tasks()
            if not tasks:
                print("No tasks found.")
            else:
                for t in tasks:
                    status = "✓" if t.completed else "○"
                    print(f"[{status}] #{t.id}: {t.title}")
                    if t.description:
                        print(f"    └─ {t.description}")

        elif choice == "3":
            print("---Update Task---")
            tid = prompt("Task ID: ").strip()
            if not tid.isdigit():
                print("✗ Invalid ID.")
                continue
            tidn = int(tid)
            new_title = prompt("New title (leave empty to keep): ").strip()
            new_desc = prompt("New description (leave empty to keep): ").strip()
            title_arg = new_title if new_title else None
            desc_arg = new_desc if new_desc else None
            if app.update_task(tidn, title=title_arg, description=desc_arg):
                print(f"✓ Updated task #{tidn}")
            else:
                print(f"✗ Task #{tidn} not found")

        elif choice == "4":
            print("---Delete Task---")
            tid = prompt("Task ID: ").strip()
            if not tid.isdigit():
                print("✗ Invalid ID.")
                continue
            if app.delete_task(int(tid)):
                print(f"✓ Deleted task #{tid}")
            else:
                print(f"✗ Task #{tid} not found")

        elif choice == "5":
            print("---Mark Complete---")
            tid = prompt("Task ID: ").strip()
            if not tid.isdigit():
                print("✗ Invalid ID.")
                continue
            if app.mark_complete(int(tid)):
                print(f"✓ Marked task #{tid} as complete")
            else:
                print(f"✗ Task #{tid} not found")

        elif choice == "6":
            print("---Mark Incomplete---")
            tid = prompt("Task ID: ").strip()
            if not tid.isdigit():
                print("✗ Invalid ID.")
                continue
            task = app.get_task_by_id(int(tid))
            if task:
                task.completed = False
                print(f"✓ Marked task #{tid} as incomplete")
            else:
                print(f"✗ Task #{tid} not found")

        elif choice == "7":
            print("Exiting. Goodbye!")
            return 0

        else:
            print("✗ Invalid choice. Please enter 1-7.")


if __name__ == "__main__":
    run_menu()
