import logging
import os
from dotenv import load_dotenv
from gpt_integration import ChatGPTIntegrationModule
from calendar_module import CalendarModule
from task_tracker_module import TaskTrackerModule
from reminder_module import ReminderModule
from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext, MessageHandler, Filters

# Загрузка переменных окружения из файла .env
load_dotenv()

class MainBotModule:
    def __init__(self, gpt_module, calendar_module, task_tracker_module, reminder_module):
        self.gpt_module = gpt_module
        self.calendar_module = calendar_module
        self.task_tracker_module = task_tracker_module
        self.reminder_module = reminder_module

    def handle_message(self, update: Update, context: CallbackContext):
        message = update.message.text
        parsed_message = self.gpt_module.parse_message(message)
        intent = parsed_message['intent']
        params = parsed_message['params']

        if intent == 'schedule_meeting':
            response = f"Создана встреча: {params['title']} на {params['date']} в {params['time']}"
            self.calendar_module.create_meeting(params)
        elif intent == 'create_task':
            response = f"Создана задача: {params['title']} с дедлайном {params['due_date']}"
            self.task_tracker_module.create_task(params)
        elif intent == 'set_reminder':
            response = f"Напоминание: {params['reminder_text']} на {params['reminder_date']} в {params['reminder_time']}"
            self.reminder_module.set_reminder(params)
        else:
            response = "Неизвестная команда"

        update.message.reply_text(response)

def start(update: Update, context: CallbackContext):
    update.message.reply_text('Здравствуйте! Я ваш электронный помощник.')

def help_command(update: Update, context: CallbackContext):
    update.message.reply_text('Как я могу помочь вам?')

if __name__ == "__main__":
    # Настройка логирования
    logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

    # Инициализация модулей
    gpt_module = ChatGPTIntegrationModule()
    calendar_module = CalendarModule()  # Инициализация с подключением к Google Calendar
    task_tracker_module = TaskTrackerModule()  # Инициализация с подключением к Trello
    reminder_module = ReminderModule()  # Инициализация с SMTP

    # Инициализация основного модуля бота
    bot = MainBotModule(gpt_module, calendar_module, task_tracker_module, reminder_module)

    # Получение токена из переменных окружения
    TOKEN = os.getenv('TELEGRAM_BOT_TOKEN')
    if not TOKEN:
        raise ValueError("TELEGRAM_BOT_TOKEN not found in .env file")

    # Настройка Telegram бота
    updater = Updater(token=TOKEN, use_context=True)
    dispatcher = updater.dispatcher

    # Добавление обработчиков команд
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("help", help_command))
    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, bot.handle_message))

    # Запуск бота
    updater.start_polling()
    updater.idle()
