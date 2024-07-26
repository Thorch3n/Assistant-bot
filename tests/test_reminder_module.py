import unittest
from reminder_module import ReminderModule


class TestReminderModule(unittest.TestCase):
    def setUp(self):
        self.module = ReminderModule()

    def test_set_reminder(self):
        # Тут можно добавить проверку для установки напоминания
        pass


if __name__ == '__main__':
    unittest.main()
