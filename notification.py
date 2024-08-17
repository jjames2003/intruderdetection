from twilio.rest import Client

# Your Twilio Account SID and Auth Token
account_sid = 'AC5e804a0a0798b969aacf794f18fc0b1a'
auth_token = '9b5312e30fe16a6921acf4827e4a734d'

# Create a Twilio client
client = Client(account_sid, auth_token)

# Send a message using your Twilio trial phone number
message = client.messages.create(
    body='Hello from Twilio!',
    from_=' +13852824111',
    to='+917356196142'
)

print("Message SID:", message.sid)
