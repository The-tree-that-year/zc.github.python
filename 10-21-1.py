import requests as rq
from lxml import etree
import time

base_url = "https://movie.douban.com/top250?start=%d&filter="
header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36'
}
for i in range(2):
    response = rq.get(base_url % (25*i), headers=header)
    HTML = etree.HTML(response.text)
    titles = HTML.xpath('//*[@id="content"]/div/div[1]/ol/li/div/div[2]/div[1]/a/span[1]/text()')
    infos = HTML.xpath('//*[@id="content"]/div/div[1]/ol/li/div/div[2]/div[2]/p[2]/span/text()')
    scores = HTML.xpath('//*[@id="content"]/div/div[1]/ol/li/div/div[2]/div[2]/div/span[2]/text()')
    for value in zip(titles, infos, scores):
        print({"电影名称": value[0], "电影简介": value[1], "电影评分":value[2]})
    time.sleep(1)

