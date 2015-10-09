from batch_sms import BatchSMS
from batch_sms import AssociatedBatchSender
from batch_sms import TwilioSender
from secrets import TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN

sender = TwilioSender(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)
batch_sender = AssociatedBatchSender(sender)
client = BatchSMS('test.db', batch_sender, auto_associate=True)

sub_id = client.create_subscription_list('Hackers')

client.add_from_number('+15005550006')

subs = [sub_id]
client.add_to_number('+15005550010', subs=subs)
client.add_to_number('+15005550011', subs=subs)
client.add_to_number('+15005550012', subs=subs)
client.add_to_number('+15005550013', subs=subs)

def callback(payload):
    print payload

client.send_to_subscription(sub_id, 'Hello World', callback=callback)