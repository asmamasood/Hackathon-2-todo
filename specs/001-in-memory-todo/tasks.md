# Tasks: In-Memory Todo CLI

**Input**: Design documents from `specs/001-in-memory-todo/`
**Prerequisites**: plan.md (required), spec.md (required for user stories), research.md, data-model.md, contracts/

## Phase 1: Setup (Shared Infrastructure)

**Purpose**: Project initialization and basic structure

- [X] T001 Create project structure per implementation plan (src/todo/, tests/)
- [X] T002 [P] Initialize Python project with UV and basic metadata
- [X] T003 [P] Configure pytest and basic linting tools

---

## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: Core infrastructure that MUST be complete before ANY user story can be implemented

**⚠️ CRITICAL**: No user story work can begin until this phase is complete

- [X] T004 Create foundational `Task` model in src/todo/domain/task.py
- [X] T005 Create base `TodoService` class and dictionary-based storage singleton in src/todo/services/todo_service.py
- [X] T006 [P] Implement base error handling and logging infrastructure in src/todo/lib/logging.py

**Checkpoint**: Foundation ready - user story implementation can now begin in parallel

---

## Phase 3: User Story 1 - Manage Basic Tasks (Priority: P1) 🎯 MVP

**Goal**: Enable core lifecycle of adding, viewing, and deleting tasks.

**Independent Test**: Add task "P1", view list, delete ID 1.

### Implementation for User Story 1

- [X] T007 [US1] Implement `addTask` functionality in src/todo/services/todo_service.py
- [X] T008 [US1] Implement `listTasks` functionality in src/todo/services/todo_service.py
- [X] T009 [US1] Implement `deleteTask` functionality in src/todo/services/todo_service.py
- [X] T010 [US1] Implement basic CLI commands (add, list, rm) in src/todo/cli.py and src/todo/__main__.py
- [X] T011 [P] [US1] Create unit tests for basic operations in tests/unit/test_todo_service.py
- [X] T012 [P] [US1] Create integration tests for CLI flows in tests/integration/test_cli_flows.py

**Checkpoint**: User Story 1 (MVP) is fully functional and testable independently.

---

## Phase 4: User Story 2 - Task Completion Status (Priority: P2)

**Goal**: Enable marking tasks as complete/incomplete.

**Independent Test**: Add task, run `done <id>`, view list to see "✔".

### Implementation for User Story 2

- [X] T013 [US2] Implement `toggleTask` functionality in src/todo/services/todo_service.py (based on ID)
- [X] T014 [US2] Update CLI list view to show status icons (✔ / ⏳) in src/todo/cli.py
- [X] T015 [US2] Add `done` command to CLI in src/todo/cli.py
- [X] T016 [P] [US2] Add unit tests for toggle logic in tests/unit/test_todo_service.py

**Checkpoint**: User Stories 1 AND 2 work independently.

---

## Phase 5: User Story 3 - Edit Task Details (Priority: P3)

**Goal**: Enable updating title and description of existing tasks.

**Independent Test**: Add task, run `edit <id> --title "New"`, view list to see update.

### Implementation for User Story 3

- [X] T017 [US3] Implement `updateTask` functionality in src/todo/services/todo_service.py
- [X] T018 [US3] Add `edit` command to CLI in src/todo/cli.py
- [X] T019 [P] [US3] Add unit tests for update logic in tests/unit/test_todo_service.py

---

## Phase N: Polish & Cross-Cutting Concerns

- [X] T020 [P] Update Quickstart documentation in specs/001-in-memory-todo/quickstart.md with final CLI syntax
- [X] T021 Manual verification of success criteria SC-001 through SC-005

---

## Dependencies & Execution Order

### Phase Dependencies
- **Setup (Phase 1)**: No dependencies.
- **Foundational (Phase 2)**: Depends on Setup.
- **User Stories (Phase 3+)**: All depend on Foundational completion.
  - US1 (P1) is the MVP and should be completed first.
  - US2 and US3 can proceed in parallel once US1 core service logic is stable.

## Implementation Strategy

### MVP First (User Story 1 Only)
1. Complete Phase 1: Setup
2. Complete Phase 2: Foundational (CRITICAL)
3. Complete Phase 3: User Story 1
4. **STOP and VALIDATE**: Test User Story 1 independently against Constitution Gate
5. Deploy/demo MVP
