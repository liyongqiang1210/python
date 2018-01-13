# coding=utf-8
'''
Created on 2017年12月4日
代理ip测试
@author: Li Yongqiang
'''
from urllib import request

class Test(object):
    if __name__ == '__main__':
        http = ['203.174.112.13:3128', '222.92.141.250:80']  # 可用的代理ip地址
        # 这是代理IP
        proxy = {'http':'203.174.112.13:3128'}
        # 创建ProxyHandler
        proxy_support = request.ProxyHandler(proxy)
        # 创建Opener
        opener = request.build_opener(proxy_support)
        # 添加User Angent
        opener.addheaders = [('User-Agent', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:57.0) Gecko/20100101 Firefox/57.0')]
        # 安装OPener
        request.install_opener(opener)
        # 访问网址
        url = 'http://edu.51cto.com/center/course/index/list?wwwdh=&page='
        # 使用自己安装好的Opener访问网址
        response = request.urlopen(url)
        print(response.getcode())
