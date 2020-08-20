class Research():
    def __init__(self, filename):
        self.filename = filename

    def file_reader(self):
        with open(self.filename, 'r') as file:
            text = file.read()
        return text


if __name__ == '__main__':
    print(Research('data.csv').file_reader())
