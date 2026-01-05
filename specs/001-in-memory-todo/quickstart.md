# Quickstart: In-Memory Todo CLI

## Environment Setup
1. Ensure Python 3.13+ is installed.
2. Install `uv`: `pip install uv` (if not already present).
3. Initialize environment: `uv sync`

## Running the App
Execute the following from the project root:
```bash
python -m todo <command> [args]
```

**Note on Persistence**: Since Phase I uses in-memory storage only, state is lost when the command finishes. To preserve state across multiple commands for demonstration purposes, use the **Interactive Mode**.

## Interactive Mode (Recommended for Demo)
To enter a session where tasks persist across commands:
```bash
python -m todo interactive
```
Within the session, type your commands (e.g., `add "Buy Milk"`) and type `exit` to quit.

## Example Commands
- **Add**: `python -m todo add "Buy Groceries" -d "Milk, Eggs, Bread"`
- **List**: `python -m todo list`
- **Complete**: `python -m todo done 1`
- **Delete**: `python -m todo rm 1`
