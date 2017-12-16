# coding=utf-8

'''

Created on 2017年12月12日

 博客园爬虫入口
@author: Li Yongqiang

'''
from bokeyuan_spider import html_downloader, html_parser, html_outputer, \
	database

class SpiderMain(object):

	def __init__(self):
		# html页面下载器
		self.downloader = html_downloader.HtmlDownloader()
		# html页面分析器
		self.parser = html_parser.HtmlParsesr()
		# 爬取数据输出器
		self.outputer = html_outputer.HtmlOutputer()
		# 数据库url管理器器
		self.database = database.Database()
	def craw(self, root_url, url_type):
		# 爬取网页数量控制变量
		count = 1;
		
		# 判断是否存在未爬取的新的url
# 		while self.database.getUrlByNotCraw() != 'no':
		try:
				# 获取一个未爬取的url
# 				new_url = self.database.getUrlByNotCraw()
				print('craw %d : %s' % (count, root_url))
				# 使用html页面下载器下载页面数据
				html_data = self.downloader.downloade(root_url)
				# 分析获取爬取页面的我们需要url与数据
				new_urls,new_data = self.parser.parse(root_url, html_data)
				# 输出我们爬取的页面数据
				self.outputer.collect_data(new_data)
				print('urls:' + new_urls)
# 				if count == 10000:
# 					break
# 				count = count + 1
			
		except :
				print('craw falied !!!')

if __name__ == '__main__':
		print('-------------' + 'craw start' + '-------------')
		for page in range(1, 21):
			root_url = 'https://www.cnblogs.com/cate/java/#p%d' % (page)
			url_type = 'java'
			obj_spider = SpiderMain()
			obj_spider.craw(root_url, url_type)
		print('-------------' + 'craw end' + '-------------')
