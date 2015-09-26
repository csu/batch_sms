from batch_sms import BatchSMS, Twilio
from secrets import ACCOUNT_SID, AUTH_TOKEN

sender = Twilio(ACCOUNT_SID, AUTH_TOKEN)
batcher = BatchSMS(sender)

body = 'hello, this is my message'
to_numbers = ['0123456789', '9876543210']
batcher.send_sms(body, to_numbers)