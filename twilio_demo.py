from twilio.rest import Client
import os
account_sid = "{your_account_sid}"
auth_token = "{your_auth_token}"
client = Client(account_sid, auth_token)

message = client.messages \
                .create(
                     body="Join Earth's mightiest heroes. Like Kevin Bacon.",
                     from_='{your_twilio_number}',
                     to='{your_phone_number}'
                 )

print(message.sid)