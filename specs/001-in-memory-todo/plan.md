# Implementation Plan: In-Memory Todo CLI

**Branch**: `001-in-memory-todo` | **Date**: 2026-01-02 | **Spec**: [specs/001-in-memory-todo/spec.md](specs/001-in-memory-todo/spec.md)
**Input**: Feature specification from `specs/001-in-memory-todo/spec.md`

## Summary
Build a modular Python CLI application using in-memory storage to manage tasks. The implementation separates the CLI handler from the business logic layer using Clean Architecture patterns.

## Technical Context
**Language/Version**: Python 3.13+
**Primary Dependencies**: None (Standard Library only)
**Storage**: In-memory (Single Project instance)
**Testing**: pytest
**Target Platform**: CLI
**Project Type**: Single project
**Performance Goals**: Sub-second startup and command execution
**Constraints**: No persistence, no external frameworks

## Constitution Check
*GATE: Must pass before Phase 0 research. Re-check after Phase 1 design.*

- [x] **AI-Native**: Implementation uses Claude Code; no manual human coding.
- [x] **Spec-Driven**: Changes trace back to `spec.md`; workflow follows Spec -> Plan -> Tasks.
- [x] **Architectural Integrity**: Approach aligns with the Evolution of Todo Master Constitution (Phase I-V).
- [x] **Forbidden Actions**: No manual code writing or unvetted external boilerplate.

## Project Structure

### Documentation (this feature)
```text
specs/001-in-memory-todo/
├── plan.md              # This file
├── research.md          # Technical decisions and rationale
├── data-model.md        # Task entity definition
├── quickstart.md        # Usage examples
├── contracts/
│   └── service_interface.md # Domain service API
└── tasks.md             # Implementation tasks
```

### Source Code (repository root)
```text
src/
├── todo/
│   ├── __init__.py
│   ├── __main__.py      # CLI Entry point
│   ├── cli.py           # Command parsing and display logic
│   ├── domain/
│   │   ├── __init__.py
│   │   └── task.py      # Data model
│   └── services/
│       ├── __init__.py
│       └── todo_service.py # Core business logic
tests/
├── integration/
│   └── test_cli_flows.py
└── unit/
    └── test_todo_service.py
```

**Structure Decision**: Option 1 (Single Project) with domain/service separation.

## Application Flow
1. **CLI Layer (`__main__.py` / `cli.py`)**: Parses arguments, delegates to `TodoService`.
2. **Service Layer (`todo_service.py`)**: Validates input, manages the in-memory collection of `Task` objects.
3. **Domain Layer (`task.py`)**: Defines the data structure.

## Module Responsibilities
- `cli.py`: Formats table output, handles user interaction.
- `todo_service.py`: Singleton-like manager for ID generation and task operations.
- `task.py`: Pure data class representing the state.
