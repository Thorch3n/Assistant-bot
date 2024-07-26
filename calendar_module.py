import os.path
import datetime
from google.oauth2 import service_account
from googleapiclient.discovery import build

class CalendarModule:
    SCOPES = ['https://www.googleapis.com/auth/calendar']
    SERVICE_ACCOUNT_FILE = 'path/to/your/credentials.json'

    def __init__(self):
        self.creds = None
        self.service = None
        self.authenticate()

    def authenticate(self):
        """Authenticate and create the Google Calendar API service."""
        self.creds = service_account.Credentials.from_service_account_file(
            self.SERVICE_ACCOUNT_FILE, scopes=self.SCOPES)
        self.service = build('calendar', 'v3', credentials=self.creds)

    def create_meeting(self, params):
        """Create a meeting in Google Calendar."""
        event = {
            'summary': params['title'],
            'start': {
                'dateTime': f"{params['date']}T{params['time']}:00",
                'timeZone': 'America/Los_Angeles',  # Замените на ваш часовой пояс
            },
            'end': {
                'dateTime': f"{params['date']}T{int(params['time'].split(':')[0])+1}:00",
                'timeZone': 'America/Los_Angeles',  # Замените на ваш часовой пояс
            },
        }

        event = self.service.events().insert(calendarId='primary', body=event).execute()
        print(f"Event created: {event.get('htmlLink')}")

