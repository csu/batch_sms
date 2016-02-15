# Batch SMS
# Christopher J. Su
# Copyright (c) 2015

from threading import current_thread

from batch_sms import AssociatedBatchSender, TwilioSender
from secrets import TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN

test_nums = {
    '+15005550006': ['+15005550010', '+15005550011', '+15005550012', '+15005550013']
}

def send_message_callback(payload):
    print current_thread().name
    print payload

sender = TwilioSender(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)
batch_sender = AssociatedBatchSender(sender)

body = 'hello, this is my message'
batch_sender.send_sms(body, test_nums, callback=send_message_callback)