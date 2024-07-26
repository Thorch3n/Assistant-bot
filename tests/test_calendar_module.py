import unittest
from calendar_module import CalendarModule


class TestCalendarModule(unittest.TestCase):
    def setUp(self):
        self.module = CalendarModule()

    def test_create_meeting(self):
        # Тут можно добавить проверку для создания встречи
        pass


if __name__ == '__main__':
    unittest.main()
