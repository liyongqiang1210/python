#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-08-14 10:05:29
# @Author  : Li Yongqiang

"""

这个类是凤凰资讯新闻网站爬虫

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

    # 打开driver方法
    def open_driver(self):
        global driver
        # chrome浏览器驱动，无头模式
        chrome_options = Options()
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('--disable-gpu')
        driver_path = 'E:\Program Files (x86)\python\Scripts\chromedriver.exe' #本地chormedriver.exe文件目录
        driver = webdriver.Chrome(chrome_options=chrome_options, executable_path=driver_path)
        
    # 关闭driver方法
    def close_driver(self):
        driver.quit()

    def get_html(self, url):
        driver.get(url)
        html = driver.page_source
        return html

    def get_data(self, html):
        # 创建新闻集合
        news_object_list = []
        # 筛选出我们所需的信息
        soup_html = BeautifulSoup(html, 'html.parser')
        div = soup_html.find('div', class_='newsList')
        soup_div = BeautifulSoup(str(div))
        li_list = soup_div.find_all('li')
        for li in li_list:
            soup = BeautifulSoup(str(li))
            news_release_time = soup.find('h4').get_text()
            news_title = soup.find('a').get_text()
            news_url = soup.find('a').get('href')
            print("news_release_time:" + str(datetime.datetime.now().year) + "/" + news_release_time + ",news_title:" + news_title + ",news_url:" + news_url)

    def main(self):
        try:
            self.open_driver()
            html = self.get_html('http://news.ifeng.com/listpage/11502/0/1/rtlist.shtml')
            self.get_data(html)
        except Exception as e:
            raise e
        finally:
            self.close_driver()
        
        
        
if __name__ == '__main__':
    spider = FengHuangSpider()
    spider.main()
