import openai
import os

class ChatGPTIntegrationModule:
    def __init__(self):
        # Убедитесь, что ключ API правильно загружен из переменных окружения
        self.api_key = os.getenv('OPENAI_API_KEY')
        openai.api_key = self.api_key

    def parse_message(self, message):
        # Запрос к ChatGPT
        response = openai.Completion.create(
            model="gpt-3.5-turbo",
            prompt=message,
            max_tokens=150
        )

        # Простейший парсер, который нужно адаптировать!!!!!!!
        response_text = response.choices[0].text.strip()

