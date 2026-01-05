# Data Model: In-Memory Todo
**Status**: Approved

## Entities

### Task
Represents a single todo item in the system.

| Field | Type | Description | Validation |
|-------|------|-------------|------------|
| `id` | `int` | Unique identifier (internal counter) | MUST be unique, system-generated |
| `title` | `str` | Short name of the task | MUST NOT be empty, max 100 chars |
| `description` | `str` | Optional detailed description | Optional, can be empty string |
| `is_completed`| `bool` | Completion status | Defaults to `False` |

## State Transitions
- **Pending (⏳)**: Default state upon creation.
- **Complete (✔)**: Achievement of task goal.
- `Pending` <--> `Complete` (Bidirectional toggle)
