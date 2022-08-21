from twilio.rest import Client
from dotenv import load_dotenv
import os
import smtplib

load_dotenv()


class NotificationManager:

    def __init__(self):
        self.client = Client(os.environ['TWILIO_SID'], os.environ['TWILIO_TOKEN'])
#Whatsapp sender msg
    def send_sms(self, message):
        message = self.client.messages.create(
            from_='whatsapp:+14155238886',
            body=message,
            to="whatsapp:+380661508739",
        )
        print(message.sid)

                )
# Mail sender
    def send_emails(self, emails, message, google_flight_link):
        with smtplib.SMTP(MAIL_PROVIDER_SMTP_ADDRESS) as connection:
            connection.starttls()
            connection.login(MY_EMAIL, MY_PASSWORD)
            for email in emails:
                connection.sendmail(
                    from_addr=MY_EMAIL,
                    to_addrs=email,
                    msg=f"Subject:New Low Price Flight!\n\n{message}\n{google_flight_link}".encode('utf-8')
                )