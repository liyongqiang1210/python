#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-08-24 10:49:19
# @Author  : Li Yongqiang
# @Version : 0.0.1

"""
    新浪微博爬虫
"""

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
		driver.get("https://weibo.com/")
		html = driver.page_source
		print(html)
		self.close_driver()

	def get_cookie_from_weibo(self, username, password):
		global driver
		# chrome浏览器驱动，无头模式
		chrome_options = Options()
		chrome_options.add_argument('--headless')
		chrome_options.add_argument('--disable-gpu')
		# 本地chormedriver.exe文件目录
		driver_path = 'E:\Program Files (x86)\python\Scripts\chromedriver.exe'
		driver = webdriver.Chrome(
			chrome_options=chrome_options, executable_path=driver_path)
		driver.get('https://weibo.cn')
		assert "微博" in driver.title
		login_link = driver.find_element_by_link_text('登录')
		ActionChains(driver).move_to_element(login_link).click().perform()
		login_name = WebDriverWait(driver, 10).until(
			EC.visibility_of_element_located((By.ID, "loginName"))
		)
		login_password = driver.find_element_by_id("loginPassword")
		login_name.send_keys(username)
		login_password.send_keys(password)
		login_button = driver.find_element_by_id("loginAction")
		login_button.click()
		cookie = driver.get_cookies()
		print(driver.page_source)
		driver.close()
		return cookie


if __name__ == '__main__':
	weibospider = WeiBoSpider()
	cookie = weibospider.get_cookie_from_weibo("18330902178","L18330902178")
	print(cookie)