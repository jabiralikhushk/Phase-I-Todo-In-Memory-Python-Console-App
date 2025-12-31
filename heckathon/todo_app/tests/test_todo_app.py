"""
Unit tests for the Todo Application.
Tests all 5 basic features: Add, Delete, Update, View, and Mark Complete.
"""

import datetime
import unittest
from todo_app import TodoApp, Task


class TestTodoApp(unittest.TestCase):
    """Test cases for the TodoApp class."""
    
    def setUp(self):
        """Set up a fresh TodoApp instance for each test."""
        self.app = TodoApp()
    
    def test_add_task(self):
        """Test adding a new task."""
        task = self.app.add_task("Test task")
        
        # Verify the task was added
        self.assertEqual(len(self.app.tasks), 1)
        self.assertEqual(task.id, 1)
        self.assertEqual(task.description, "Test task")
        self.assertFalse(task.completed)
        
        # Verify the next_id was incremented
        self.assertEqual(self.app.next_id, 2)
    
    def test_add_multiple_tasks(self):
        """Test adding multiple tasks with unique IDs."""
        task1 = self.app.add_task("First task")
        task2 = self.app.add_task("Second task")
        
        self.assertEqual(len(self.app.tasks), 2)
        self.assertEqual(task1.id, 1)
        self.assertEqual(task2.id, 2)
        self.assertEqual(task1.description, "First task")
        self.assertEqual(task2.description, "Second task")
    
    def test_view_tasks_empty(self):
        """Test viewing tasks when the list is empty."""
        tasks = self.app.view_tasks()
        
        self.assertEqual(tasks, [])
        self.assertEqual(len(tasks), 0)
    
    def test_view_tasks_with_items(self):
        """Test viewing tasks when the list has items."""
        self.app.add_task("First task")
        self.app.add_task("Second task")
        
        tasks = self.app.view_tasks()
        
        self.assertEqual(len(tasks), 2)
        self.assertEqual(tasks[0].description, "First task")
        self.assertEqual(tasks[1].description, "Second task")
    
    def test_update_task(self):
        """Test updating a task's description."""
        task = self.app.add_task("Original task")
        
        result = self.app.update_task(task.id, "Updated task")
        
        self.assertTrue(result)
        self.assertEqual(task.description, "Updated task")
    
    def test_update_nonexistent_task(self):
        """Test updating a task that doesn't exist."""
        result = self.app.update_task(999, "Updated task")
        
        self.assertFalse(result)
    
    def test_delete_task(self):
        """Test deleting a task."""
        task = self.app.add_task("Task to delete")
        initial_count = len(self.app.tasks)
        
        result = self.app.delete_task(task.id)
        
        self.assertTrue(result)
        self.assertEqual(len(self.app.tasks), initial_count - 1)
        
        # Verify the task is no longer in the list
        deleted_task = self.app.get_task_by_id(task.id)
        self.assertIsNone(deleted_task)
    
    def test_delete_nonexistent_task(self):
        """Test deleting a task that doesn't exist."""
        result = self.app.delete_task(999)
        
        self.assertFalse(result)
    
    def test_mark_complete(self):
        """Test marking a task as complete."""
        task = self.app.add_task("Task to complete")
        
        result = self.app.mark_complete(task.id)
        
        self.assertTrue(result)
        self.assertTrue(task.completed)
    
    def test_mark_nonexistent_task_complete(self):
        """Test marking a task as complete when it doesn't exist."""
        result = self.app.mark_complete(999)
        
        self.assertFalse(result)
    
    def test_get_task_by_id(self):
        """Test retrieving a task by its ID."""
        task = self.app.add_task("Test task")
        
        retrieved_task = self.app.get_task_by_id(task.id)
        
        self.assertEqual(retrieved_task, task)
        self.assertEqual(retrieved_task.id, task.id)
        self.assertEqual(retrieved_task.description, task.description)
    
    def test_get_nonexistent_task_by_id(self):
        """Test retrieving a task that doesn't exist."""
        retrieved_task = self.app.get_task_by_id(999)
        
        self.assertIsNone(retrieved_task)


class TestTask(unittest.TestCase):
    """Test cases for the Task class."""
    
    def test_task_initialization(self):
        """Test initializing a task with default values."""
        task = Task(1, "Test description")
        
        self.assertEqual(task.id, 1)
        self.assertEqual(task.description, "Test description")
        self.assertFalse(task.completed)
        self.assertIsNotNone(task.created_at)
        self.assertIsInstance(task.created_at, type(datetime.datetime.now()))
    
    def test_task_initialization_with_completed(self):
        """Test initializing a task with completed status."""
        task = Task(1, "Test description", completed=True)
        
        self.assertEqual(task.id, 1)
        self.assertEqual(task.description, "Test description")
        self.assertTrue(task.completed)
        self.assertIsNotNone(task.created_at)


if __name__ == "__main__":
    unittest.main()