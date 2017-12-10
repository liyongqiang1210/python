# coding=utf-8


'''

Created on 2017年12月4日

 

@author: Li Yongqiang

'''

from urllib.request import Request
from urllib.request import urlopen

url = "http://baike.baidu.com/view/100000.htm"

# print("第一种方法")
# response1 = urlopen(url)
# print(response1.getcode())
# print(response1.read())

print("第二种方法")
request = Request(url)
request.add_header("user-agent","Mozilla/6.0")
response2 = urlopen(request)
print(response2.getcode())
print(response2.read().decode('utf-8'))


