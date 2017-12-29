# coding=utf-8

'''
Created on 2017��12��29��

@author: liyongqiang
'''
from urllib.request import urlopen
class Url_test(object):
    if __name__ == '__main__':
        url = 'https://v12.51cto.com/2017/07/29/74183/aaa2/general/loco_video_267000_0.ts'
        res =  urlopen(url)
        print(res.getcode())

