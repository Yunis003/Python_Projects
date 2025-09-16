#!/usr/bin/python3
"""
Test script for the Todo List functionality
"""
import sys
import os

# Add current directory to path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from todo import Todo
from todolist import TodoList


def test_todo_class():
    """Test the Todo class"""
    print("Testing Todo class...")
    
    # Test creation
    todo = Todo("Test task")
    assert todo.task == "Test task"
    assert todo.completed == False
    print("✓ Todo creation works")
    
    # Test completion
    todo.mark_complete()
    assert todo.completed == True
    print("✓ Mark complete works")
    
    todo.mark_incomplete()
    assert todo.completed == False
    print("✓ Mark incomplete works")
    
    # Test toggle
    todo.toggle_status()
    assert todo.completed == True
    todo.toggle_status()
    assert todo.completed == False
    print("✓ Toggle status works")
    
    # Test string representation
    expected_incomplete = "[✗] Test task"
    expected_complete = "[✓] Test task"
    assert str(todo) == expected_incomplete
    todo.mark_complete()
    assert str(todo) == expected_complete
    print("✓ String representation works")
    
    # Test serialization
    data = todo.to_dict()
    assert data['task'] == "Test task"
    assert data['completed'] == True
    
    new_todo = Todo.from_dict(data)
    assert new_todo.task == "Test task"
    assert new_todo.completed == True
    print("✓ Serialization works")


def test_todolist_class():
    """Test the TodoList class"""
    print("\nTesting TodoList class...")
    
    # Use a test filename
    test_file = "test_todos.json"
    todo_list = TodoList(test_file)
    
    # Test adding
    todo_list.add_todo("Task 1")
    todo_list.add_todo("Task 2")
    assert len(todo_list) == 2
    print("✓ Adding todos works")
    
    # Test marking complete
    result = todo_list.mark_complete(0)
    assert result == True
    assert todo_list.todos[0].completed == True
    print("✓ Mark complete by index works")
    
    # Test toggle
    result = todo_list.toggle_todo(1)
    assert result == True
    assert todo_list.todos[1].completed == True
    print("✓ Toggle by index works")
    
    # Test statistics
    stats = todo_list.get_statistics()
    assert stats['total'] == 2
    assert stats['completed'] == 2
    assert stats['incomplete'] == 0
    assert stats['completion_rate'] == 100.0
    print("✓ Statistics work")
    
    # Test removal
    result = todo_list.remove_todo(0)
    assert result == True
    assert len(todo_list) == 1
    print("✓ Remove by index works")
    
    # Test clear completed
    todo_list.add_todo("Task 3")
    todo_list.clear_completed()
    assert len(todo_list) == 1
    assert todo_list.todos[0].task == "Task 3"
    assert todo_list.todos[0].completed == False
    print("✓ Clear completed works")
    
    # Test clear all
    todo_list.clear_all()
    assert len(todo_list) == 0
    print("✓ Clear all works")
    
    # Clean up test file
    if os.path.exists(test_file):
        os.remove(test_file)


def test_edge_cases():
    """Test edge cases"""
    print("\nTesting edge cases...")
    
    todo_list = TodoList("edge_test.json")
    
    # Test operations on empty list
    assert todo_list.mark_complete(-1) == False
    assert todo_list.mark_complete(0) == False
    assert todo_list.remove_todo(0) == False
    print("✓ Empty list edge cases work")
    
    # Test invalid indices
    todo_list.add_todo("Task 1")
    assert todo_list.mark_complete(-1) == False
    assert todo_list.mark_complete(1) == False
    assert todo_list.remove_todo(-1) == False
    assert todo_list.remove_todo(1) == False
    print("✓ Invalid index edge cases work")
    
    # Clean up
    if os.path.exists("edge_test.json"):
        os.remove("edge_test.json")


def main():
    """Run all tests"""
    print("Running Todo List Tests...")
    print("=" * 40)
    
    try:
        test_todo_class()
        test_todolist_class()
        test_edge_cases()
        
        print("\n" + "=" * 40)
        print("✅ All tests passed successfully!")
        print("=" * 40)
        
    except AssertionError as e:
        print(f"\n❌ Test failed: {e}")
        sys.exit(1)
    except Exception as e:
        print(f"\n💥 Unexpected error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()