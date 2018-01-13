# coding=utf-8
'''
Created on 2018年1月10日
xici代理ip爬虫
@author: liyongqiang
'''
from urllib.request import Request, urlopen
from bs4 import BeautifulSoup
import re
from urllib import request

if __name__ == '__main__':
    
    http = []  # 存放http的集合
    
    url = 'http://www.xicidaili.com/nn'  # url地址
    req = Request(url)  # 发送请求
    
    
    # 模拟浏览器请求
    req.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:57.0) Gecko/20100101 Firefox/57.0')  # 个人主机信息 
    req.add_header('Get', url)  # url地址
    req.add_header('Host', 'www.xicidaili.com')  # 服务器地址
    req.add_header('Referer', 'http://www.xicidaili.com/nt/')  # 访问的网址
    
    html_cont = urlopen(req).read().decode('utf-8')  # 获取网页内容
    
    
    # 开始解析网页信息
    soup = BeautifulSoup(html_cont, 'html.parser')  # 创建soup对象
    tr_list = soup.find_all('tr')  # 匹配到tr标签返回的是一个列表
    
    
    # 开始遍历这个列表
    for li in tr_list :
        
        # 匹配出ip地址
        ip_r = re.compile(r'<td>\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3}</td>')  # 匹配ip地址的正则表达式
        ip = str(ip_r.findall(str(li)))[6:-7]  # 找到ip地址
        
        # 匹配出ip对应的端口号
        port_r = re.compile(r'<td>\d{1,6}</td>')  # 匹配端口号的正则
        port = str(port_r.findall(str(li)))[6:-7]  # 找到端口号
        if ip != '' and port != '' :
            ip_address = str(ip) + ':' + str(port)  # 完整的ip地址
            try :
                # 代理ip访问地址
                url = 'http://www.whatismyip.com.tw/'
                # 这是代理IP
                proxy = {'http':ip_address}
                # 创建ProxyHandler
                proxy_support = request.ProxyHandler(proxy)
                # 创建Opener
                opener = request.build_opener(proxy_support)
                # 添加User Angent
                opener.addheaders = [('User-Agent', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:57.0) Gecko/20100101 Firefox/57.0')]
                # 安装OPener
                request.install_opener(opener)
                # 使用自己安装好的Opener
                response = request.urlopen(url)
                print('ip地址:' + ip_address + '状态码:' + response.getcode() + '=========>可用')
                # 如果返回200则证明ip可用
                if response.getcode() == 200 :
                    http.append(object)
            except :
                print('ip地址:' + ip_address + '=========>无效')
                continue
    print(http)
            

    
    
    
    
