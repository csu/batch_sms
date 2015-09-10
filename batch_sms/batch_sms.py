from multiprocessing import Process, Queue

from twilio.rest import TwilioRestClient

def sms_worker(to_queue, from_num, client, body):
    try:
        for to_num in iter(to_queue.get, 'END'):
            send_single_sms(client, body, to_num, from_num)
    except:
        pass
    return True

def send_single_sms(client, body, to_number, from_number, media_url=None, callback=None):
    message = client.messages.create(body=body,
        to=to_number,
        from_=from_number,
        media_url=media_url)
    
    if callback:
        payload = {
            'sid': str(message.sid),
            'body': body,
            'to': to_number,
            'from': from_number
        }
        if media_url:
            payload['media_url'] = media_url
        callback(payload)

class BatchSMS:
    def __init__(self, account_sid, auth_token, from_numbers=None):
        self.account_sid = account_sid
        self.auth_token = auth_token
        self.client = TwilioRestClient(self.account_sid, self.auth_token)

        if from_numbers:
            self.from_numbers = from_numbers
        else:
            self.from_numbers = []

    def add_from_number(self, number):
        self.from_numbers.append(number)

    def remove_from_number(self, number):
        self.from_numbers.remove(number)

    def send_sms(self, body, to_numbers, media_url=None):
        to_queue = Queue()
        for num in to_numbers:
            to_queue.put(num)

        processes = []
        for from_num in from_numbers:
            p = Process(target=sms_worker, args=(to_queue, from_num, self.client, body))
            p.start()
            to_queue.put('END')

        for p in processes:
            p.join()