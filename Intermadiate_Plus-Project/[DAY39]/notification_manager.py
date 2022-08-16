from twilio.rest import Client
from dotenv import load_dotenv
import os

load_dotenv()


class NotificationManager:

    def __init__(self):
        self.client = Client(os.environ['TWILIO_SID'], os.environ['TWILIO_TOKEN'])

    def send_sms(self, message):
        message = self.client.messages.create(
            body=message,
            from_=os.environ["TWILIO_NUMBER"],
            to=os.environ["TWILIO_MY_NUMBER"],
        )
        print(message.sid)
