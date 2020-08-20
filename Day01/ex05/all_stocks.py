import sys


def find_element(elem):
    companies = {
        'Apple': 'AAPL',
        'Microsoft': 'MSFT',
        'Netflix': 'NFLX',
        'Tesla': 'TSLA',
        'Nokia': 'NOK'
        }
    tickers = {value: key for key, value in companies.items()}
    stocks = {
        'AAPL': 287.73,
        'MSFT': 173.79,
        'NFLX': 416.90,
        'TSLA': 724.88,
        'NOK': 3.37
        }
    elem_cap = elem.capitalize()
    elem_up = elem.upper()
    if elem_cap in companies:
        return f'{elem_cap} stock price is {stocks[companies[elem_cap]]}'
    elif elem_up in tickers:
        return f'{elem_up} is a ticker symbol for {tickers[elem_up]}'
    return f'{elem} is an unknown company or an unknown ticker symbol'


def all_stocks(string):
    string_split = string.replace(',', ' , ').split()
    commas_num = string_split.count(',')
    if commas_num * 2 + 1 == len(string_split):
        for elem in string_split:
            if elem != ',':
                print(find_element(elem.strip(',')))


if __name__ == '__main__':
    if len(sys.argv) == 2:
        all_stocks(sys.argv[1])
    else:
        print('usage: python3 all_stocks.py string')
