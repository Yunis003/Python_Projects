#!/usr/bin/python3
"""
Main application for the Todo List
"""
import sys
import os

# Add current directory to path to import our modules
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from todolist import TodoList


class TodoApp:
    """Command-line Todo List application"""
    
    def __init__(self):
        """Initialize the todo app"""
        self.todo_list = TodoList()
    
    def display_menu(self):
        """Display the main menu"""
        print("\n" + "="*50)
        print("           PYTHON TODO LIST")
        print("="*50)
        print("1. Add a new todo")
        print("2. List all todos")
        print("3. Mark todo as complete")
        print("4. Mark todo as incomplete") 
        print("5. Toggle todo status")
        print("6. Remove a todo")
        print("7. Show statistics")
        print("8. Clear completed todos")
        print("9. Clear all todos")
        print("0. Exit")
        print("="*50)
    
    def get_user_input(self, prompt):
        """Get user input with error handling"""
        try:
            return input(prompt).strip()
        except (KeyboardInterrupt, EOFError):
            print("\nGoodbye!")
            sys.exit(0)
    
    def get_todo_index(self, prompt="Enter todo number: "):
        """Get and validate todo index from user"""
        try:
            index = int(self.get_user_input(prompt)) - 1
            if 0 <= index < len(self.todo_list):
                return index
            else:
                print(f"Invalid todo number. Please enter a number between 1 and {len(self.todo_list)}")
                return None
        except ValueError:
            print("Please enter a valid number.")
            return None
    
    def add_todo(self):
        """Add a new todo"""
        task = self.get_user_input("Enter the task: ")
        if task:
            todo = self.todo_list.add_todo(task)
            print(f"✓ Added: {todo.task}")
        else:
            print("Task cannot be empty!")
    
    def list_todos(self):
        """List all todos"""
        if len(self.todo_list) == 0:
            print("No todos yet! Add some tasks to get started.")
        else:
            print(f"\nYour todos ({len(self.todo_list)} total):")
            print("-" * 30)
            print(self.todo_list)
    
    def mark_complete(self):
        """Mark a todo as complete"""
        if len(self.todo_list) == 0:
            print("No todos to mark complete!")
            return
        
        self.list_todos()
        index = self.get_todo_index("Enter todo number to mark complete: ")
        if index is not None:
            if self.todo_list.mark_complete(index):
                print(f"✓ Marked complete: {self.todo_list.todos[index].task}")
            else:
                print("Failed to mark todo as complete.")
    
    def mark_incomplete(self):
        """Mark a todo as incomplete"""
        if len(self.todo_list) == 0:
            print("No todos to mark incomplete!")
            return
        
        self.list_todos()
        index = self.get_todo_index("Enter todo number to mark incomplete: ")
        if index is not None:
            if self.todo_list.mark_incomplete(index):
                print(f"✓ Marked incomplete: {self.todo_list.todos[index].task}")
            else:
                print("Failed to mark todo as incomplete.")
    
    def toggle_todo(self):
        """Toggle todo status"""
        if len(self.todo_list) == 0:
            print("No todos to toggle!")
            return
        
        self.list_todos()
        index = self.get_todo_index("Enter todo number to toggle: ")
        if index is not None:
            if self.todo_list.toggle_todo(index):
                status = "complete" if self.todo_list.todos[index].completed else "incomplete"
                print(f"✓ Toggled to {status}: {self.todo_list.todos[index].task}")
            else:
                print("Failed to toggle todo status.")
    
    def remove_todo(self):
        """Remove a todo"""
        if len(self.todo_list) == 0:
            print("No todos to remove!")
            return
        
        self.list_todos()
        index = self.get_todo_index("Enter todo number to remove: ")
        if index is not None:
            task = self.todo_list.todos[index].task
            if self.todo_list.remove_todo(index):
                print(f"✓ Removed: {task}")
            else:
                print("Failed to remove todo.")
    
    def show_statistics(self):
        """Show todo statistics"""
        stats = self.todo_list.get_statistics()
        print("\n📊 Todo Statistics:")
        print("-" * 20)
        print(f"Total todos: {stats['total']}")
        print(f"Completed: {stats['completed']}")
        print(f"Incomplete: {stats['incomplete']}")
        print(f"Completion rate: {stats['completion_rate']:.1f}%")
    
    def clear_completed(self):
        """Clear completed todos"""
        stats = self.todo_list.get_statistics()
        if stats['completed'] == 0:
            print("No completed todos to clear!")
            return
        
        confirm = self.get_user_input(f"Clear {stats['completed']} completed todos? (y/N): ")
        if confirm.lower() in ['y', 'yes']:
            self.todo_list.clear_completed()
            print("✓ Cleared completed todos!")
        else:
            print("Operation cancelled.")
    
    def clear_all(self):
        """Clear all todos"""
        if len(self.todo_list) == 0:
            print("No todos to clear!")
            return
        
        confirm = self.get_user_input(f"Clear all {len(self.todo_list)} todos? (y/N): ")
        if confirm.lower() in ['y', 'yes']:
            self.todo_list.clear_all()
            print("✓ Cleared all todos!")
        else:
            print("Operation cancelled.")
    
    def run(self):
        """Main application loop"""
        print("Welcome to Python Todo List!")
        
        while True:
            self.display_menu()
            choice = self.get_user_input("Choose an option (0-9): ")
            
            if choice == "1":
                self.add_todo()
            elif choice == "2":
                self.list_todos()
            elif choice == "3":
                self.mark_complete()
            elif choice == "4":
                self.mark_incomplete()
            elif choice == "5":
                self.toggle_todo()
            elif choice == "6":
                self.remove_todo()
            elif choice == "7":
                self.show_statistics()
            elif choice == "8":
                self.clear_completed()
            elif choice == "9":
                self.clear_all()
            elif choice == "0":
                print("\nThank you for using Python Todo List!")
                break
            else:
                print("Invalid choice. Please enter a number between 0-9.")


def main():
    """Main function"""
    app = TodoApp()
    app.run()


if __name__ == "__main__":
    main()