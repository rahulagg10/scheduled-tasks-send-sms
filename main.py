# Download the helper library from https://www.twilio.com/docs/python/install
import os
from twilio.rest import Client

# Find your Account SID and Auth Token at twilio.com/console
# and set the environment variables. See http://twil.io/secure
account_sid = "ACdbf284cd6bb78d55287ddd29654f9b1e"
auth_token = "6767cd1f751b77350fc1cd18a654d404"
client = Client(account_sid, auth_token)

# message = client.messages.create(
#     body="Aaj Night ka kya plan h?",
#     from_="+16562263135",
#     to="+918800149444",
# )
print(client.api.accounts(account_sid).fetch().friendly_name)
# print(message.body)
