from batch_sms import AssociatedBatchSender, TwilioSender
from secrets import TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN, test_from_num, test_to_num

def send_message_callback(payload):
    print payload

sender = TwilioSender(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)
batch_sender = AssociatedBatchSender(sender)

body = 'hello, this is my message'
numbers = {test_from_num: [test_to_num]}
batch_sender.send_sms(body, numbers, callback=send_message_callback)