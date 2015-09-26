from batch_sms import BatchSMS, Twilio
from secrets import ACCOUNT_SID, AUTH_TOKEN

sender = Twilio(ACCOUNT_SID, AUTH_TOKEN)
batcher = BatchSMS(sender)