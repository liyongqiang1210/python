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

    def craw(self, video_url,video_id):
        try:
            html_cont = self.downloader.downloade(video_url)  # 下载页面数据
            self.parser.parse(video_id, html_cont)  # 获取url集合
        except:
            print('craw failed')
         
        
if __name__ == '__main__':
    print('========>开始爬取')
    for i in range(4000):
        print(i)
        video_id,video_url = Database().selectVideoUrlIsCraw()
        obj_spider = SpiderMain()
        obj_spider.craw(video_url,video_id)
    print('========>爬取结束')
