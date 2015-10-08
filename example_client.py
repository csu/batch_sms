from batch_sms import BatchSMS
from batch_sms import AssociatedBatchSender
from batch_sms import TwilioSender
from secrets import TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN

sender = TwilioSender(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)
batch_sender = AssociatedBatchSender(sender)
client = BatchSMS('test.db', batch_sender, auto_associate=True)

client.add_from_number('+15005550006')

client.add_to_number('+15005550010')
client.add_to_number('+15005550011')
client.add_to_number('+15005550012')
client.add_to_number('+15005550013')

# Needed when auto_associate is not used
# client.associate('+15005550010', '+15005550006')
# client.associate('+15005550011', '+15005550006')
# client.associate('+15005550012', '+15005550006')
# client.associate('+15005550013', '+15005550006')

sub_id = client.create_subscription_list('Hackers')
client.add_to_subscription('+15005550010', sub_id)
client.add_to_subscription('+15005550011', sub_id)
client.add_to_subscription('+15005550012', sub_id)
client.add_to_subscription('+15005550013', sub_id)

def callback(payload):
    print payload

client.send_to_subscription(sub_id, 'Hello World', callback=callback)