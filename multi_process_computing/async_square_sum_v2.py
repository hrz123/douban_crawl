# async_square_sum_v2.py

"""
输入一个列表，对于列表中的每个元素，我想计算 0 到这个元素的所有整数的平方和。
每个CPU核算一个元素。
"""
import multiprocessing
import time


def cpu_bound(number):
    print(sum(i * i for i in range(number)))


def find_sums(numbers):
    with multiprocessing.Pool() as pool:
        pool.map(cpu_bound, numbers)


if __name__ == "__main__":
    numbers = [10000000 + x for x in range(60)]

    start_time = time.time()
    find_sums(numbers)
    duration = time.time() - start_time
    print(f"Duration {duration} seconds")


import threading

n = 0

def foo():
    global n
    n += 1

threads = []
for i in range(100):
    t = threading.Thread(target=foo)
    threads.append(t)

for t in threads:
    t.start()

for t in threads:
    t.join()

print(n)