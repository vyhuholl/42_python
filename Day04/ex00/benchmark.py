import timeit


def filter_gmail_1(emails):
    gmails = []
    for email in emails:
        if email.endswith('@gmail.com'):
            gmails.append(email)
    return gmails


def filter_gmail_2(emails):
    return [email for email in emails if email.endswith('@gmail.com')]


def check_results():
    emails = 5 * [
        'john@gmail.com', 'james@gmail.com', 'alice@yahoo.com',
        'anna@live.com', 'philipp@gmail.com'
        ]
    res_1 = filter_gmail_1(emails)
    res_2 = filter_gmail_2(emails)
    assert res_1 == res_2
    for email in res_1:
        assert email.endswith('@gmail.com')


def main():
    check_results()
    setup = """
from __main__ import filter_gmail_1, filter_gmail_2

emails = 5 * ['john@gmail.com', 'james@gmail.com',
'alice@yahoo.com', 'anna@live.com', 'philipp@gmail.com']
    """
    stmt_1 = 'filter_gmail_1(emails)'
    stmt_2 = 'filter_gmail_2(emails)'
    time_1 = timeit.timeit(setup=setup, stmt=stmt_1, number=90000000)
    time_2 = timeit.timeit(setup=setup, stmt=stmt_2, number=90000000)
    if time_1 > time_2:
        res = 'loop'
    else:
        res = 'list comprehension'
    time_sorted = sorted([time_1, time_2])
    print(f'it is better to use a {res}')
    print(f'{time_sorted[0]} vs {time_sorted[1]}')


if __name__ == '__main__':
    main()
