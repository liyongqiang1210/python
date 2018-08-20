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

class Spider(object):


    # 打开driver方法
    def open_driver(self):
        global driver
        # chrome浏览器驱动，无头模式
        chrome_options = Options()
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('--disable-gpu')
        driver_path = 'E:\python\Scripts\chromedriver.exe' #本地chormedriver.exe文件目录
        driver = webdriver.Chrome(chrome_options=chrome_options, executable_path=driver_path)
        # 设置最长的超时时间
        # driver.set_page_load_timeout(10)
        
    # 关闭driver方法
    def close_driver(self):
        driver.quit()





