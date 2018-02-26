# coding=utf-8
'''
Created on 2018年2月23日

@author: liyongqiang
'''
from urllib.request import Request, urlopen
from bs4 import BeautifulSoup
from urllib import request

if __name__ == '__main__':
    
    # 发送请求
    req = Request('http://www.xicidaili.com')
    # 模拟浏览器
    req.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:57.0) Gecko/20100101 Firefox/57.0')
    
    res = urlopen(req)
    
    if res.getcode() == 200 :
        # 获取html页面信息
        html_doc = res.read().decode('utf-8')
        

    # 分析html页面
    soup = BeautifulSoup(html_doc, 'html.parser', from_encoding='utf-8')
    # 获取tr标签集合
    trs = soup.find_all('tr',attrs={'class':'odd'})
    for tr in trs:
        # 获取td标签集合
        tds = tr.find_all('td')
        # ip地址
        ip_address = tds[1].string
        # 端口号
        port = tds[2].string
        # 服务器地址
        server_address = tds[3].string
        # 是否匿名
        is_anonymous = tds[4].string
        # 协议类型
        ip_type = tds[5].string
        
        # 测试ip是否能用
        if ip_address != '' and port != '' :
            ip_address = 'http://' + str(ip_address) + ':' + str(port)  # 完整的ip地址
            try :
                # 代理ip访问地址
                url = 'https://www.baidu.com/'
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
                print(response.info())
                # 如果返回200则证明ip可用
                if response.getcode() == 200 :
                    print('ip地址:' + ip_address + '=========>可用')
                else:
                    print('ip地址:' + ip_address + '=========>不可用')
            except :
                print('异常')
                continue
        
         
        
