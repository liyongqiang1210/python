# coding=utf-8
'''
Created on 2018年1月5日
创建文件夹工具
@author: liyongqiang
'''
import os
class mkdir(object):
    
    # 创建文件夹的方法
    def mkdirs(self, path):
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
        
        