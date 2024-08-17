from twilio.rest import Client

# Your Twilio Account SID and Auth Token
account_sid = 'AC5e804a0a0798b969aacf794f18fc0b1a'
auth_token = '9b5312e30fe16a6921acf4827e4a734d'

# Initialize Twilio client
client = Client(account_sid, auth_token)

# Function to send SMS notification
def send_notification(phone_number):
    try:
        message = client.messages.create(
            body="Human detected!",
            from_=' +13852824111',  # Your Twilio phone number
            to=phone_number
        )
        print(f"Notification sent to {phone_number}: {message.sid}")
        return True
    except Exception as e:
        print(f"Error sending notification to {phone_number}: {e}")
        return False
