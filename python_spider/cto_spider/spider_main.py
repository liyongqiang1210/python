#!/usr/bin/python3.6
# coding=utf-8

'''

Created on 2017年1月9日

 51cto视频链接爬虫入口
html_cont:页面数据
@author: Li Yongqiang

'''
from cto_spider import html_downloader, html_parser, html_outputer
from cto_spider.database import Database


class SpiderMain(object):

    def __init__(self):
        self.downloader = html_downloader.HtmlDownloader()
        self.parser = html_parser.HtmlParsesr()
        self.outputer = html_outputer.HtmlOutputer()
        self.database = Database()

    def craw(self, url):
        try:
            html_cont = self.downloader.downloade(url)  # 下载页面数据
            new_urls = self.parser.parse(url, html_cont)  # 获取url集合
            for url in new_urls: # 遍历url集合存入数据库
                self.database.insertUrl(url)
        except:
            print('craw failed')
         
        
if __name__ == '__main__':
    print('========>开始爬取')
    root_url = 'http://edu.51cto.com/course/558.html'
    obj_spider = SpiderMain()
    obj_spider.craw(root_url)
    print('========>爬取结束')
