# coding=utf-8

'''

Created on 2017年12月12日

 网页分析器

@author: Li Yongqiang

'''
from bs4 import BeautifulSoup
import re
from urllib.parse import urljoin


class HtmlParsesr(object):

    #获取新的url集合
    def _get_new_urls(self, page_url, soup):
        new_urls = set()
        # url格式：'http://www.cnblogs.com/dzpykj/p/8043810.html'
        links = soup.find_all('a', href=re.compile(r'http://www.cnblogs.com/[a-zA-Z]+/p/[0-9]+.html'))
        for link in links:
            new_url = link['href']
            new_urls.add(new_url)
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
    #解析html页面的方法 
    def parse(self, page_url, html_data):
        
        if page_url is None or html_data is None:
            return
        else:
            #html页面解析器
            soup = BeautifulSoup(html_data, 'html.parser', from_encoding='utf-8')
            new_urls = self._get_new_urls(page_url, soup)
            new_data = self._get_new_data(page_url, soup)
            return new_urls,new_data
