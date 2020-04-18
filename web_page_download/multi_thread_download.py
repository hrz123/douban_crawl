# multi_thread_download.py

"""
多线程下载一些文件并打印
"""
import concurrent.futures
import time

import requests


def download_one(url):
    resp = requests.get(url)
    print('Read {} from {}'.format(len(resp.content), url))


def download_all(sites):
    # 并发的方式提高运行效率
    # 也可以用并行的方式去提高程序运行效率，下面语句改为
    # with concurrent.futures.ProcessPoolExecutor() as executor:
    # 在需要修改的这部分代码中，函数 ProcessPoolExecutor() 表示创建进程池，使用多个进程并行的执行程序。
    # 不过，这里我们通常省略参数 workers，因为系统会自动返回 CPU 的数量作为可以调用的进程数。
    # 并行的方式一般用在 CPU heavy 的场景中，因为对于 I/O heavy 的操作，多数时间都会用于等待，
    # 相比于多线程，使用多进程并不会提升效率。反而很多时候，因为 CPU 数量的限制，会导致其执行效率不如多线程版本。
    with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
        executor.map(download_one, sites)


def main():
    sites = {
        'https://en.wikipedia.org/wiki/Portal:Arts',
        'https://en.wikipedia.org/wiki/Portal:History',
        'https://en.wikipedia.org/wiki/Portal:Society',
        'https://en.wikipedia.org/wiki/Portal:Biography',
        'https://en.wikipedia.org/wiki/Portal:Mathematics',
        'https://en.wikipedia.org/wiki/Portal:Technology',
        'https://en.wikipedia.org/wiki/Portal:Geography',
        'https://en.wikipedia.org/wiki/Portal:Science',
        'https://en.wikipedia.org/wiki/Computer_science',
        'https://en.wikipedia.org/wiki/Python_(programming_language)',
        'https://en.wikipedia.org/wiki/Java_(programming_language)',
        'https://en.wikipedia.org/wiki/PHP',
        'https://en.wikipedia.org/wiki/Node.js',
        'https://en.wikipedia.org/wiki/The_C_Programming_Language',
        'https://en.wikipedia.org/wiki/Go_(programming_language)'
    }

    start_time = time.perf_counter()
    download_all(sites)
    end_time = time.perf_counter()
    print('Download {} sites in {} seconds'.format(len(sites), end_time - start_time))


if __name__ == '__main__':
    main()
