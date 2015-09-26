from threading import Thread
from Queue import Queue

from twilio.rest import TwilioRestClient

def sms_worker(sender, body, to_queue, from_num):
    try:
        for to_num in iter(to_queue.get, 'END'):
            sender.send(body, to_num, from_num)
    except:
        pass
    return True

class BatchSMS:
    def __init__(self, sender, from_numbers=None):
        self.sender = sender

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
            t = Thread(target=sms_worker, args=(self.sender, body, to_queue, from_num))
            t.start()
            to_queue.put('END')

        for t in processes:
            t.join()