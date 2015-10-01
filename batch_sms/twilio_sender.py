from sender import Sender

from twilio.rest import TwilioRestClient

class TwilioSender(Sender):
    def __init__(self, account_sid, auth_token):
        self.client = TwilioRestClient(account_sid, auth_token)

    def send(self, body, to_number, from_number, media_url=None, callback=None):
        message = self.client.messages.create(body=body,
            to=to_number,
            from_=from_number,
            media_url=media_url)
    
        if callback:
            payload = {
                'result': str(message.sid),
                'body': body,
                'to': to_number,
                'from': from_number
            }
            if media_url:
                payload['media_url'] = media_url

            callback(payload)