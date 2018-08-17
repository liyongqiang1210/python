#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-08-14 10:05:29
# @Author  : Li Yongqiang

"""

凤凰资讯新闻网站爬虫

"""

import re
import time
import random
import json
import datetime
import urllib.request
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

"""

凤凰资讯爬虫

"""


class FengHuangSpider(object):

    # 定义文章类型列表集合
    NEWS_TYPE_LIST = {

    }

    # 创建set集合用来存放新闻
    NEWS_OBJECT_LIST = []

    # 打开driver方法
    def open_driver(self):
        global driver
        # chrome浏览器驱动，无头模式
        chrome_options = Options()
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('--disable-gpu')
        # 本地chormedriver.exe文件目录
        driver_path = 'E:\Program Files (x86)\python\Scripts\chromedriver.exe'
        driver = webdriver.Chrome(
            chrome_options=chrome_options, executable_path=driver_path)

    # 关闭driver方法
    def close_driver(self):
        driver.quit()

    # 获取html页面数据
    def get_html(self, url):
        driver.get(url)
        html = driver.page_source
        return html

    # 获取我们需要的数据
    def get_data(self, html):
        
        # 筛选出我们所需的信息
        soup_html = BeautifulSoup(html, 'html.parser')
        div = soup_html.find('div', class_='newsList')
        soup_div = BeautifulSoup(str(div))
        li_list = soup_div.find_all('li')
        
        for li in li_list:
            soup = BeautifulSoup(str(li))
            news_release_time = soup.find('h4').get_text()  # 新闻发布时间
            news_title = soup.find('a').get_text()  # 新闻标题
            news_url = soup.find('a').get('href')  # 新闻url
            news_object = '{news_release_time:' + str(datetime.datetime.now().year) + '/' \
            + news_release_time + ',news_title:' + news_title + ',news_url:' + news_url + '}'

            # 去除重复数据
            if news_object not in FengHuangSpider.NEWS_OBJECT_LIST:
                FengHuangSpider.NEWS_OBJECT_LIST.append(news_object)

        print(json.dumps(FengHuangSpider.NEWS_OBJECT_LIST, ensure_ascii=False))


    def get_top10_data(self, html):
        soup_html = BeautifulSoup(html, 'html.parser')
        div = soup_html.find('div', class_='top10')
        soup_div = BeautifulSoup(str(div))
        a_list = soup_div.find_all('a')
        i = 1
        for a in a_list:
            if i > 10:
                break
            news_title = a.get_text()
            news_url = a.get('href')
            news_ranking = i
            print("{news_title:" + news_title + ", news_url:"+ news_url + ", news_ranking:" + str(news_ranking) + "}")
            i = i+1

    def main(self):
        try:
            self.open_driver()
            html = self.get_html( \
                'http://news.ifeng.com/listpage/11502/0/1/rtlist.shtml')
            # self.get_data(html)
            self.get_top10_data(html)
        except Exception as e:
            raise e
        finally:
            self.close_driver()


if __name__ == '__main__':
    spider = FengHuangSpider()
    spider.main()
