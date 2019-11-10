from twilio.rest import Client
import json
from os.path import expanduser

class Notification:

    def __init__(self):
        key_file = expanduser("~/api.key")
        with open(key_file) as file:
            key = json.load(file)

        account_sid =  key['sid']
        auth_token = key['token']

        self.number = "+12024108297"
        self.smsClient = Client(account_sid, auth_token)

    def send_sms(self, message, recipient):
        self.smsClient.messages.create(
            body= message,
            from_= self.number,
            to = recipient
        )