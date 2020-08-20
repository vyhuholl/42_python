def read_and_write(filename):
    with open(f'{filename}.csv', 'r') as file_csv:
        with open(f'{filename}.tsv', 'w') as file_tsv:
            new_text = file_csv.read().replace('\",', '\"\t')
            new_text = new_text.replace('false,', 'false\t')
            new_text = new_text.replace('true,', 'true\t')
            file_tsv.write(new_text)


if __name__ == '__main__':
    read_and_write('d01_ds')
