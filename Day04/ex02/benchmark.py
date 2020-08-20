import sys
import timeit


def filter_gmail_1(emails):
    gmails = []
    for email in emails:
        if email.endswith('@gmail.com'):
            gmails.append(email)
    return gmails


def filter_gmail_2(emails):
    return [email for email in emails if email.endswith('@gmail.com')]


def filter_gmail_3(emails):
    return list(map(lambda x: x if x.endswith('@gmail.com') else None, emails))


def filter_gmail_4(emails):
    return list(filter(lambda x: x.endswith('@gmail.com'), emails))


def check_results():
    emails = 5 * [
        'john@gmail.com', 'james@gmail.com', 'alice@yahoo.com',
        'anna@live.com', 'philipp@gmail.com'
        ]
    res_1 = filter_gmail_1(emails)
    res_2 = filter_gmail_2(emails)
    res_3 = filter_gmail_3(emails)
    res_4 = filter_gmail_4(emails)
    assert len(res_3) == len(emails)
    res_3_new = [email for email in res_3 if email]
    assert res_1 == res_2 == res_3_new == res_4
    for email in res_3:
        if email is not None:
            assert email.endswith('@gmail.com')


def compute_time(function, number):
    functions = {'loop': 1, 'list_comprehension': 2, 'map': 3, 'filter': 4}
    if function not in functions:
        raise ValueError('invalid function name')
    setup = f"""
from __main__ import filter_gmail_{functions[function]}

emails = 5 * ['john@gmail.com', 'james@gmail.com',
'alice@yahoo.com', 'anna@live.com', 'philipp@gmail.com']
    """
    stmt = f'filter_gmail_{functions[function]}(emails)'
    return timeit.timeit(setup=setup, stmt=stmt, number=number)


if __name__ == '__main__':
    check_results()
    if len(sys.argv) == 3:
        print(compute_time(sys.argv[1], int(sys.argv[2])))
    else:
        print('usage: python3 benchmark.py function number')
