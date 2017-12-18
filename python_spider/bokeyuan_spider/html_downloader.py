#!/usr/bin/python3.6
# coding=utf-8

'''

Created on 2017年12月4日

 html页面下载器使用urllib库

@author: Li Yongqiang

'''
from urllib.request import urlopen


class HtmlDownloader(object):
    
    #下载方法返回页面数据
    def downloade(self, url):
        if url is None:
            return None
        
        response = urlopen(url)
        
        if response.getcode() != 200:
            return None
        
        return response.read()


