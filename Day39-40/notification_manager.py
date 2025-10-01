from twilio.rest import Client
import os 
from dotenv import load_dotenv
load_dotenv(".env")


account_sid=os.getenv('ACCOUNT_ID')
auth_token=os.getenv('auth_token')
what_from=os.getenv('what_from')
what_to=os.getenv('what_to')

class NotificationManager:
    #This class is responsible for sending notifications with the deal flight details.
    def __init__(self):
        pass

    def send_notification(self, message_body):
        self.client = Client(account_sid, auth_token)
        # Simple WhatsApp sender (no try/except)
        message = self.client.messages.create(
            from_=f"whatsapp:{what_from}",
            to=f"whatsapp:{what_to}",
            body=message_body
        )
        print(message.sid)
        print("message sent.")
    
