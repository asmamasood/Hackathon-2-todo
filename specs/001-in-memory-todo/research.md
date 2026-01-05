# Research: In-Memory Todo CLI App

**Feature**: 001-in-memory-todo

## Phase 0: Research Decisions

### Decision: Python 3.13+ with UV
- **Rationale**: Python 3.13 provides modern features and performance. UV is used for high-speed dependency and environment management, aligning with the "Agentic Dev Stack" principle.
- **Alternatives considered**: Standard `venv` (rejected as slower/less agent-friendly than UV).

### Decision: Clean Architecture (Domain Driven)
- **Rationale**: Separating the `domain` (Task model) from `services` (business logic) and `cli` (delivery mechanism) ensures modularity and testability. This supports the "Architectural Integrity" requirement for future cloud-native evolution.
- **Alternatives considered**: Simple monolith (rejected as hard to evolve).

### Decision: In-Memory Storage (Dictionary-based)
- **Rationale**: Strict constraint of Phase I. Using a simple dictionary within a singleton or service class allows for P1/P2/P3 functional compliance without the complexity of a database.
- **Persistence Note**: Since storage is in-memory only, data is lost when the Python process exits. This is by design for Phase I.
- **Alternatives considered**: File-based storage (explicitly forbidden).

### Decision: Interactive Mode for Demonstration
- **Rationale**: To mitigate the volatility of in-memory storage during manual testing and demonstrations, an `interactive` command was added. This allows multiple commands to be executed within a single process lifecycle, preserving state.
- **Alternatives considered**: Chained bash commands (too complex for users).

### Decision: Atomic CLI Input Handling
- **Rationale**: Since no external frameworks (like Click or Typer) are allowed in Phase I, `argparse` or manual `sys.argv` parsing will be used to maintain modularity.
- **Alternatives considered**: Interactive prompt loop (argparse preferred for CLI tool standards).
