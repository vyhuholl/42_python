import sys
import timeit
from functools import reduce


def sum_of_squares_1(n):
    res = 0
    for i in range(1, n + 1):
        res += i ** 2
    return res


def sum_of_squares_2(n):
    return reduce(lambda x, y: x + y ** 2, [i for i in range(1, n + 1)])


def compute_time(function, number, n):
    functions = {'loop': 1, 'reduce': 2}
    if function not in functions:
        raise ValueError('invalid function name')
    setup = f'from __main__ import sum_of_squares_{functions[function]}'
    stmt = f'sum_of_squares_{functions[function]}({n})'
    return timeit.timeit(setup=setup, stmt=stmt, number=number)


if __name__ == '__main__':
    assert sum_of_squares_1(5) == sum_of_squares_2(5) == 55
    if len(sys.argv) == 4:
        print(compute_time(sys.argv[1], int(sys.argv[2]), int(sys.argv[3])))
    else:
        print('usage: python3 benchmark.py function number n')
