#!/usr/bin/python3.6
# coding=utf-8

'''

Created on 2017年1月9日

 网页下载模块

@author: Li Yongqiang

'''
from urllib.request import Request, urlopen


class HtmlDownloader(object):
    
    def downloade(self, url):
        if url is None:
            return None
        
        req = Request(url)  # 发送请求
        
        # 模拟浏览器访问页面
        req.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:57.0) Gecko/20100101 Firefox/57.0')  # 个人主机的信息User-Agent
        req.add_header('Get', url)  # 告诉浏览器我们访问的网址
        req.add_header('Host', 'edu.51cto.com')  # 网站的信息在浏览器开发者工具中找这个信息
        req.add_header('Referer', 'http://edu.51cto.com/courselist/index.html?wwwdh')  # 告诉网站服务器我们是在哪找到要访问的网页的
        response = urlopen(req)  # 获取网站的响应信息
        if response.getcode() != 200:  # 判断请求是否成功，成功返回网页信息/失败返回None
            return None
         
        return response.read().decode('utf-8')

