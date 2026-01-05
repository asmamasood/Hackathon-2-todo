import argparse
import sys
from todo.services.todo_service import TodoService

def main():
    parser = argparse.ArgumentParser(description="Todo CLI Application")
    subparsers = parser.add_subparsers(dest="command", help="Available commands")

    # Add command
    add_parser = subparsers.add_parser("add", help="Add a new task")
    add_parser.add_argument("title", help="Task title")
    add_parser.add_argument("-d", "--description", default="", help="Task description")

    # List command
    subparsers.add_parser("list", help="List all tasks")

    # Remove command
    rm_parser = subparsers.add_parser("rm", help="Remove a task")
    rm_parser.add_argument("id", type=int, help="Task ID")

    # Done command
    done_parser = subparsers.add_parser("done", help="Toggle task completion status")
    done_parser.add_argument("id", type=int, help="Task ID")

    # Edit command
    edit_parser = subparsers.add_parser("edit", help="Edit a task")
    edit_parser.add_argument("id", type=int, help="Task ID")
    edit_parser.add_argument("-t", "--title", help="New title")
    edit_parser.add_argument("-d", "--description", help="New description")

    # Interactive command (demo mode)
    subparsers.add_parser("interactive", help="Start interactive session")

    args = parser.parse_args()
    service = TodoService()

    def handle_command(args, service, parser):
        if args.command == "add":
            task = service.add_task(args.title, args.description)
            print(f"Task added with ID: {task.id}")

        elif args.command == "list":
            tasks = service.list_tasks()
            if not tasks:
                print("No tasks found.")
                return

            print(f"{'ID':<4} {'Status':<8} {'Title':<20} {'Description'}")
            print("-" * 50)
            for task in tasks:
                status = "✔" if task.is_completed else "⏳"
                print(f"{task.id:<4} {status:<8} {task.title:<20} {task.description}")

        elif args.command == "rm":
            if service.delete_task(args.id):
                print(f"Task {args.id} deleted.")
            else:
                print(f"Error: Task {args.id} not found.")

        elif args.command == "done":
            task = service.toggle_task(args.id)
            if task:
                status = "completed" if task.is_completed else "incomplete"
                print(f"Task {args.id} marked as {status}.")
            else:
                print(f"Error: Task {args.id} not found.")

        elif args.command == "edit":
            try:
                task = service.update_task(args.id, title=args.title, description=args.description)
                if task:
                    print(f"Task {args.id} updated.")
                else:
                    print(f"Error: Task {args.id} not found.")
            except ValueError as e:
                print(f"Error: {e}")

        elif args.command == "interactive":
            print("Entering interactive mode. Type 'exit' to quit.")
            while True:
                try:
                    line = input("todo> ").strip()
                    if not line:
                        continue
                    if line.lower() in ("exit", "quit"):
                        break

                    # Parse the sub-command
                    sub_args = parser.parse_args(line.split())
                    handle_command(sub_args, service, parser)
                except EOFError:
                    break
                except SystemExit:
                    # Argparse will try to exit on --help or error; catch it
                    continue
                except Exception as e:
                    print(f"Error: {e}")

        else:
            parser.print_help()

    handle_command(args, service, parser)

if __name__ == "__main__":
    main()
