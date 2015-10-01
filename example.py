from batch_sms import BatchSMS, TwilioSender
from secrets import TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN, test_from_num, test_to_num

def send_message_callback(payload):
    print payload

sender = TwilioSender(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)
batcher = BatchSMS(sender, from_numbers=[test_from_num])

body = 'hello, this is my message'
to_numbers = [test_to_num]
batcher.send_sms(body, to_numbers, callback=send_message_callback)