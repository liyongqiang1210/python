'''
Created on 2018��1��5��
python��ά�Զ�����Ƶ
@author: liyongqiang
'''
from urllib.request import urlopen
from _io import open


class Test(object):
    if __name__ == '__main__':
        # ����Ƶ�ʸߵ��ַ�
        character = ['a', 'b', 'c', 'd', 'e', 'f', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        # ����
        host = ['v12.51cto.com', 'v15.51cto.com', 'v4.51cto.com', 'v5.51cto.com']
        # ����
        number = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        # https://v4.51cto.com/part/2017/06/05/47667/1763/high/loco_video_556000_2.ts
        # �����url
        url = ''
        # ����i
        i = 0
        # ����һ��txt�ļ�����url���뵽�ļ���
        try:
            txt = open('url.txt', 'w')
            # ���ѭ������https://�������
            for h in host:
                url = 'https://' + h + '/2017/07/29/74183/'
                # https://v12.51cto.com/2017/07/29/74183/�����λ����ַ�
                for char in character:
                    url1 = url + char
                    for char1 in character:
                        url2 = url1 + char1
                        for char2 in character:
                            url3 = url2 + char2
                            for char3 in character:
                                # �µ�url
                                new_url = url3 + char3 + '/general/loco_video_198000_0.ts'
                                # �����url.txt�ļ�
                                txt.write(new_url + '\n')
                                # ��ʼ������ҳ
                                response = urlopen(url)
                                if response.getcode() != 200:
                                    i = i + 1
                                    print('���������%d' % (i))
                                else:
                                    print(response.getcode())
                                    print('url��ַ��%s' % (url))
                                    break
            # �ر������
            txt.close()
        except :
            print('�쳣')
