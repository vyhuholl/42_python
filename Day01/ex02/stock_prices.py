import sys


def stock_prices(company):
    companies = {
        'Apple': 'AAPL',
        'Microsoft': 'MSFT',
        'Netflix': 'NFLX',
        'Tesla': 'TSLA',
        'Nokia': 'NOK'
        }
    stocks = {
        'AAPL': 287.73,
        'MSFT': 173.79,
        'NFLX': 416.90,
        'TSLA': 724.88,
        'NOK': 3.37
        }
    if company not in companies:
        return 'Unknown company'
    return stocks[companies[company]]


if __name__ == '__main__':
    if len(sys.argv) == 2:
        print(stock_prices(sys.argv[1].capitalize()))
    else:
        print('usage: python3 stock_prices.py company')
