#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-08-07
# @Author  : liyongqiang
# @Link    : ${link}
# @Version : 0.0.1

import os,re,time,random
import urllib.request
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.firefox.options import Options

class Spider(object):

    # 打开driver方法
    def open_driver(self):
        global driver
        # chrome浏览器驱动，无头模式
        chrome_options = Options()
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('--disable-gpu')
        driver_path = 'E:\Program Files (x86)\python\Scripts\chromedriver.exe' #本地chormedriver.exe文件目录
        driver = webdriver.Chrome(chrome_options=chrome_options, executable_path = driver_path)
        # 设置最长的超时时间
        # driver.set_page_load_timeout(10)
        
    
    # 关闭driver方法
    def close_driver(self):
        driver.quit()


    # 下载html动态页面方法
    # 需要传入要下载页面的url
    def html_downloader_dynamic(self,url):
        if url is None:
            print('url参数为None')
            return None
        
        # 浏览器打开url
        driver.get(url)
        
        # 逐渐滚动浏览器窗口,使ajax逐渐加载
        for i in range(1, 30):
            # 将页面滚动条向下滚动
            js = 'var q=document.documentElement.scrollTop=' + str(1000 * i)
            # 执行js
            driver.execute_script(js)
            # 等待1s
            time.sleep(2)

        # 截屏方法
        # driver.save_screenshot('E:/original.jpg')
        
        # 获取页面源码
        html = driver.page_source

        return html


    #解析html页面方法
    def html_parser_dynamic(self, html):
        if html is None:
            print('html参数为None')
            return

        # 将html转换成BeautifulSoup对象
        soup = BeautifulSoup(html, 'html.parser')

        # 筛选出我们需要的内容
        div_list = soup.find_all('div',class_='item-inner y-box')

        # 遍历筛选出的内容
        for div in div_list:
            try:
                # 获取文章title
                a = div.find_all('a', class_='link title')
                title = a[0].string
                
                # 获取文章url
                th = a[0].get('href')
                title_href = th[6:len(th)]
                
                # 获取文章source
                b = div.find_all('a', class_='lbtn source')
                source = (b[0].string)[0:len((b[0].string))-1]
                
                # 获取文章来源url
                source_href = b[0].get('href')
                
                # 获取文章标题图片url
                c = div.find_all('img')
                img_url = c[0].get('src')
                print(title + ':' + title_href + ';' + source + ':' + img_url)
            except Exception as e:
                print('异常：' + e)
                continue

        return


if __name__ == '__main__':
    toutiaoSpider = Spider()
    toutiaoSpider.open_driver()
    html = toutiaoSpider.html_downloader_dynamic('https://www.toutiao.com/ch/news_sports/')
    toutiaoSpider.html_parser_dynamic(html)
    toutiaoSpider.close_driver()




