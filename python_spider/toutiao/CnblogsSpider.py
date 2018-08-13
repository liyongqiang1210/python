#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-08-07
# @Author  : liyongqiang
# @Link    : ${link}
# @Version : 0.0.1

import os
import re
import time
import random
import json
import urllib.request
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

class CnblogsSpider(object):

    # 定义博客类型列表集合
    # NEWS_TYPE_LIST = {
    #     'java','cpp','php','python','ruby','c','go','r','108702','design','dp','javascript','jquery','html5',
    #     'android','ios','sqlserver','oracle','mysql','nosql','bigdata','linux'
    #     }
    NEWS_TYPE_LIST = {
        'java'
        }

    # 打开driver方法
    def open_driver(self):
        global driver
        # chrome浏览器驱动，无头模式
        chrome_options = Options()
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('--disable-gpu')
        driver_path = 'E:\python\Scripts\chromedriver.exe' #本地chormedriver.exe文件目录
        driver = webdriver.Chrome(chrome_options=chrome_options, executable_path=driver_path)
        
    # 关闭driver方法
    def close_driver(self):
        driver.quit()

    # 下载html静态页面方法
    # 需要传入要下载页面的url
    def html_downloader_static(self,type):
        if type is None:
            print('url参数为None')
            return None
        # 分页获取
        for i in range(1, 10):
            # 将页面滚动条向下滚动
            url = 'https://www.cnblogs.com/cate/' + type + '/#p' + str(i)
            # 浏览器打开url
            driver.get(url)
        html = driver.page_source
        return html


    # 解析html页面方法
    def html_parser_static(self, html):
        if html is None:
            print('html参数为None')
            return
        #  声明一个博客对象列表对象
        news_object_list = []
        # 将html转换成BeautifulSoup对象
        soup = BeautifulSoup(html, 'html.parser')
        # 筛选出我们需要的内容
        div_list = soup.find_all('div',class_='post_item')
        # 遍历筛选出的内容
        for div in div_list:
            try:
                # 获取博客title
                a = div.find_all('a', class_='titlelnk')
                if len(a) > 0:
                    title = a[0].string
                    # 获取博客url
                    title_href = a[0].get('href')
                else:
                    continue
                # 获取博客部分内容
                b = div.find_all('a', class_='post_item_summary')
                if len(b) > 0:
                    content = b[0].string
                else:
                    continue
                # 获取博客作者和url
                c = div.find_all('lightblue')
                if len(c) > 0:
                    author_name = c[0].string
                    author_url = c[0].get('href')
                else:
                    continue
                # 获取发布时间
                d = div.find_all('div', class_='post_item_foot')
                if len(d) > 0:
                    release_time = d[0].string
                else:
                    continue
                # 创建博客字符串对象
                print("{'title':'" + title + "','title_href':'" + title_href + "','content':'" + content + "','author_name':'" + author_name + "'}")
                news_object = "{'title':'" + title + "','title_href':'" + title_href + "','content':'" + content + "','author_name':'" + author_name + "'}"
                news_object_list.append(news_object)
            except Exception as e:
                print('异常：' + e)
            continue
        return json.dumps(news_object_list, ensure_ascii=False)

    # 爬虫主函数
    def main(self):
        try:
            self.open_driver()
            for news_type in CnblogsSpider.NEWS_TYPE_LIST:
                print('=======================>' + news_type + '爬虫启动')
                html = self.html_downloader_static(news_type)
                news_object_list = self.html_parser_static(html)
                if news_object_list != "":
                    print(news_object_list)
                print('=======================>' + news_type + '爬虫结束')
        except Exception as e:
            raise e
        finally:
            self.close_driver() # 关闭driver
        
        
if __name__ == '__main__':
    spider = CnblogsSpider()
    spider.main()




