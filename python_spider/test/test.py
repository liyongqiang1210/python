# coding=utf-8
'''
Created on 2017年12月4日
爬取51cto视频链接与视频名
@author: Li Yongqiang
'''
from urllib import request
from bs4 import BeautifulSoup
import re
class Test(object):
    if __name__ == '__main__':
#         http = ['203.174.112.13:3128', '222.92.141.250:80']  # 可用的代理ip地址
#         #这是代理IP
#         proxy = {'http':'203.174.112.13:3128'}
#         #创建ProxyHandler
#         proxy_support = request.ProxyHandler(proxy)
#         #创建Opener
#         opener = request.build_opener(proxy_support)
#         #添加User Angent
#         opener.addheaders = [('User-Agent','Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:57.0) Gecko/20100101 Firefox/57.0')]
#         #安装OPener
#         request.install_opener(opener)
        # 访问网址
        url = 'http://edu.51cto.com/center/course/index/list?wwwdh=&page='

        # 使用自己安装好的Opener访问网址
        for i in range(1, 189):
            print('==================>第' + str(i) + '页开始')
            response = request.urlopen(url + str(i))
            # 读取相应信息并解码
            if response.getcode() == 200 :  # 判断
                html_cont = response.read().decode('utf-8')  # 获取网页内容
            # 创建soup对象开始分析网页
            soup = BeautifulSoup(html_cont, 'html.parser', from_encoding='utf-8')  # 创建soup对象
            video_list = soup.find_all('div', class_='cList_Item')  # 视频信息列表
            
            # 遍历视频列表
            for video in video_list:
                video_soup = BeautifulSoup(str(video), 'html.parser')
                tag = video_soup.find('a', title=re.compile(r'([\u4E00-\u9FA5\s]|-|\S|.)+')) 
                video_url = tag['href']  # 视频url 
                video_title = tag['title']  # 视频title
                video_classHour = video_soup.find('p', class_='fl').string  # 视频课时
                video_number = video_soup.find('p', class_='fr').string  # 视频学习人数
                video_price = video_soup.find('h4').string  # 视频价格
                print('视频url =======>%s\n视频title ========>%s\n视频价格 ========>%s\n视频课时 ========>%s\n视频学习人数 ========>%s' 
                      % (video_url, video_title, video_price, video_classHour, video_number))
            
            print('==================>第' + str(i) + '页结束')    
