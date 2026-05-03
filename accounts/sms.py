import africastalking

africastalking.initialize(
    username='sandbox',  # change later
    api_key='YOUR_API_KEY'
)

sms = africastalking.SMS


def send_sms(message, phone_numbers):
    try:
        response = sms.send(message, phone_numbers)
        print(response)
    except Exception as e:
        print("SMS Error:", str(e))