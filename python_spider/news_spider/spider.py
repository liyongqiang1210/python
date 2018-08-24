#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-08-07
# @Author  : Li Yongqiang
# @Link    : 
# @Version : 0.0.1

"""
    爬虫父类
"""
import os
import re
import time
import random
import json
import urllib.request
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

class Spider(object):

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
        print("浏览器已打开！")

        return driver

    # 关闭driver方法
    def close_driver(self):
        driver.quit()
        print("浏览器已关闭！")

    # 获取html页面数据
    def get_html(self, url):
        if url != "":
            driver.get(url)
            html = driver.page_source
            return html
        else:
            print("url参数不能为空！")
            return
        

if __name__ == '__main__':
    Spider().open_driver()
    Spider().close_driver()





