from todo.services.todo_service import TodoService
import logging

# Disable logging for cleaner interactive output
logging.getLogger("todo").setLevel(logging.WARNING)

def display_tasks(service):
    """Display all tasks in a formatted table."""
    tasks = service.list_tasks()
    if not tasks:
        print("\nNo tasks found.")
        return

    print("\n" + "=" * 70)
    print(f"{'ID':<5} {'Status':<10} {'Title':<25} {'Description':<30}")
    print("=" * 70)
    for task in tasks:
        status = "DONE" if task.is_completed else "TODO"
        title = task.title[:24] if len(task.title) > 24 else task.title
        desc = task.description[:29] if len(task.description) > 29 else task.description
        print(f"{task.id:<5} {status:<10} {title:<25} {desc:<30}")
    print("=" * 70)

def add_task_interactive(service):
    """Add a new task interactively."""
    print("\n--- Add New Task ---")
    title = input("Enter task title: ").strip()
    if not title:
        print("Error: Title cannot be empty.")
        return

    description = input("Enter task description (optional): ").strip()
    task = service.add_task(title, description)
    print(f"[OK] Task added successfully with ID: {task.id}")

def delete_task_interactive(service):
    """Delete a task by ID."""
    print("\n--- Delete Task ---")
    try:
        task_id = int(input("Enter task ID to delete: ").strip())
        if service.delete_task(task_id):
            print(f"[OK] Task {task_id} deleted successfully.")
        else:
            print(f"[ERROR] Task {task_id} not found.")
    except ValueError:
        print("[ERROR] Invalid ID. Please enter a number.")

def update_task_interactive(service):
    """Update a task's title, description, or toggle completion."""
    print("\n--- Update Task ---")
    try:
        task_id = int(input("Enter task ID to update: ").strip())
        task = service.get_task(task_id)
        if not task:
            print(f"[ERROR] Task {task_id} not found.")
            return

        print(f"\nCurrent task: {task.title}")
        print(f"Description: {task.description}")
        print(f"Status: {'DONE' if task.is_completed else 'TODO'}")

        print("\nWhat would you like to update?")
        print("  1 - Update title")
        print("  2 - Update description")
        print("  3 - Toggle completion status")
        print("  4 - Cancel")

        choice = input("Choose an option (1-4): ").strip()

        if choice == "1":
            new_title = input("Enter new title: ").strip()
            if new_title:
                service.update_task(task_id, title=new_title)
                print("[OK] Title updated successfully.")
            else:
                print("[ERROR] Title cannot be empty.")

        elif choice == "2":
            new_desc = input("Enter new description: ").strip()
            service.update_task(task_id, description=new_desc)
            print("[OK] Description updated successfully.")

        elif choice == "3":
            service.toggle_task(task_id)
            new_status = "DONE" if service.get_task(task_id).is_completed else "TODO"
            print(f"[OK] Task status toggled to: {new_status}")

        elif choice == "4":
            print("Update cancelled.")

        else:
            print("[ERROR] Invalid choice.")

    except ValueError:
        print("[ERROR] Invalid ID. Please enter a number.")

def show_menu():
    """Display the main menu."""
    print("\n" + "=" * 70)
    print("MENU OPTIONS")
    print("=" * 70)
    print("  1 - Add a new task")
    print("  2 - Delete a task by ID")
    print("  3 - List all tasks")
    print("  4 - Update a task (title/description/toggle completion)")
    print("  5 - Show final task status and EXIT")
    print("=" * 70)

def main():
    service = TodoService()

    # Welcome message
    print("\n" + "=" * 70)
    print("=== Welcome to In-Memory Todo CLI ===")
    print("=" * 70)

    # Display current task list
    display_tasks(service)

    # Main menu loop
    while True:
        show_menu()
        choice = input("\nEnter your choice (1-5): ").strip()

        if choice == "1":
            add_task_interactive(service)

        elif choice == "2":
            delete_task_interactive(service)

        elif choice == "3":
            display_tasks(service)

        elif choice == "4":
            update_task_interactive(service)

        elif choice == "5":
            print("\n--- Final Task Status ---")
            display_tasks(service)
            print("\nThank you for using In-Memory Todo CLI! Goodbye.")
            break

        else:
            print("[ERROR] Invalid choice. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main()
