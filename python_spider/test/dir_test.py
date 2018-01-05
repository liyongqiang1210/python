# coding=utf-8

'''
Created on 2017年12月29日

@author: liyongqiang
'''
import os
class Dir_test(object):
    def mkdirs(self,path):
        path = path.strip()
        path = path.rstrip("\\")
        
        print(path)
        
        #判断创建的路径是否存在
        isExists = os._exists(path)
        
        #判断结果
        if isExists: #存在不创建
            print('目录已经存在')
            return False
        else : #不存在则创建
            os.makedirs(path)
            print('%s 创建成功！'%(path))
            return True
        
if __name__ == '__main__':
    test = Dir_test()
    test.mkdirs("e:\\dir\\dir")

