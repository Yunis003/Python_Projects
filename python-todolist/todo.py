#!/usr/bin/python3
"""
Todo class for managing individual todo items
"""

class Todo:
    """A simple Todo item class"""
    
    def __init__(self, task, completed=False):
        """
        Initialize a Todo item
        
        Args:
            task (str): The task description
            completed (bool): Whether the task is completed
        """
        self.task = task
        self.completed = completed
    
    def mark_complete(self):
        """Mark the todo as completed"""
        self.completed = True
    
    def mark_incomplete(self):
        """Mark the todo as incomplete"""
        self.completed = False
    
    def toggle_status(self):
        """Toggle the completion status"""
        self.completed = not self.completed
    
    def __str__(self):
        """String representation of the todo"""
        status = "✓" if self.completed else "✗"
        return f"[{status}] {self.task}"
    
    def __repr__(self):
        """Developer representation of the todo"""
        return f"Todo(task='{self.task}', completed={self.completed})"
    
    def to_dict(self):
        """Convert todo to dictionary for serialization"""
        return {
            'task': self.task,
            'completed': self.completed
        }
    
    @classmethod
    def from_dict(cls, data):
        """Create Todo from dictionary"""
        return cls(data['task'], data['completed'])