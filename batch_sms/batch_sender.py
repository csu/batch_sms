# Batch SMS
# Christopher J. Su
# Copyright (c) 2015

from abc import ABCMeta, abstractmethod

class BatchSender:
  __metaclass__ = ABCMeta

  @abstractmethod
  def send_sms(self, message_body, numbers, media_url=None, callback=None, on_fail=None): pass