class Must_read():
    def __init__(self, filename):
        with open(filename, 'r') as file:
            print(file.read())


if __name__ == '__main__':
    Must_read('data.csv')
