# crawl_async.py

"""
异步的爬取豆瓣上北京即将上映电影的名称、上映日期和原始海报图片
"""
import asyncio
import time

import aiohttp
from bs4 import BeautifulSoup

headers = {
    "Cookie":     "bid=\"qNzQ6uMlaCw\"",
    "User-Agent": "Paw/3.1.10 (Macintosh; OS X/10.15.4) GCDHTTPRequest"
}


async def fetch_content(url):
    async with aiohttp.ClientSession(
            headers=headers, connector=aiohttp.TCPConnector(ssl=False)
    ) as session:
        async with session.get(url) as response:
            return await response.text()


async def main():
    url = "https://movie.douban.com/cinema/later/beijing/"
    init_page = await fetch_content(url)
    init_soup = BeautifulSoup(init_page, 'lxml')

    movie_names, urls_to_fetch, movie_dates = [], [], []

    all_movies = init_soup.find('div', id="showing-soon")
    for each_movie in all_movies.find_all('div', class_="item"):
        all_a_tag = each_movie.find_all('a')
        all_li_tag = each_movie.find_all('li')

        movie_names.append(all_a_tag[1].text)
        urls_to_fetch.append(all_a_tag[1]['href'])
        movie_dates.append(all_li_tag[0].text)

    tasks = [fetch_content(url) for url in urls_to_fetch]
    pages = await asyncio.gather(*tasks)

    for movie_name, movies_date, page in zip(movie_names, movie_dates, pages):
        soup_item = BeautifulSoup(page, 'lxml')
        img_tag = soup_item.find('img')

        print('{} {} {}'.format(movie_name, movies_date, img_tag['src']))


if __name__ == '__main__':
    s = time.perf_counter()
    asyncio.run(main())
    e = time.perf_counter()
    print(e - s)
