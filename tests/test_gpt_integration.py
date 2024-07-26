import unittest
from gpt_integration import ChatGPTIntegrationModule


class TestChatGPTIntegrationModule(unittest.TestCase):
    def setUp(self):
        self.module = ChatGPTIntegrationModule()

    def test_parse_message_meeting(self):
        result = self.module.parse_message("Поставь встречу с клиентом на 30 июля в 15:00")
        self.assertEqual(result['intent'], 'schedule_meeting')

    def test_parse_message_task(self):
        result = self.module.parse_message("Создай задачу написать отчет с дедлайном 25 июля")
        self.assertEqual(result['intent'], 'create_task')

    def test_parse_message_reminder(self):
        result = self.module.parse_message("Напомни позвонить маме 24 июля в 18:00")
        self.assertEqual(result['intent'], 'set_reminder')


if __name__ == '__main__':
    unittest.main()
