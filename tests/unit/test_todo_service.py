import pytest
from todo.services.todo_service import TodoService

@pytest.fixture
def service():
    # Reset singleton for each test
    TodoService._instance = None
    return TodoService()

def test_add_task(service):
    task = service.add_task("Test Task", "Test Description")
    assert task.id == 1
    assert task.title == "Test Task"
    assert task.description == "Test Description"
    assert not task.is_completed

def test_add_task_empty_title(service):
    with pytest.raises(ValueError, match="Title cannot be empty"):
        service.add_task("")

def test_list_tasks(service):
    service.add_task("Task 1")
    service.add_task("Task 2")
    tasks = service.list_tasks()
    assert len(tasks) == 2
    assert tasks[0].title == "Task 1"
    assert tasks[1].title == "Task 2"

def test_delete_task(service):
    service.add_task("To Delete")
    assert service.delete_task(1) is True
    assert len(service.list_tasks()) == 0

def test_delete_nonexistent_task(service):
    assert service.delete_task(999) is False

def test_toggle_task(service):
    service.add_task("Toggle Me")
    task = service.toggle_task(1)
    assert task.is_completed is True
    task = service.toggle_task(1)
    assert task.is_completed is False

def test_update_task(service):
    service.add_task("Original Title", "Original Desc")
    task = service.update_task(1, title="New Title", description="New Desc")
    assert task.title == "New Title"
    assert task.description == "New Desc"

def test_update_task_partial(service):
    service.add_task("Original Title", "Original Desc")
    task = service.update_task(1, title="New Title")
    assert task.title == "New Title"
    assert task.description == "Original Desc"
