#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-08-24 10:49:19
# @Author  : Li Yongqiang
# @Version : 0.0.1

"""
    新浪微博爬虫
"""
import time
from spider import Spider
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By


class WeiBoSpider(Spider):
    """docstring for WeiBoSpider"""

    def get_weibo_html(self):
        driver = self.open_driver()
        driver.get('https://weibo.com/')
        html = driver.page_source
        print(html)
        self.close_driver()

    def get_cookie_from_weibo(self, username, password):

        driver_path = 'E:\Program Files (x86)\python\Scripts\chromedriver.exe'
        driver = webdriver.Chrome(executable_path=driver_path)
        driver.get('https://weibo.com/')
        driver.maximize_window()#将浏览器最大化
        time.sleep(10) # 等待10s等待浏览器加载页面
        username_elem = driver.find_element_by_name('username') # 根据name属性找到用户名输入框
        username_elem.send_keys(username) # 填写用户名
        password_elem = driver.find_element_by_name('password')
        password_elem.send_keys(password) # 填写密码
        login = driver.find_element_by_class_name("login_btn") # 根据class属性找到登录按钮
        login.click() # 点击登录按钮
        time.sleep(2)
        # 逐渐滚动浏览器窗口,使ajax逐渐加载
        for i in range(1, 30):
            # 将页面滚动条向下滚动
            js = 'var q=document.documentElement.scrollTop=' + str(1000 * i)
            # 执行js
            driver.execute_script(js)
            # 等待1s
            time.sleep(1)

        # print(driver.page_source)
        driver.quit()



if __name__ == '__main__':
    weibospider = WeiBoSpider()
    cookie = weibospider.get_cookie_from_weibo('18330902178', 'L18330902178')
