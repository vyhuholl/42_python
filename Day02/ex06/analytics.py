import json
import requests
from random import randint


class Research():
    def __init__(self, filename):
        self.filename = filename
        self.data = self.file_reader()
        self.calc = self.Analytics(self.data)

    def file_reader(self, has_header=True):
        with open(self.filename, 'r') as file:
            text = file.read()
        lines = text.split('\n')
        if has_header and len(lines[0].split(',')) != 2:
            raise ValueError('Incorrect header')
        if has_header:
            lines = lines[1:]
        if len(lines) == 0:
            raise ValueError('No lines')
        for line in lines:
            if line != '0,1' and line != '1,0':
                raise ValueError('Incorrect line')
        return [[int(elem) for elem in line.split(',')] for line in lines]

    def send_message_to_slack(self, message, webhook_url=None):
        slack_data = {'text': message}
        if webhook_url is not None:
            requests.post(
                webhook_url,
                data=json.dumps(slack_data),
                headers={'Content-Type': 'application/json'}
                )

    class Calculations():
        def __init__(self, data):
            self.data = data
            self.count = self.counts()
            self.fraction = self.fractions()

        def counts(self):
            return tuple(sum(elem) for elem in zip(*self.data))

        def fractions(self):
            return tuple(elem / sum(self.count) * 100 for elem in self.count)

    class Analytics(Calculations):
        def predict_random(self, num_steps):
            dictionary = {0: [0, 1], 1: [1, 0]}
            return [dictionary[randint(0, 1)] for i in range(num_steps)]

        def predict_last(self):
            return self.data[-1]

        def save_file(self, data, filename, extension='txt'):
            with open(f'{filename}.{extension}', 'w') as file:
                file.write(data)
