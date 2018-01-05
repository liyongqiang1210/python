# coding=utf-8

'''
Created on 2017年12月29日

@author: liyongqiang
'''
from urllib.request import urlopen
class Url_test(object):
    if __name__ == '__main__':
        url = 'https://v4.51cto.com/part/2017/06/05/47667/1763/high/loco_video_556000_2.ts'
        res =  urlopen(url)
        print(res.getcode())

