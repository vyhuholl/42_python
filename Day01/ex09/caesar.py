import sys


def encode(string, shift):
    ascii_lowercase = 'abcdefghijklmnopqrstuvwxyz'
    ascii_uppercase = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    printable = set(
        ascii_lowercase + ascii_uppercase + '0123456789' +
        r'!\"#$%&\'()*+,-./:;<=>?@[\]^_`{|}~' + ' \t\n\r\f\v'
        )
    res = ''
    for char in string:
        if char not in printable:
            raise ValueError(' The script does not support your language yet')
        elif char in ascii_lowercase:
            res += ascii_lowercase[(ascii_lowercase.index(char) + shift) % 26]
        elif char in ascii_uppercase:
            res += ascii_uppercase[(ascii_uppercase.index(char) + shift) % 26]
        else:
            res += char
    return res


if __name__ == '__main__':
    if len(sys.argv) == 1:
        print('usage: python3 caesar.py option string shift')
    elif len(sys.argv) == 4:
        if sys.argv[1] == 'encode':
            print(encode(sys.argv[2], int(sys.argv[3])))
        elif sys.argv[1] == 'decode':
            print(encode(sys.argv[2], -int(sys.argv[3])))
        else:
            raise ValueError('Incorrect option')
    else:
        raise ValueError('Incorrect number of arguments')
