import sys


class Research():
    def __init__(self, filename):
        self.filename = filename

    def file_reader(self):
        with open(self.filename, 'r') as file:
            text = file.read()
        lines = text.split('\n')
        if len(lines) < 2:
            raise ValueError('Too few lines')
        if len(lines[0].split(',')) != 2:
            raise ValueError('Incorrect header')
        for line in lines[1:]:
            if line != '0,1' and line != '1,0':
                raise ValueError('Incorrect line')
        return text


if __name__ == '__main__':
    if len(sys.argv) == 2:
        print(Research(sys.argv[1]).file_reader())
    else:
        print('usage: python3 first_constructor.py filepath')
