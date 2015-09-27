from batch_sms import BatchSMS, Twilio
from secrets import TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN

sender = Twilio(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)
batcher = BatchSMS(sender)

body = 'hello, this is my message'
to_numbers = ['0123456789', '9876543210']
batcher.send_sms(body, to_numbers)