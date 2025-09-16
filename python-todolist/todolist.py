#!/usr/bin/python3
"""
TodoList class for managing a collection of todos
"""
import json
import os
from todo import Todo


class TodoList:
    """A class to manage a collection of todos"""
    
    def __init__(self, filename="todos.json"):
        """
        Initialize the TodoList
        
        Args:
            filename (str): The file to save/load todos from
        """
        self.filename = filename
        self.todos = []
        self.load_from_file()
    
    def add_todo(self, task):
        """
        Add a new todo
        
        Args:
            task (str): The task description
        """
        todo = Todo(task)
        self.todos.append(todo)
        self.save_to_file()
        return todo
    
    def remove_todo(self, index):
        """
        Remove a todo by index
        
        Args:
            index (int): The index of the todo to remove
            
        Returns:
            bool: True if successful, False if index is invalid
        """
        if 0 <= index < len(self.todos):
            removed = self.todos.pop(index)
            self.save_to_file()
            return True
        return False
    
    def mark_complete(self, index):
        """
        Mark a todo as complete by index
        
        Args:
            index (int): The index of the todo to mark complete
            
        Returns:
            bool: True if successful, False if index is invalid
        """
        if 0 <= index < len(self.todos):
            self.todos[index].mark_complete()
            self.save_to_file()
            return True
        return False
    
    def mark_incomplete(self, index):
        """
        Mark a todo as incomplete by index
        
        Args:
            index (int): The index of the todo to mark incomplete
            
        Returns:
            bool: True if successful, False if index is invalid
        """
        if 0 <= index < len(self.todos):
            self.todos[index].mark_incomplete()
            self.save_to_file()
            return True
        return False
    
    def toggle_todo(self, index):
        """
        Toggle the completion status of a todo by index
        
        Args:
            index (int): The index of the todo to toggle
            
        Returns:
            bool: True if successful, False if index is invalid
        """
        if 0 <= index < len(self.todos):
            self.todos[index].toggle_status()
            self.save_to_file()
            return True
        return False
    
    def list_todos(self, show_completed=True):
        """
        Get a list of all todos
        
        Args:
            show_completed (bool): Whether to include completed todos
            
        Returns:
            list: List of todos
        """
        if show_completed:
            return self.todos
        return [todo for todo in self.todos if not todo.completed]
    
    def get_statistics(self):
        """
        Get statistics about the todos
        
        Returns:
            dict: Statistics about the todos
        """
        total = len(self.todos)
        completed = sum(1 for todo in self.todos if todo.completed)
        incomplete = total - completed
        
        return {
            'total': total,
            'completed': completed,
            'incomplete': incomplete,
            'completion_rate': (completed / total * 100) if total > 0 else 0
        }
    
    def save_to_file(self):
        """Save todos to file"""
        try:
            data = [todo.to_dict() for todo in self.todos]
            with open(self.filename, 'w') as f:
                json.dump(data, f, indent=2)
        except Exception as e:
            print(f"Error saving to file: {e}")
    
    def load_from_file(self):
        """Load todos from file"""
        if not os.path.exists(self.filename):
            return
        
        try:
            with open(self.filename, 'r') as f:
                data = json.load(f)
                self.todos = [Todo.from_dict(item) for item in data]
        except Exception as e:
            print(f"Error loading from file: {e}")
            self.todos = []
    
    def clear_all(self):
        """Clear all todos"""
        self.todos = []
        self.save_to_file()
    
    def clear_completed(self):
        """Remove all completed todos"""
        self.todos = [todo for todo in self.todos if not todo.completed]
        self.save_to_file()
    
    def __len__(self):
        """Return the number of todos"""
        return len(self.todos)
    
    def __str__(self):
        """String representation of the todo list"""
        if not self.todos:
            return "No todos yet!"
        
        result = []
        for i, todo in enumerate(self.todos):
            result.append(f"{i + 1}. {todo}")
        return "\n".join(result)