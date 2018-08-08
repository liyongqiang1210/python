#!/usr/bin/python3.6
# coding=utf-8

'''

Created on 2017年12月12日

 博客园爬虫入口
@author: Li Yongqiang

'''
import html_downloader, html_parser, html_outputer, database


class SpiderMain(object):

	def __init__(self):
		# html页面下载器
		# html页面分析器
		self.parser = html_parser.HtmlParsesr()
		# 爬取数据输出器
		self.outputer = html_outputer.HtmlOutputer()
		# 数据库url管理器器
		self.database = database.Database()

	def craw(self, root_url, url_type):
		try:
			print('CRAW URL: %s' % (root_url))
			# 使用html页面下载器下载页面数据
			html_data = self.downloader.downloade(root_url)
			# 分析获取爬取页面的我们需要url与数据
			new_urls = self.parser.parse(html_data)
			
			# for url in new_urls :
			# 	self.database.insertUrl(url, url_type, '')
		except :
				print('craw falied !!!')


if __name__ == '__main__':
		
		type_list = ['web', 'java', 'php', 'python', 'cpp', 'javascript', 'jquery', 'linux', 'mysql', 'all']
		obj_spider = SpiderMain()
		for url_type in type_list:
			print('-------------' + url_type + ' craw start-------------')
			for page in range(0, 201):
				root_url = 'https://www.cnblogs.com/cate/%s/%d' % (url_type,page)
				obj_spider.craw(root_url, url_type)
		print('-------------' + url_type + ' craw end-------------')
