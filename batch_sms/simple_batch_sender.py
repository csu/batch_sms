# Batch SMS
# Christopher J. Su
# Copyright (c) 2015

from threading import Thread
from Queue import Queue

from batch_sender import BatchSender

def sms_worker(sender, message_body, to_queue, from_num, callback=None):
  try:
    for to_num in iter(to_queue.get, 'END'):
      sender.send(message_body, to_num, from_num, callback=callback)
  except:
    pass
  return True

class SimpleBatchSender(BatchSender):
  def __init__(self, sender, from_numbers=None):
    self.sender = sender

    if from_numbers:
      if isinstance(list, from_numbers):
        self.from_numbers = from_numbers
      else:
        self.from_numbers = [from_numbers]
    else:
      self.from_numbers = []

  def add_from_number(self, number):
    self.from_numbers.append(number)

  def remove_from_number(self, number):
    self.from_numbers.remove(number)

  def send_sms(self, message_body, to_numbers, media_url=None, callback=None):
    if not isinstance(list, to_numbers):
      to_numbers = [to_numbers]

    to_queue = Queue()
    for num in to_numbers:
      to_queue.put(num)

    processes = []
    for from_num in self.from_numbers:
      t = Thread(target=sms_worker, args=(self.sender, message_body, to_queue, from_num, callback))
      t.start()
      to_queue.put('END')
      processes.append(t)

    for t in processes:
      t.join()