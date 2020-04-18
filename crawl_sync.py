# crawl_sync.py

"""
同步的爬取豆瓣上北京即将上映电影的名称、上映日期和原始海报图片
"""
import time

import requests
from bs4 import BeautifulSoup


def main():
    headers = {
        "Cookie":     "bid=\"qNzQ6uMlaCw\"",
        "User-Agent": "Paw/3.1.10 (Macintosh; OS X/10.15.4) GCDHTTPRequest"
    }
    url = "https://movie.douban.com/cinema/later/beijing/"
    init_page = requests.get(url, headers=headers).content
    init_soup = BeautifulSoup(init_page, 'lxml')

    all_movies = init_soup.find('div', id="showing-soon")
    for each_movie in all_movies.find_all('div', class_="item"):
        all_a_tag = each_movie.find_all('a')
        all_li_tag = each_movie.find_all('li')

        movie_name = all_a_tag[1].text
        url_to_fetch = all_a_tag[1]['href']
        movie_date = all_li_tag[0].text

        response_item = requests.get(url_to_fetch, headers=headers).content
        soup_item = BeautifulSoup(response_item, 'lxml')
        img_tag = soup_item.find('img')

        print('{} {} {}'.format(movie_name, movie_date, img_tag['src']))


if __name__ == '__main__':
    s = time.perf_counter()
    main()
    e = time.perf_counter()
    print(e - s)
