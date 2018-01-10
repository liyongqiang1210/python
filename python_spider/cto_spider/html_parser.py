#!/usr/bin/python3.6
# coding=utf-8

'''

Created on 2017年1月9日

 

@author: Li Yongqiang

'''
from bs4 import BeautifulSoup
import re
from urllib.parse import urljoin


class HtmlParsesr(object):

    # 获取页面的url集合
    def _get_new_urls(self, page_url, soup):
        new_urls = set()
        # url格式：'http://edu.51cto.com/center/course/lesson/index?id=12263'
        # 匹配到合适的url
        links = soup.find_all('a', href=re.compile(r'/center/course/lesson/index\?id=\d{5}'))
        # 视频title
        titles = soup.find_all('title', href=re.compile(r'/center/course/lesson/index\?id=\d{5}'))
        
        for link,title in links,titles:
            title = title # 视频标题
            new_url = link['href']
            new_full_url = urljoin(page_url, new_url) # 视频地址url
            new_urls.add(new_full_url)
        return new_urls
        
    def parse(self, page_url, html_cont):
        
        if page_url is None:
            return
        else:
            soup = BeautifulSoup(html_cont, 'html.parser', from_encoding='utf-8')
            new_urls = self._get_new_urls(page_url, soup)
            return new_urls
