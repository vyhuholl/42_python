import sys


def ticker_symbols(ticker):
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
    if ticker not in tickers:
        return 'Unknown ticker'
    return f'{tickers[ticker]} {stocks[ticker]}'


if __name__ == '__main__':
    if len(sys.argv) == 2:
        print(ticker_symbols(sys.argv[1].upper()))
    else:
        print('usage: python3 ticker_symbols.py ticker')
