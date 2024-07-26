# Пример возможных утилит для работы с датами
from datetime import datetime

def parse_date(date_string):
    try:
        return datetime.strptime(date_string, '%Y-%m-%d')
    except ValueError:
        return None
