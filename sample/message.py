from twilio.rest import Client
from prettytable import PrettyTable


account_sid = '' # account sid from twilio
auth_token = '' # account auth token from twilio
to_number = 'whatsapp:+44xxxxxxxxxx' # phone number

client = Client(account_sid, auth_token)


def make_message(parsed_weather):
    """takes a dict of weather data and processes into a message to send to whatsapp"""
    table = PrettyTable(['T'.center(6), '°C'.center(6), 'description', 'c%'.center(3), 'ws'.center(4)])
    for p in ['00', '03', '06', '09', '12', '15', '18', '21']:
        table.add_row(parsed_weather[p])
    # print(table)
    return table


def send_message(message):
    """uses twilio to send a whatsapp message to a phone number"""
    print(message)
    message = client.messages.create(
        body=message,
        from_='whatsapp:+14155238886',
        to=to_number
    )