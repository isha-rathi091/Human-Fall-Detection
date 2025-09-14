from twilio.rest import Client

def send_sms_alert(message, to_number):
    account_sid = 'your_account_sid'
    auth_token = 'your_auth_token'
    client = Client(account_sid, auth_token)

    client.messages.create(
        body=message,
        from_='+1234567890',  # Your Twilio number
        to=to_number
    )
