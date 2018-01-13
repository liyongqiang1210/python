#!/usr/bin/python3.6
# coding=utf-8

'''

Created on 2017年1月9日

 

@author: Li Yongqiang

'''
from bs4 import BeautifulSoup
import re


class HtmlParsesr(object):

    # 获取页面的url集合
    def _get_new_urls(self, page_url, soup):
        new_urls = set()
        # url格式：'http://edu.51cto.com/center/course/lesson/index?id=12263'
        # 匹配到合适的url
        links = soup.find_all('a', href=re.compile(r'/center/course/lesson/index\?id=\d{5}'))
        for link in links:
            new_url = link['href']  # 视频url
            title = link['title']  # 视频title
            print('title=======>' + title +'\nurl地址=======>' + new_url)
            new_urls.add(new_url)
        return new_urls
        
    def parse(self, page_url, html_cont):
        
        if page_url is None:
            return
        else:
            soup = BeautifulSoup(html_cont, 'html.parser', from_encoding='utf-8')
            new_urls = self._get_new_urls(page_url, soup)
            return new_urls
