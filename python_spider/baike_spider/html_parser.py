# coding=utf-8

'''

Created on 2017年12月4日

 

@author: Li Yongqiang

'''
from bs4 import BeautifulSoup
import re
from urllib.parse import urljoin
from baike_spider import database


class HtmlParsesr(object):

    def _get_new_urls(self, page_url, soup):
        new_urls = set()
        # url格式：''
        links = soup.find_all('a', href=re.compile(r'/item/([A-Z0-9]|%)+'))
        for link in links:
            new_url = link['href']
            new_full_url = urljoin(page_url, new_url)
            database.Database().insertUrl(new_full_url)
            new_urls.add(new_full_url)
        return new_urls
    
    def _get_new_data(self, page_url, soup):
        res_data = {}
        
        # url
        res_data['url'] = page_url
        # <dd class="lemmaWgt-lemmaTitle-title"><h1>速读</h1>
        title_node = soup.find('dd', class_='lemmaWgt-lemmaTitle-title').find('h1')
        print('网页的title:%s' % (title_node))
        res_data['title'] = title_node.get_text()
        
        # <div class="lemma-summary" label-module="lemmaSummary">
        summary_node = soup.find('div', class_='lemma-summary')
        res_data['summary'] = summary_node.get_text()
        
        return res_data
        
    def parse(self, page_url, html_cont):
        
        if page_url is None or html_cont is None:
            return
        else:
            soup = BeautifulSoup(html_cont, 'html.parser', from_encoding='utf-8')
            new_urls = self._get_new_urls(page_url, soup)
            new_data = self._get_new_data(page_url, soup)
            return new_urls, new_data
