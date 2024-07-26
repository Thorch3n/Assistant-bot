import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import os

class ReminderModule:
    def __init__(self):
        self.smtp_server = os.getenv('SMTP_SERVER')
        self.smtp_port = os.getenv('SMTP_PORT')
        self.smtp_user = os.getenv('SMTP_USER')
        self.smtp_password = os.getenv('SMTP_PASSWORD')

    def send_email(self, subject, body, to_email):
        """Отправляет email через SMTP."""
        msg = MIMEMultipart()
        msg['From'] = self.smtp_user
        msg['To'] = to_email
        msg['Subject'] = subject
        msg.attach(MIMEText(body, 'plain'))

        with smtplib.SMTP(self.smtp_server, self.smtp_port) as server:
            server.starttls()
            server.login(self.smtp_user, self.smtp_password)
            server.sendmail(self.smtp_user, to_email, msg.as_string())

    def set_reminder(self, params):
        """Устанавливает напоминание через email."""
        subject = 'Reminder'
        body = f"Напоминание: {params['reminder_text']}. Дата: {params['reminder_date']} Время: {params['reminder_time']}"
        to_email = os.getenv('REMINDER_EMAIL')  # Email получателя
        self.send_email(subject, body, to_email)
        print(f"Reminder set: {params['reminder_text']} on {params['reminder_date']} at {params['reminder_time']}")
