# -*-coding:utf8-*-

import requests
from bs4 import BeautifulSoup
import pandas as pd
from fake_useragent import UserAgent

class MaoyanSpider(object):

    def __init__(self,url):
        self.headers = {"User-Agent": UserAgent().random}
        self.url = url
        self.datas = list()

    # 通过for循环，获取10页的电影信息的源码
    def getPage(self):
        for i in range(0,10):
            url = self.url + "?offset={0}".format(i*10)
            response = requests.get(url, headers = self.headers)
            if response.status_code == 200:
                self.parsePage(response.text)
            else:
                return None

    # 通过BeautifulSoup获取每页10部电影的详细信息
    def parsePage(self, html):
        soup = BeautifulSoup(html, "html.parser")
        details = soup.find_all("dd")
        for dd in details:
            data = {}
            data["index"] = dd.find("i").text
            data["name"] = dd.find("p", class_ = "name").text
            data["star"] = dd.find("p", class_="star").text.strip()[3:]
            data["time"] = dd.find("p", class_="releasetime").text.strip()[5:]
            data["score"] = dd.find("p", class_="score").text
            self.datas.append(data)

    # 通过DataFrame，把Top100的电影存储到CSV文件中
    def saveData(self):
        self.getPage()
        data = pd.DataFrame(self.datas)
        columns = ["index", "name", "star", "time", "score"]
        data.to_csv(".\maoyanTop100.csv", index=False, columns=columns)

if __name__ == "__main__":
    url = "http://maoyan.com/board/4"
    spider = MaoyanSpider(url)
    spider.saveData()