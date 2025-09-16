#!/usr/bin/python3
"""
Simple demonstration of the Todo List functionality
"""
import sys
import os

# Add current directory to path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from todo import Todo
from todolist import TodoList


def demo_basic_usage():
    """Demonstrate basic usage of the Todo classes"""
    print("=== Todo List Demo ===\n")
    
    # Create a new todo list
    print("1. Creating a new Todo List...")
    my_todos = TodoList("demo_todos.json")
    
    # Add some todos
    print("\n2. Adding some todos...")
    my_todos.add_todo("Learn Python basics")
    my_todos.add_todo("Build a todo app")
    my_todos.add_todo("Write documentation")
    my_todos.add_todo("Test the application")
    
    # List all todos
    print("\n3. Current todos:")
    print(my_todos)
    
    # Mark some as complete
    print("\n4. Marking first todo as complete...")
    my_todos.mark_complete(0)
    print(my_todos)
    
    # Toggle a todo
    print("\n5. Toggling second todo status...")
    my_todos.toggle_todo(1)
    print(my_todos)
    
    # Show statistics
    print("\n6. Statistics:")
    stats = my_todos.get_statistics()
    print(f"Total: {stats['total']}")
    print(f"Completed: {stats['completed']}")
    print(f"Incomplete: {stats['incomplete']}")
    print(f"Completion rate: {stats['completion_rate']:.1f}%")
    
    # Remove a todo
    print("\n7. Removing the last todo...")
    my_todos.remove_todo(3)
    print(my_todos)
    
    print(f"\n8. Final count: {len(my_todos)} todos")
    
    # Clean up demo file
    if os.path.exists("demo_todos.json"):
        os.remove("demo_todos.json")
    
    print("\n=== Demo Complete ===")


def demo_individual_todo():
    """Demonstrate individual Todo functionality"""
    print("\n=== Individual Todo Demo ===\n")
    
    # Create individual todos
    todo1 = Todo("Read a book")
    todo2 = Todo("Exercise", completed=True)
    
    print("Created todos:")
    print(f"Todo 1: {todo1}")
    print(f"Todo 2: {todo2}")
    
    # Test methods
    print("\nTesting methods:")
    todo1.mark_complete()
    print(f"After marking complete: {todo1}")
    
    todo2.toggle_status()
    print(f"After toggling: {todo2}")
    
    # Test serialization
    print(f"\nSerialization test:")
    print(f"Todo1 dict: {todo1.to_dict()}")
    todo3 = Todo.from_dict({"task": "New task", "completed": False})
    print(f"Todo from dict: {todo3}")


if __name__ == "__main__":
    demo_individual_todo()
    demo_basic_usage()