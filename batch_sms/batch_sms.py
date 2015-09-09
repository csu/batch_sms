from twilio.rest import TwilioRestClient

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