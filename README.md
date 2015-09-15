# batch-sms
Send bulk SMS in batches with the Twilio API. Made to send notifications for DubHacks.

## Usage
```python
from batch_sms import BatchSMS

nums = ['your', 'phone', 'numbers']
batch_sms = BatchSMS(TWILIO_SID, TWILIO_AUTH_TOKEN, from_numers=nums)
```