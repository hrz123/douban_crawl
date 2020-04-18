# python_callback.py

"""
用python实现回调函数，使用协程（python内置asyncio库）
"""
import asyncio
import time


async def crawl_page(url):
    print('crawling {}'.format(url))
    sleep_time = int(url.split('_')[-1])
    await asyncio.sleep(sleep_time)
    return 'OK {}'.format(url)


async def main(urls):
    tasks = [asyncio.create_task(crawl_page(url)) for url in urls]
    for task in tasks:
        task.add_done_callback(lambda future: print('result: ', future.result()))
    await asyncio.gather(*tasks)


if __name__ == '__main__':
    s = time.perf_counter()
    asyncio.run(main(['url_1', 'url_2', 'url_3', 'url_4']))
    e = time.perf_counter()
    print(e - s)
