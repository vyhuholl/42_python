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


def check_results():
    emails = 5 * [
        'john@gmail.com', 'james@gmail.com', 'alice@yahoo.com',
        'anna@live.com', 'philipp@gmail.com'
        ]
    res_1 = filter_gmail_1(emails)
    res_2 = filter_gmail_2(emails)
    res_3 = filter_gmail_3(emails)
    assert res_1 == res_2
    assert len(res_3) == len(emails)
    res_3_new = [email for email in res_3 if email]
    assert res_3_new == res_1
    for email in res_3:
        if email is not None:
            assert email.endswith('@gmail.com')


def main():
    check_results()
    setup = """
from __main__ import filter_gmail_1, filter_gmail_2, filter_gmail_3

emails = 5 * ['john@gmail.com', 'james@gmail.com',
'alice@yahoo.com', 'anna@live.com', 'philipp@gmail.com']
    """
    stmt_1 = 'filter_gmail_1(emails)'
    stmt_2 = 'filter_gmail_2(emails)'
    stmt_3 = 'filter_gmail_3(emails)'
    time_1 = timeit.timeit(setup=setup, stmt=stmt_1, number=90000000)
    time_2 = timeit.timeit(setup=setup, stmt=stmt_2, number=90000000)
    time_3 = timeit.timeit(setup=setup, stmt=stmt_3, number=90000000)
    min_time = min([time_1, time_2, time_3])
    if min_time == time_1:
        res = 'loop'
    elif min_time == time_2:
        res = 'list comprehension'
    else:
        res = 'map'
    time_sorted = sorted([time_1, time_2, time_3])
    print(f'it is better to use a {res}')
    print(f'{time_sorted[0]} vs {time_sorted[1]} vs {time_sorted[2]}')


if __name__ == '__main__':
    main()
