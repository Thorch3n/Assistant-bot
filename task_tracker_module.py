from trello import TrelloClient
import os

class TaskTrackerModule:
    def __init__(self):
        self.client = TrelloClient(
            api_key=os.getenv('TRELLO_API_KEY'),
            api_secret=os.getenv('TRELLO_TOKEN')
        )
        self.board = self.client.list_boards()[0]  # Выберите правильную доску

    def create_task(self, params):
        """Создает задачу в Trello."""
        list_name = 'To Do'  # Замените на ваш список
        task_list = next((lst for lst in self.board.list_lists() if lst.name == list_name), None)
        if task_list:
            task_list.add_card(name=params['title'], due=params['due_date'])
            print(f"Task created: {params['title']} with due date {params['due_date']}")
        else:
            print(f"List '{list_name}' not found on board.")
