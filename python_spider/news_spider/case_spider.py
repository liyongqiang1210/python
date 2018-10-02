#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-08-24 10:49:19
# @Author  : Li Yongqiang
# @Version : 0.0.1

"""
    裁判文书网法院爬虫
"""
import time
import random
import json
import pymysql
from spider import Spider
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains


class CourtSpider(Spider):
    """docstring for CourtSpider"""
    # 打开浏览器
    driver_path = 'E:\Program Files (x86)\python\Scripts\chromedriver.exe'
    driver = webdriver.Chrome(executable_path=driver_path)
    driver.get('http://wenshu.court.gov.cn/')
    # driver.maximize_window()  # 将浏览器最大化

    def get_index_html(self):
        
        html = self.driver.page_source  # 获取html页面
        soup = BeautifulSoup(html)
        citys = soup.find_all(class_="map_p");  # 获取所有省会城市的法院
        for city in citys:
            name = city['class'][1]  # 获取法院标签的class属性的唯一class名
            # print(name)
            city = self.driver.find_element_by_class_name(name)  # 根据唯一的class名获取到标签
            city.click()  # 点击标签
            time.sleep(random.randint(5, 10))  # 等待页面加载完成
            html = self.driver.page_source  # 获取到点击后的html页面
            self.get_no_base_court(html)  # 获取非基层法院
            
        driver.quit();

    # 获取非基层法院
    def get_no_base_court(self, html):
        highest_court_list = []  # 最高级法院
        high_court_list = []  # 高级法院
        middle_court_list = []  # 中级法院
        province_id = ""  # 省id
        # 开始解析页面
        soup = BeautifulSoup(html)
        court_html = soup.find(class_="region")  # 获取中高级法院,最高法院html
        courts_soup = BeautifulSoup(str(court_html))
        # 筛选出非基础法院信息标签
        court_element_list = courts_soup.find_all(attrs={"target": "_blank"})  # 获取法院标签
        for court_element in court_element_list:
            city_id = ""  # 城市id
            court_name = court_element.get_text()  # 获取到中高级，高级法院名
            
            # 判断法院类型
            if "最高" in court_name:  # 最高级
                highest_court_list.append(court_name)
                # 插入数据
                # self.insert_court(highest_court_list, 1, "110000", "", "")
            elif "高级" in court_name:  # 高级
                # 获取省id
                province_name = str(court_name)[:-6]
                province_id = self.select_province_id(province_name)
                court = {'court_name': court_name,'province_id': province_id, 'city_id':'','area_id':'','court_level':2}
                # 插入数据
                high_court_list.append(court)
                # 中级法院
                high_court_json = json.dumps(high_court_list)
#                 self.insert_court(high_court_list, 2, province_id, "", "")
            else:  # 中级
                if court_name[0:2] not in "北京市上海市天津市重庆市":
                    # 获取城市id
                    length = len(province_name)
                    city_name = str(court_name)[length:-6]
                    city_id = self.select_city_id(city_name)
                else:
                    # 获取城市id
                    city_name = court_name[0:3]
                    city_id = self.select_province_id(city_name)
                
                court = {'court_name': court_name,'province_id': province_id, 'city_id':city_id,'area_id':'','court_level':3}
                # 插入数据
                middle_court_list.append(court)
                # 中级法院print("中级法院：" + middle_court_json)
                middle_court_json = json.dumps(middle_court_list)
#                 self.insert_court(middle_court_list, 3, province_id, city_id, "")
                
                # 获取基层法院信息
                try:
                    # 获取到鼠标需要悬停地方的标签
                    court_link = self.driver.find_element_by_xpath('//a[@href="/List/List?sorttype=1&conditions=searchWord+' + court_name + '+++中级法院:' + court_name + '"]')
                    # 获取基层法院
                    ActionChains(self.driver).move_to_element(court_link).perform()  # 鼠标悬停到当前法院标签上
                    # 获取到带有基层法院标签内容的html
                    html = self.driver.page_source
                    # 获取当前法院的下属基层法院
                    self.get_base_html(html, province_id, city_id, city_name)
                except Exception as e:
                    print(e)
#         print("中级法院：" + middle_court_json)
#         print("高级法院：" + high_court_json)
        self.insert_court(high_court_json)
        self.insert_court(middle_court_json)
            
                    
        # 刷新页面
        self.driver.refresh()
        
    # 获取基层法院
    def get_base_html(self, html, province_id, city_id, city_name):
        base_court_list = []  # 基层法院
        base_court_name = ""
        # 城市名字长度
        length = len(city_name)
        # 开始解析页面
        soup = BeautifulSoup(html)
        try:
            base_court_list_li = soup.find_all("li", class_="divarealihide")
            if len(base_court_list_li) != 0:
                # 获取基层法院
                for base_court in base_court_list_li:
                    court_name = base_court.get_text()
                    # 区县名字
                    area_name = str(base_court_name)[length:-4]
                    # 根据区县名字获取区县id
                    area_id = self.select_area_id(area_name)
                    court = {'court_name': court_name,'province_id': province_id, 'city_id': city_id,'area_id':area_id,'court_level':4}
                    base_court_list.append(court)
                    # 基层法院
                base_court_json = json.dumps(base_court_list)
                self.insert_court(base_court_json)
                # print("基层法院：" + base_court_json)
        except Exception as e:
            print(e)
            
    # 插入法院信息的方法
    def insert_court(self, court_json):

        # 打开数据连接
        conn = pymysql.connect(host='127.0.0.1', user='root',
                password='root', database='lyq_db', charset='utf8')
        # 使用cursor()方法创建一个游标对象cur
        cur = conn.cursor()
        # 插入语句
        insert_sql = "insert into courts(court_name, court_level, court_province_id, court_city_id, court_area_id) values "
        i = 1
        for court in json.loads(court_json):
            if i == len(json.loads(court_json)):
                insert_sql += '("%s",%d,"%s","%s","%s");' % (court['court_name'], court['court_level'], court['province_id'], court['city_id'], court['area_id'])
            else:
                insert_sql += '("%s",%d,"%s","%s","%s"),' % (court['court_name'], court['court_level'], court['province_id'], court['city_id'], court['area_id'])
            i = i + 1
        
        try:
            print(insert_sql)
            cur.execute(str(insert_sql))
            conn.commit()
            print('===================> 插入成功')
        except Exception as e:
            conn.rollback()
            print('===================> 插入失败' + e)
            
        cur.close()  # 关闭查询
        conn.close()  # 关闭数据库连接
    
    # 根据省名获取省id
    def select_province_id(self, province_name):
        province_id = ""
        # 打开数据连接
        conn = pymysql.connect(host='127.0.0.1', user='root',
                password='root', database='lyq_db', charset='utf8')
        # 使用cursor()方法创建一个游标对象cur
        cur = conn.cursor()
        # 查询语句 
        select_sql = "select provinceid from provinces where province = '%s'" % (province_name)
        try:
            cur.execute(select_sql)
            # 获取所有记录列表
            results = cur.fetchall()
            for row in results:
               province_id = row[0]
        except Exception as e:
            print(e)
        
        cur.close()
        conn.close()
        
        return province_id
    
    # 根据城市名获取城市id
    def select_city_id(self, city_name):
        city_id = ""
        # 打开数据连接
        conn = pymysql.connect(host='127.0.0.1', user='root',
                password='root', database='lyq_db', charset='utf8')
        # 使用cursor()方法创建一个游标对象cur
        cur = conn.cursor()
        # 查询语句 
        select_sql = "select cityid from cities where city = '%s'" % (city_name)
        try:
            cur.execute(select_sql)
            # 获取所有记录列表
            results = cur.fetchall()
            for row in results:
               city_id = row[0]
        except Exception as e:
            print(e)
        
        cur.close()
        conn.close()
        
        return city_id
        
    # 根据区县名获取区县id
    def select_area_id(self, area_name):
        area_id = ""
        # 打开数据连接
        conn = pymysql.connect(host='127.0.0.1', user='root',
                password='root', database='lyq_db', charset='utf8')
        # 使用cursor()方法创建一个游标对象cur
        cur = conn.cursor()
        # 查询语句 
        select_sql = "select areaid from areas where area = '%s'" % (area_name)
        try:
            cur.execute(select_sql)
            # 获取所有记录列表
            results = cur.fetchall()
            for row in results:
                   area_id = row[0]
        except Exception as e:
            print(e)
        
        cur.close()
        conn.close()
        
        return area_id


if __name__ == '__main__':
    cs = CourtSpider();
    cs.get_index_html();
    
