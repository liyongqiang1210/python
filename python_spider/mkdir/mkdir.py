'''
Created on 2018��1��5��
�����ļ��й���
@author: liyongqiang
'''
import os
class mkdir(object):
    def mkdirs(self,path):
        # ȥ����λ�ո�
        path = path.strip()
        # ȥ��β�� \ ����
        path = path.rstrip("\\")
        
        #�жϴ�����·���Ƿ���ڷ���true/false
        isExists = os._exists(path)
        
        #�жϽ��
        if isExists: #���ڲ�����
            print('Ŀ¼�Ѿ�����')
            return False
        else : #�������򴴽�
            os.makedirs(path)
            print('%s �����ɹ���'%(path))
            return True
        