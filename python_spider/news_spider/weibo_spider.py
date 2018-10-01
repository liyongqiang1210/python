#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-08-24 10:49:19
# @Author  : Li Yongqiang
# @Version : 0.0.1

"""
    新浪微博爬虫
"""
import time
import random
import json
from spider import Spider
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


class WeiBoSpider(Spider):
    """docstring for WeiBoSpider"""

    def get_weibo_html(self):
        driver = self.open_driver()
        driver.get('https://weibo.com/')
        html = driver.page_source
        print(html)
        self.close_driver()

    # 获取cookies保存到指定文件中
    def get_cookies(self, username, password):
        # 打开浏览器
        driver_path = 'E:\python\Scripts\chromedriver.exe'
        driver = webdriver.Chrome(executable_path=driver_path)
        driver.get('https://weibo.com/')
        driver.maximize_window()#将浏览器最大化
        time.sleep(10) # 等待10s等待浏览器加载页面

        username_elem = driver.find_element_by_name('username') # 根据name属性找到用户名输入框
        username_elem.send_keys(username) # 填写用户名
        password_elem = driver.find_element_by_name('password')
        password_elem.send_keys(password) # 填写密码
        login = driver.find_element_by_class_name('login_btn') # 根据class属性找到登录按钮
        login.click() # 点击登录按钮
        time.sleep(1)

        # 获取登录后的cookies
        cookies = driver.get_cookies()
        json_cookies = json.dumps(cookies)
        # 登录完成后，将cookie保存到本地文件
        with open('cookies.json', 'w') as f:
            f.truncate() # 清空文件中内容
            f.write(json_cookies)

        driver.quit()

    def get_weibo_html(self):

        driver_path = 'E:\python\Scripts\chromedriver.exe'
        driver = webdriver.Chrome(executable_path=driver_path)
        driver.get('https://baidu.com/') # 随便打开一个网页
        time.sleep(2) # 等待2s等待浏览器加载页面

        # 删除第一次建立连接时的cookie
        driver.delete_all_cookies()
        # 读取登录时存储到本地的cookie
        with open('cookies.json', 'r', encoding='utf-8') as f:
            cookies_list = json.loads(f.read())
        for cookies in cookies_list:
            driver.add_cookie({
                'domain': '.weibo.com',  # 此处xxx.com前，需要带点
                'name': cookies['name'],
                'value': cookies['value'],
                'path': '/',
                'expires': None
            })

        # 请求登录后的微博页面
        driver.get('https://weibo.com/u/5379876310/home?wvr=5&lf=reg')
        # 逐渐滚动浏览器窗口,使ajax逐渐加载
        for i in range(1, 100):
            try:
                # 查看更多按钮
                more_click = driver.find_element_by_class_name('WB_cardmore WB_cardmore_noborder clearfix')
                more_click.click()
                # 将页面滚动条向下滚动900-1100的随机长度
                js = 'var q=document.documentElement.scrollTop=' + str(random.randint(900,1100) * i)
                # 执行js
                driver.execute_script(js)
                # 随机等待0.1-2s
                time.sleep(random.randint(0, 9) * 0.3)
            except Exception as e:
                # 将页面滚动条向下滚动900-1100的随机长度
                js = 'var q=document.documentElement.scrollTop=' + str(random.randint(900,1100) * i)
                # 执行js
                driver.execute_script(js)
                # 随机等待0.1-2s
                time.sleep(random.randint(0, 9) * 0.3)
            
            print(i)

        time.sleep(60)
        # 获取html页面内容
        html = driver.page_source

        driver.quit() # 退出浏览器
        return html

    # 解析html页面
    def parser_html(self, html):

        soup = BeautifulSoup(html, 'html.parser')
        div_list = soup.find_all('div', class_='WB_feed_detail') # 微博列表
        for div in div_list:
            print(div)
            # wb_nick_name = div.find('a', class_='W_f14 W_fb S_txt1') # 微博昵称
            # wb_content = div.find('div', class_='WB_text W_f14') # 微博内容

            



if __name__ == '__main__':
    weibospider = WeiBoSpider()
    # weibospider.get_cookies('18330902178', 'L18330902178')
    html = weibospider.get_weibo_html()
    # weibospider.parser_html(html)

