import sys
import time
import requests
from bs4 import BeautifulSoup


def get_row(ticker, row):
    url = f'https://finance.yahoo.com/quote/{ticker}/financials'
    page = requests.get(url).text
    page_parsed = BeautifulSoup(page, 'html.parser')
    title = page_parsed.title.string
    if title == 'Symbol Lookup from Yahoo Finance':
        raise ValueError('ticker does not exist')
    tags = page_parsed.find_all(attrs={'data-test': 'fin-row'})
    rows = [tag.find(class_='Va(m)').get_text() for tag in tags]
    if row not in rows:
        raise ValueError('row does not exist')
    elems = tags[rows.index(row)].find_all('span')
    return tuple(elem.get_text() for elem in elems)


if __name__ == '__main__':
    if len(sys.argv) == 3:
        print(get_row(sys.argv[1], sys.argv[2]))
    else:
        print('usage: python3 financial.py ticker field')
