# Python Todo List

A simple command-line todo list application built with Python classes.

## Features

- ✅ Add new todos
- ✅ Mark todos as complete/incomplete
- ✅ Toggle todo status
- ✅ Remove todos
- ✅ List all todos with visual status indicators
- ✅ View statistics (total, completed, incomplete, completion rate)
- ✅ Clear completed todos
- ✅ Clear all todos
- ✅ Persistent storage (saves to JSON file)
- ✅ Interactive command-line interface

## Files

- `todo.py` - The Todo class for individual todo items
- `todolist.py` - The TodoList class for managing collections of todos
- `main.py` - Main application with interactive CLI
- `demo.py` - Demonstration script showing basic functionality

## Usage

### Interactive Mode
Run the main application for an interactive experience:
```bash
python3 main.py
```

### Demo Mode
Run the demo to see the functionality:
```bash
python3 demo.py
```

### Programming Interface
You can also use the classes directly in your own code:

```python
from todolist import TodoList

# Create a new todo list
my_todos = TodoList()

# Add todos
my_todos.add_todo("Learn Python")
my_todos.add_todo("Build an app")

# Mark as complete
my_todos.mark_complete(0)

# List todos
print(my_todos)

# Get statistics
stats = my_todos.get_statistics()
print(f"Completion rate: {stats['completion_rate']:.1f}%")
```

## Todo Class Methods

- `__init__(task, completed=False)` - Create a new todo
- `mark_complete()` - Mark as completed
- `mark_incomplete()` - Mark as incomplete
- `toggle_status()` - Toggle completion status
- `to_dict()` - Convert to dictionary for saving
- `from_dict(data)` - Create from dictionary (class method)

## TodoList Class Methods

- `add_todo(task)` - Add a new todo
- `remove_todo(index)` - Remove todo by index
- `mark_complete(index)` - Mark todo as complete by index
- `mark_incomplete(index)` - Mark todo as incomplete by index
- `toggle_todo(index)` - Toggle todo status by index
- `list_todos(show_completed=True)` - Get list of todos
- `get_statistics()` - Get completion statistics
- `clear_all()` - Remove all todos
- `clear_completed()` - Remove completed todos
- `save_to_file()` - Save to JSON file
- `load_from_file()` - Load from JSON file

## Data Persistence

Todos are automatically saved to `todos.json` in the current directory. The file is created automatically and updated whenever changes are made.

## Example Output

```
==================================================
           PYTHON TODO LIST
==================================================
1. Add a new todo
2. List all todos
3. Mark todo as complete
4. Mark todo as incomplete
5. Toggle todo status
6. Remove a todo
7. Show statistics
8. Clear completed todos
9. Clear all todos
0. Exit
==================================================

Your todos (3 total):
------------------------------
1. [✓] Learn Python basics
2. [✗] Build a todo app
3. [✗] Write documentation

📊 Todo Statistics:
--------------------
Total todos: 3
Completed: 1
Incomplete: 2
Completion rate: 33.3%
```