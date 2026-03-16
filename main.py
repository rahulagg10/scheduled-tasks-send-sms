# Download the helper library from https://www.twilio.com/docs/python/install
import os
from twilio.rest import Client

# Find your Account SID and Auth Token at twilio.com/console
# and set the environment variables. See http://twil.io/secure
account_sid = ""
auth_token = ""
client = Client(account_sid, auth_token)

message = client.messages.create(
    body="Hello, How are you?",
    from_="+16562263135",
    to="+918800149444",
)
# print("SID:", account_sid[:6])
# print("Token length:", len(auth_token))
# print(client.api.accounts(account_sid).fetch().friendly_name)
print(message.body)
