#!/usr/bin/python3.6
# coding=utf-8

'''

Created on 2017年12月4日

 

@author: Li Yongqiang

'''
from bs4 import BeautifulSoup
import re
from urllib.parse import urljoin


class HtmlParsesr(object):

    # 获取页面的url集合
    def _get_new_urls(self, page_url, soup):
        new_urls = set()
        # url格式：''
        links = soup.find_all('a', href=re.compile(r'/item/([A-Z0-9]|%)+'))
        for link in links:
            new_url = link['href']
            new_full_url = urljoin(page_url, new_url)
            new_urls.add(new_full_url)
        return new_urls
        
    def parse(self, page_url, html_cont):
        
        if page_url is None:
            return
        else:
            soup = BeautifulSoup(html_cont, 'html.parser', from_encoding='utf-8')
            new_urls = self._get_new_urls(page_url, soup)
            return new_urls
