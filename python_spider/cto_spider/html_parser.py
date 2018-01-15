#!/usr/bin/python3.6
# coding=utf-8

'''

Created on 2017年1月9日

 

@author: Li Yongqiang

'''
from bs4 import BeautifulSoup
import re
from cto_spider.database import Database


class HtmlParsesr(object):

    # 获取页面的url集合
    def _get_new_urls(self, soup, video_id):
        
        # url格式：'http://edu.51cto.com/center/course/lesson/index?id=12263'
        links = soup.find_all('a', href=re.compile(r'/center/course/lesson/index\?id=\d{5}'))  # 匹配到合适的url
        for link in links:
            course_url = link['href']  # 课程url
            course_title = link['title']  # 课程title
            Database.insertCourseUrl(self, course_url, course_title, video_id)
            print('title=======>' + course_title + '\nurl地址=======>' + course_url)
        
    def parse(self, video_id, html_cont):
        
        if video_id is None:
            return
        else:
            soup = BeautifulSoup(html_cont, 'html.parser', from_encoding='utf-8')
            new_urls = self._get_new_urls(soup, video_id)
            return new_urls
