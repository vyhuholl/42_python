import sys
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

    class Calculations():
        def __init__(self, data):
            self.data = data
            self.count = self.counts()
            self.fraction = self.fractions()

        def counts(self):
            return tuple(sum(elem) for elem in zip(*self.data))

        def fractions(self):
            return tuple(elem / sum(self.count) for elem in self.count)

    class Analytics(Calculations):
        def predict_random(self, num_steps):
            dictionary = {0: [0, 1], 1: [1, 0]}
            return [dictionary[randint(0, 1)] for i in range(num_steps)]

        def predict_last(self):
            return self.data[-1]


if __name__ == '__main__':
    if len(sys.argv) == 2:
        reader = Research(sys.argv[1])
        print(reader.data)
        print(' '.join([str(elem) for elem in reader.calc.count]))
        print(' '.join([str(elem) for elem in reader.calc.fraction]))
        print(reader.calc.predict_random(3))
        print(reader.calc.predict_last())
    else:
        print('usage: python3 first_constructor.py filepath')
