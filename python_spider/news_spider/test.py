#!/usr/bin/python3.6
# coding=utf-8

import time
import datetime
import random

def job():
	print(time.asctime(time.localtime(time.time())))

if __name__ == '__main__':
	
	# print(datetime.datetime.now().year)
	# schedule.every(1).minutes.do(job)

	# while True:
	# 	schedule.run_pending()
	# print(random.randint(1,9) * 0.1) # 随机数

	# 写入文件操作
	file_name = 'cookies.json'
	# my_open = open(file_name, 'w')
	# #打开fie_name2路径下的my_write.txt文件,采用写入模式
	# #若文件不存在,创建，若存在，清空并写入
	# my_open.write('one\ntwo\n')
	# #在文件中写入一个字符串
	# my_open.write('three\n')
	# my_open.close()

	##检查是否正确写入
	my_open = open(file_name, 'r')
	#读取file_name2路径下的my_write.txt文件
	my_infor = my_open.readlines()
	my_open.close()
	print(my_infor)

	
