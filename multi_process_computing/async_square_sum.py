# async_square_sum.py

"""
输入一个列表，对于列表中的每个元素，我想计算 0 到这个元素的所有整数的平方和。
每一个元素平均分到每一个核来算。
"""
import concurrent.futures
import time


def compute_one(start, end):
    return sum(i * i for i in range(start, end))


def async_cpu_bound(number):
    ret = 0
    with concurrent.futures.ProcessPoolExecutor() as executor:
        to_do = []
        max_workers = executor._max_workers

        nodes = [round(number * i / max_workers) for i in range(max_workers)]
        nodes.append(number)
        for i in range(1, len(nodes)):
            future = executor.submit(compute_one, nodes[i - 1], nodes[i])
            to_do.append(future)
            # as_completed函数，在future完成后，输出结果
        for future in concurrent.futures.as_completed(to_do):
            ret += future.result()
    print(ret)


def calculate_sums(numbers):
    for number in numbers:
        async_cpu_bound(number)


def main():
    start_time = time.perf_counter()
    numbers = [10000000 + x for x in range(60)]
    calculate_sums(numbers)
    end_time = time.perf_counter()
    print('Calculation takes {} seconds'.format(end_time - start_time))


if __name__ == '__main__':
    main()
