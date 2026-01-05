from typing import Dict, List, Optional
from todo.domain.task import Task
from todo.lib.logging import logger

class TodoService:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(TodoService, cls).__new__(cls)
            cls._instance._tasks: Dict[int, Task] = {}
            cls._instance._next_id = 1
        return cls._instance

    def add_task(self, title: str, description: str = "") -> Task:
        if not title:
            raise ValueError("Title cannot be empty")

        task = Task(id=self._next_id, title=title, description=description)
        self._tasks[self._next_id] = task
        self._next_id += 1
        logger.info(f"Added task {task.id}: {task.title}")
        return task

    def list_tasks(self) -> List[Task]:
        return list(self._tasks.values())

    def get_task(self, task_id: int) -> Optional[Task]:
        return self._tasks.get(task_id)

    def delete_task(self, task_id: int) -> bool:
        if task_id in self._tasks:
            del self._tasks[task_id]
            logger.info(f"Deleted task {task_id}")
            return True
        return False

    def toggle_task(self, task_id: int) -> Optional[Task]:
        task = self.get_task(task_id)
        if task:
            task.is_completed = not task.is_completed
            logger.info(f"Toggled task {task_id} to {'completed' if task.is_completed else 'incomplete'}")
            return task
        return None

    def update_task(self, task_id: int, title: Optional[str] = None, description: Optional[str] = None) -> Optional[Task]:
        task = self.get_task(task_id)
        if task:
            if title is not None:
                if not title:
                    raise ValueError("Title cannot be empty")
                task.title = title
            if description is not None:
                task.description = description
            logger.info(f"Updated task {task_id}")
            return task
        return None
