# sync_square_sum.py

"""
输入一个列表，对于列表中的每个元素，我想计算 0 到这个元素的所有整数的平方和。
常规版本。
"""

import time


def cpu_bound(number):
    print(sum(i * i for i in range(number)))


def calculate_sums(numbers):
    for number in numbers:
        cpu_bound(number)


def main():
    start_time = time.perf_counter()
    numbers = [10000000 + x for x in range(20)]
    calculate_sums(numbers)
    end_time = time.perf_counter()
    print('Calculation takes {} seconds'.format(end_time - start_time))


if __name__ == '__main__':
    main()
