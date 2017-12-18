# coding=utf-8

'''

Created on 2017年12月4日

 百科爬虫入口
html_cont:页面数据
@author: Li Yongqiang

'''
from baike_spider import html_downloader, html_outputer, html_parser
from baike_spider.database import Database


class SpiderMain(object):

    def __init__(self):
        self.downloader = html_downloader.HtmlDownloader()
        self.parser = html_parser.HtmlParsesr()
        self.outputer = html_outputer.HtmlOutputer()
        self.database = Database()

    def craw(self, url):
        while self.database.selectUrlNoCraw() != '' :
            try:
                html_cont = self.downloader.downloade(self.database.selectUrlNoCraw())
                new_urls= self.parser.parse(self.database.selectUrlNoCraw(), html_cont)
                for url in new_urls:
                    self.database.insertUrl(url)
            except:
                print('craw failed')
         
        
if __name__ == '__main__':
    print("开始爬取")
    root_url = 'https://baike.baidu.com/item/%E8%8A%B1%E9%B8%9F/5703594#viewPageContent'
    obj_spider = SpiderMain()
    obj_spider.craw(root_url)
    print('爬取结束')
