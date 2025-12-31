"""
Todo Application Core Classes
Implements Task and TodoApp classes for the todo application.
"""

import datetime
from typing import List, Optional


class Task:
    """Represents a single task in the todo application."""
    
    def __init__(self, task_id: int, title: str, description: str = "", completed: bool = False):
        """
        Initialize a new task.
        
        Args:
            task_id (int): Unique identifier for the task
            title (str): Title of the task
            description (str): Detailed description of the task (optional)
            completed (bool): Whether the task is completed (default: False)
        """
        self.id = task_id
        self.title = title
        self.description = description
        self.completed = completed
        self.created_at = datetime.datetime.now()


class TodoApp:
    """Main application class for the todo application."""
    
    def __init__(self):
        """Initialize the todo application."""
        self.tasks = []
        self.next_id = 1
    
    def add_task(self, title: str, description: str = "") -> Task:
        """
        Add a new task to the application.
        
        Args:
            title (str): Title of the task to add
            description (str): Detailed description of the task (optional)
            
        Returns:
            Task: The newly created task
        """
        task = Task(self.next_id, title, description)
        self.tasks.append(task)
        self.next_id += 1
        return task
    
    def view_tasks(self) -> List[Task]:
        """
        Get all tasks in the application.
        
        Returns:
            List[Task]: List of all tasks
        """
        return self.tasks
    
    def update_task(self, task_id: int, title: str = None, description: str = None) -> bool:
        """
        Update a task's title and/or description.
        
        Args:
            task_id (int): ID of the task to update
            title (str): New title for the task (optional)
            description (str): New description for the task (optional)
            
        Returns:
            bool: True if task was updated, False if task not found
        """
        for task in self.tasks:
            if task.id == task_id:
                if title is not None:
                    task.title = title
                if description is not None:
                    task.description = description
                return True
        return False
    
    def delete_task(self, task_id: int) -> bool:
        """
        Delete a task from the application.
        
        Args:
            task_id (int): ID of the task to delete
            
        Returns:
            bool: True if task was deleted, False if task not found
        """
        for i, task in enumerate(self.tasks):
            if task.id == task_id:
                del self.tasks[i]
                return True
        return False
    
    def mark_complete(self, task_id: int) -> bool:
        """
        Mark a task as complete.
        
        Args:
            task_id (int): ID of the task to mark as complete
            
        Returns:
            bool: True if task was marked complete, False if task not found
        """
        for task in self.tasks:
            if task.id == task_id:
                task.completed = True
                return True
        return False
    
    def get_task_by_id(self, task_id: int) -> Optional[Task]:
        """
        Get a task by its ID.
        
        Args:
            task_id (int): ID of the task to retrieve
            
        Returns:
            Task or None: The task if found, None otherwise
        """
        for task in self.tasks:
            if task.id == task_id:
                return task
        return None
