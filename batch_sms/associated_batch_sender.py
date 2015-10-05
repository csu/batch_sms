from batch_sender import BatchSender

from threading import Thread

def sms_associated(sender, message_body, to_numbers, from_num, callback=None):
    for to_num in to_numbers:
        sender.send(message_body, to_num, from_num, callback=callback)
    return True

class AssociatedBatchSender(BatchSender):
    def __init__(self, sender):
        self.sender = sender

    def send_sms(self, message_body, numbers, media_url=None, callback=None):
        """
        numbers: {
            "from_number": [
                "to_numbers",
                "to_numbers",
                "to_numbers"
            ]
        }
        """
        processes = []
        for key, value in numbers.iteritems():
            t = Thread(target=sms_associated, args=(self.sender, message_body, value, key, callback))
            processes.append(t)
            t.start()

        for t in processes:
            t.join()