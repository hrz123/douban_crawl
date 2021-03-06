# multi_thread_download_v2.py

"""
多线程下载一些文件并打印的另一个版本
"""

import concurrent.futures
import time

import requests


def download_one(url):
    try:
        resp = requests.get(url)
        print('Read {} from {}'.format(len(resp.content), url))
    except requests.exceptions.RequestException as exc:
        print("exception met from {}".format(url))


def download_all(sites):
    with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
        to_do = []
        for site in sites:
            # 调用submit，将下载每一个网站的内容都放进future队列to_do，等待执行
            future = executor.submit(download_one, site)
            to_do.append(future)
            # as_completed函数，在future完成后，输出结果
        for future in concurrent.futures.as_completed(to_do):
            future.result()


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
