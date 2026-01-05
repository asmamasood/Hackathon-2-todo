# Service Interface: TodoService

This document defines the atomic operations provided by the domain service layer.

## Operations

### addTask(title: str, description: str = "") -> int
- **Input**: Title (required), Description (optional).
- **Return**: New unique Task ID.
- **Constraints**: Title must be validated.

### listTasks() -> List[Task]
- **Return**: All tasks currently in memory.

### updateTask(id: int, title: str = None, description: str = None) -> bool
- **Input**: Task ID, optional new title and/or description.
- **Return**: Success status.

### deleteTask(id: int) -> bool
- **Input**: Task ID.
- **Return**: Success status.

### toggleTask(id: int) -> bool
- **Input**: Task ID.
- **Return**: New completion status.
