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
from database import Database
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

"""

凤凰资讯爬虫

"""


class FengHuangSpider(object):

    # 存放24小时阅读排行榜新闻列表集合
    NEWS_RANKING_LIST = []

    # 存放即时新闻
    NEWS_INSTANT_LIST = []

    # 历史资讯集合
    NEWS_HISTORY_LIST = []

    # 网站名
    NEWS_WEBSITE = "fenghuangzixun"

    # 日期
    CREATE_TIME = time.strftime("%Y-%m-%d", time.localtime())

    # 创建数据库连接对象
    database = Database()

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
        driver.implicitly_wait(30)

    # 关闭driver方法
    def close_driver(self):
        driver.quit()

    # 获取html页面数据
    def get_html(self, url):
        driver.get(url)
        html = driver.page_source
        return html

    # 获取凤凰资讯即时新闻数据
    def get_instant_data(self, html):
        
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
            news_instant = '{news_release_time:' + \
                           str(datetime.datetime.now().year) + '/' \
                           + news_release_time + ',news_title:' + news_title \
                           + ',news_url:' + news_url + '}'

            # 去除重复数据
            if news_instant not in FengHuangSpider.NEWS_INSTANT_LIST:
                FengHuangSpider.NEWS_INSTANT_LIST.append(news_instant)

        # 将数据转换为json格式
        json_instant = json.dumps(FengHuangSpider.NEWS_INSTANT_LIST, 
                       ensure_ascii=False)

        return json_instant

    # 获取凤凰资讯排行前十新闻数据
    def get_ranking_data(self, html):
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
            ranking = i
            i = i+1
            news_ranking = "{news_title:" + news_title + \
                           ", news_url:"+ news_url + ", ranking:" + \
                           str(ranking) + "}";
            
            # 去除重复数据
            if news_ranking not in FengHuangSpider.NEWS_RANKING_LIST:
                FengHuangSpider.NEWS_RANKING_LIST.append(news_ranking)
        
        # 转换成json格式数据
        json_ranking = json.dumps(FengHuangSpider.NEWS_RANKING_LIST, 
                          ensure_ascii=False)

        return json_ranking

    # 获取凤凰网历史资讯数据
    def get_history_data(self, html):

        news_type = "history"

        # 开始解析页面
        html = BeautifulSoup(html,'html.parser')
        div_list = html.find_all('div', class_='box_list clearfix')
        for div in div_list:
            try:
                news_release_time = div.find("span").get_text()
                h2 = BeautifulSoup(str(div.find("h2")),'html.parser')
                news_url = h2.find("a").get("href")
                news_title = h2.find("a").get("title")
                news_content = div.find("p").get_text()
                if div.find("img") != "" and div.find("img") != None:
                    news_image = div.find("img").get("src")
                news_image = ""
                news_history = "('" + str(news_title) + "','" + str(news_content) + "','" \
                                + str(news_image) + "','" + str(news_release_time) + "','" \
                                + str(news_type) + "','" + str(news_url) + "','" + \
                                  FengHuangSpider.NEWS_WEBSITE + "','" + str(FengHuangSpider.CREATE_TIME) + "')";
            except Exception as e:
                print("get_history_data()方法出现异常：" + e)
                continue

            if news_history not in FengHuangSpider.NEWS_HISTORY_LIST:
                FengHuangSpider.NEWS_HISTORY_LIST.append(news_history)

        # 转换成json格式
        # json_history = json.dumps(FengHuangSpider.NEWS_HISTORY_LIST,ensure_ascii=False)

    # 爬取全部历史资讯方法
    def news_history_all_main(self):
        page_url = "https://news.ifeng.com/listpage/4762/1/list.shtml"
        i = 0
        # 获取历史资讯数据
        while page_url != "" and i < 9:
            try:
                print(page_url)

                # 模拟点击下一页按钮
                html = self.get_html(page_url)
                elem_next_page = driver.find_element_by_id("pagenext") # 根据id找到下一页按钮
                elem_next_page.click() # 模拟点击下一页按钮
                page_url = driver.current_url # 下一页要打开的url
                
                # 获取数据
                self.get_history_data(html)
                time.sleep(1)
                i = i+1
            except Exception as e:
                print("news_history_all_main()方法出现异常：" + e)
                break
                

        # FengHuangSpider.database.insert_news(FengHuangSpider.NEWS_HISTORY_LIST)



    def main(self):
        try:
            self.open_driver()
            # 获取即时资讯和前十资讯
            # html = self.get_html( \
            #     'http://news.ifeng.com/listpage/11502/0/1/rtlist.shtml')
            # instant_news = self.get_instant_data(html)
            # ranking_news = self.get_ranking_data(html)
            # print(instant_news)
            # print(ranking_news)
            
            # 获取历史资讯数据
            # html = self.get_html(
            #        'https://news.ifeng.com/listpage/4763/1/list.shtml')
            # print(self.get_history_data(html))

            self.news_history_all_main()
        except Exception as e:
            raise e
        finally:
            self.close_driver()


if __name__ == '__main__':
    spider = FengHuangSpider()
    spider.main()

