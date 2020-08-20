import sys


def names_extractor(filename):
    with open(filename, 'r') as input_file:
        with open('employees.tsv', 'w') as output_file:
            output_file.write('Name\tSurname\tE-mail\n')
            for line in input_file.readlines():
                line_split = line.split('@')[0].split('.')
                name = line_split[0].capitalize()
                surname = line_split[1].capitalize()
                output_file.write(f'{name}\t{surname}\t{line}')


if __name__ == '__main__':
    if len(sys.argv) == 2:
        names_extractor(sys.argv[1])
    else:
        print('usage: python3 names_extractor.py filename')
