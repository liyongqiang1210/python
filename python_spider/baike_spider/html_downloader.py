# coding=utf-8

'''

Created on 2017年12月4日

 

@author: Li Yongqiang

'''
from urllib.request import urlopen


class HtmlDownloader(object):
    
    def downloade(self, url):
        if url is None:
            return None
        
        response = urlopen(url)
        
        if response.getcode() != 200:
            return None
        
        return response.read()

