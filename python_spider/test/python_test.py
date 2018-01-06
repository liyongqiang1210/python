# coding=utf-8
'''
Created on 2018年1月5日
python运维自动化视频
@author: liyongqiang
'''
from _io import open
import time
import os


class Test(object):
    
    # https://v4.51cto.com/part/2017/06/05/47667/1763/high/loco_video_556000_2.ts
    if __name__ == '__main__':
        # 出现频率高的字符
        character = ['a', 'b', 'c', 'd', 'e', 'f', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        # 域名
        host = ['v12.51cto.com', 'v15.51cto.com', 'v4.51cto.com', 'v5.51cto.com']
        # 数字
        number = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        
        try:
            # 获取当前日期
            date = time.strftime('%Y%m%d', time.localtime())
            # 存放url文件的路径
            path = 'G:\\url\\' + date
            # 去除首位空格
            path = path.strip()
            # 去除尾部 \ 符号
            path = path.rstrip("\\")
            # 判断创建的路径是否存在返回true/false
            isExists = os.path.exists(path)
            # 判断结果
            if isExists:  # 目录存在
                print('目录已经存在')
            else :  # 目录不存在则创建
                os.makedirs(path)
                print('%s 创建成功！' % (path))
            # 获取当前时间用作url的文件名
            time = time.strftime('%H%M%S', time.localtime())
            # 创建一个txt文件并把url输入到文件中
            txt = open(path + '\\' + time + '.txt', 'w')
            
            print('url开始创建...')
            # 这层循环的是https://后的域名
            for h in host:
                url = 'https://' + h + '/2017/07/29/74183/'
                # https://v12.51cto.com/2017/07/29/74183/后的四位随机字符
                for char in character:
                    url1 = url + char
                    for char1 in character:
                        url2 = url1 + char1
                        for char2 in character:
                            url3 = url2 + char2
                            for char3 in character:
                                url4 = url3 + char3 + '/general/loco_video_'
                                for num in number:
                                    url5 = url4 + num
                                    for num1 in number:
                                        url6 = url5 + num1
                                        for num2 in number:
                                            # url
                                            new_url = url6 + num2 + '000_0.ts'
                                            # 输出到url.txt文件
                                            txt.write(new_url + '\n')
            print('url创建结束')
            # 关闭输出流
            txt.close()
        except :
            print('异常')
