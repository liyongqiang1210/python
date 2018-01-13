# coding=utf-8
'''
Created on 2017年12月4日
爬取51cto视频链接与视频名
@author: Li Yongqiang
'''
from urllib import request
from bs4 import BeautifulSoup
import re
import time
from cto_spider.database import Database

class Test(object):
    
    if __name__ == '__main__':

        db = Database() # 创建database对象
        
        url = 'http://edu.51cto.com/center/course/index/list?wwwdh=&page=' # 爬取的网址
       
        for i in range(1, 189): # 循环遍历所有网址
            
            print('==================>第' + str(i) + '页开始')
            response = request.urlopen(url + str(i)) # 获取响应信息
            
            if response.getcode() == 200 :  # 判断
                html_cont = response.read().decode('utf-8')  # 获取网页内容
                
            soup = BeautifulSoup(html_cont, 'html.parser', from_encoding='utf-8')  # 创建soup对象
            video_list = soup.find_all('div', class_='cList_Item')  # 视频信息列表
           
            for video in video_list: # 遍历视频列表
                
                video_soup = BeautifulSoup(str(video), 'html.parser')  # 创建soup对象
                video_a = video_soup.find('a', title=re.compile(r'([\u4E00-\u9FA5\s]|-|\S|.)+'))  # 获取a标签列表
                video_url = video_a['href']  # 视频url 
                video_title = video_a['title']  # 视频title
                video_classHour = video_soup.find('p', class_='fl').string  # 视频课时
                video_number = video_soup.find('p', class_='fr').string  # 视频学习人数
                video_price = video_soup.find('h4').string  # 视频价格
                
                print('视频url =======>%s\n视频title ========>%s\n视频价格 ========>%s\n视频课时 ========>%s\n视频学习人数 ========>%s' 
                      % (video_url, video_title, video_price, video_classHour, video_number))
                
                db.insertCouserUrl(video_url, video_title, video_classHour, video_number, video_price) # 将数据存储到数据库
                
            time.sleep(10)  # 休眠10秒
            
            print('==================>第' + str(i) + '页结束')    
