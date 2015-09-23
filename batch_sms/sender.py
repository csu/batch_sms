from abc import ABCMeta, abstractmethod

class Sender:
    __metaclass__ = ABCMeta

    @abstractmethod
    def send_message(self): pass