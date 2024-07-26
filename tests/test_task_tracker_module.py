import unittest
from task_tracker_module import TaskTrackerModule


class TestTaskTrackerModule(unittest.TestCase):
    def setUp(self):
        self.module = TaskTrackerModule()

    def test_create_task(self):
        # Тут можно добавить проверку для создания задачи
        pass


if __name__ == '__main__':
    unittest.main()
