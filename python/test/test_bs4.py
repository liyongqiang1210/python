# coding=utf-8

'''

Created on 2017年12月4日

 

@author: Li Yongqiang

'''
from bs4 import BeautifulSoup
from nt import link
import re
html_doc = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
"""
soup = BeautifulSoup(html_doc,"html.parser",from_encoding="utf-8")
print("获取所有的链接")
links = soup.find_all("a")
for link in links:
    print(link.name,link['href'],link.get_text())

print("获取指定的链接")
link_compile = soup.find('a',href=re.compile(r"ill"))
print(link_compile.name,link_compile['href'],link_compile.get_text())

print("获取p段落文字")
link_node = soup.find('p')
print(link_node.get_text())

