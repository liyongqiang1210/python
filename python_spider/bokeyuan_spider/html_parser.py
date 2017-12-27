#!/usr/bin/python3.6
# coding=utf-8

'''

Created on 2017年12月12日

 网页分析器

@author: Li Yongqiang

'''
from bs4 import BeautifulSoup
import re


class HtmlParsesr(object):

    # 获取新的url集合
    def _get_new_urls(self,soup):
        new_urls = set()
        # url格式：'http://www.cnblogs.com/dzpykj/p/8043810.html'
        links = soup.find_all('a', class_='titlelnk', href=re.compile(r'https://www.cnblogs.com/([a-zA-Z0-9]|-)+/p/([a-zA-Z0-9]|-)+.html'))
        for link in links:
            new_url = link['href']
            new_urls.add(new_url)
        return new_urls
    
    # 解析html页面的方法 
    def parse(self,html_data):
        
        if html_data is None:
            return
        else:
            # html页面解析器
            soup = BeautifulSoup(html_data, 'html.parser', from_encoding='utf-8')
            new_urls = self._get_new_urls(soup)
            return new_urls
