#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-08-07
# @Author  : liyongqiang
# @Link    : ${link}
# @Version : 0.0.1

import os,re
import urllib.request
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

class Spider(object):

    # 打开driver
    def init_web_driver(self):
    	global driver
    	chrome_options = Options()
    	chrome_options.add_argument('--headless')
    	chrome_options.add_argument('--disable-gpu')
    	driver_path = 'E:\Program Files (x86)\python\Scripts\chromedriver.exe' #本地chormedriver.exe文件目录
    	driver = webdriver.Chrome(chrome_options=chrome_options, executable_path = driver_path)
        
    # 下载html页面
    # 需要传入要下载页面的url
    def html_downloader(self,url):
    	if url is None:
    		print('url参数为None')
    		return None

    	driver.get(url)
    	html = driver.page_source

    	return html

    #解析html页面
    def html_parser(self, html):
    	if html is None:
    		print('html参数为None')
    		return None

    	soup = BeautifulSoup(html, 'html.parser')
    	div = soup.find_all('div',class_='feedBox')
    	print(div)
    	return None

    # 关闭driver
    def close_driver(self):
    	driver.quit()

if __name__ == '__main__':
	toutiaoSpider = Spider()
	toutiaoSpider.init_web_driver()
	html = toutiaoSpider.html_downloader('https://www.toutiao.com/ch/news_tech/')
	toutiaoSpider.html_parser(html)
	toutiaoSpider.close_driver()




