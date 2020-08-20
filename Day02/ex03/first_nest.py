import sys


class Research():
    def __init__(self, filename):
        self.filename = filename
        self.data = self.file_reader()
        self.calc = self.Calculations(self.data)

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
            return ([sum(elem) for elem in zip(*self.data)])

        def fractions(self):
            return (elem / sum(self.count) for elem in self.count)


if __name__ == '__main__':
    if len(sys.argv) == 2:
        reader = Research(sys.argv[1])
        print(reader.data)
        print(' '.join([str(elem) for elem in reader.calc.count]))
        print(' '.join([str(elem) for elem in reader.calc.fraction]))
    else:
        print('usage: python3 first_constructor.py filepath')
