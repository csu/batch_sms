# Batch SMS
# Christopher J. Su
# Copyright (c) 2015

from abc import ABCMeta, abstractmethod

class Sender:
    __metaclass__ = ABCMeta

    @abstractmethod
    def send(self, message_body, to_number, from_number, media_url=None, callback=None): pass