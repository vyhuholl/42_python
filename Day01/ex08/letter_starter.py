import sys


def letter_starter(email):
    name = email.split('@')[0].split('.')[0].capitalize()
    return f'Dear {name}, welcome to our team.'


if __name__ == '__main__':
    if len(sys.argv) == 2:
        print(letter_starter(sys.argv[1]))
    else:
        print('usage: python3 letter_starter e-mail')
