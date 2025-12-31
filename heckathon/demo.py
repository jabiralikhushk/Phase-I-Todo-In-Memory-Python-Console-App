"""
Interactive Todo Application Demonstration
Shows all features of the todo app in action.
"""

from src.todo import TodoApp


def main():
    """Run interactive demonstration of the todo app."""
    app = TodoApp()
    
    print("=" * 70)
    print("📋 Todo Application - Phase I Demonstration")
    print("=" * 70)
    
    # Feature 1: Add Tasks
    print("\n✓ FEATURE 1: Adding Tasks")
    print("-" * 70)
    
    task1 = app.add_task("Buy groceries", "Milk, eggs, bread, butter")
    print(f"  Added task #{task1.id}: {task1.title}")
    print(f"  Description: {task1.description}")
    
    task2 = app.add_task("Walk the dog", "30 minutes in the park")
    print(f"  Added task #{task2.id}: {task2.title}")
    print(f"  Description: {task2.description}")
    
    task3 = app.add_task("Complete project")
    print(f"  Added task #{task3.id}: {task3.title}")
    
    task4 = app.add_task("Review code", "Check all pull requests")
    print(f"  Added task #{task4.id}: {task4.title}")
    print(f"  Description: {task4.description}")
    
    # Feature 2: View Tasks
    print("\n✓ FEATURE 2: Viewing All Tasks")
    print("-" * 70)
    tasks = app.view_tasks()
    print(f"\n📋 Todo List ({len(tasks)} tasks):")
    print("=" * 70)
    for task in tasks:
        status = "✓" if task.completed else "○"
        print(f"[{status}] #{task.id}: {task.title}")
        if task.description:
            print(f"     └─ {task.description}")
    print("=" * 70)
    
    # Feature 3: Mark Complete
    print("\n✓ FEATURE 3: Marking Tasks as Complete")
    print("-" * 70)
    success = app.mark_complete(1)
    print(f"  Marked task #1 as complete: {success}")
    
    success = app.mark_complete(3)
    print(f"  Marked task #3 as complete: {success}")
    
    print(f"\n📋 Updated Todo List:")
    print("=" * 70)
    for task in app.view_tasks():
        status = "✓" if task.completed else "○"
        print(f"[{status}] #{task.id}: {task.title}")
        if task.description:
            print(f"     └─ {task.description}")
    print("=" * 70)
    
    # Feature 4: Update Task
    print("\n✓ FEATURE 4: Updating Task Details")
    print("-" * 70)
    original_task = app.get_task_by_id(2)
    print(f"  Original task #2: {original_task.title}")
    
    success = app.update_task(2, "Walk the dog (extended)", "45 minutes in the park")
    print(f"  Updated task #2: {success}")
    
    updated_task = app.get_task_by_id(2)
    print(f"  New title: {updated_task.title}")
    print(f"  New description: {updated_task.description}")
    
    print(f"\n📋 Todo List after update:")
    print("=" * 70)
    for task in app.view_tasks():
        status = "✓" if task.completed else "○"
        print(f"[{status}] #{task.id}: {task.title}")
        if task.description:
            print(f"     └─ {task.description}")
    print("=" * 70)
    
    # Feature 5: Delete Task
    print("\n✓ FEATURE 5: Deleting Tasks")
    print("-" * 70)
    success = app.delete_task(4)
    print(f"  Deleted task #4: {success}")
    
    print(f"\n📋 Final Todo List ({len(app.view_tasks())} tasks):")
    print("=" * 70)
    for task in app.view_tasks():
        status = "✓" if task.completed else "○"
        print(f"[{status}] #{task.id}: {task.title}")
        if task.description:
            print(f"     └─ {task.description}")
    print("=" * 70)
    
    # Summary
    print("\n" + "=" * 70)
    print("✅ All Features Demonstrated Successfully!")
    print("=" * 70)
    print("\nFeatures Implemented:")
    print("  ✓ Add tasks with title and optional description")
    print("  ✓ View all tasks with status indicators")
    print("  ✓ Mark tasks as complete/incomplete")
    print("  ✓ Update task title and description")
    print("  ✓ Delete tasks by ID")
    print("\nNote: Tasks are stored in memory. Restart to clear.")
    print("=" * 70 + "\n")


if __name__ == "__main__":
    main()
