'''
Created on 2018年1月5日
python运维自动化视频
@author: liyongqiang
'''
from urllib.request import urlopen
from _io import open


class Test(object):
    if __name__ == '__main__':
        # 出现频率高的字符
        character = ['a', 'b', 'c', 'd', 'e', 'f', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        # 域名
        host = ['v12.51cto.com', 'v15.51cto.com', 'v4.51cto.com', 'v5.51cto.com']
        # 数字
        number = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        # https://v4.51cto.com/part/2017/06/05/47667/1763/high/loco_video_556000_2.ts
        # 请求的url
        url = ''
        # 变量i
        i = 0
        # 创建一个txt文件并把url输入到文件中
        try:
            txt = open('url.txt', 'w')
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
                                # 新的url
                                new_url = url3 + char3 + '/general/loco_video_198000_0.ts'
                                # 输出到url.txt文件
                                txt.write(new_url + '\n')
                                # 开始请求网页
                                response = urlopen(url)
                                if response.getcode() != 200:
                                    i = i + 1
                                    print('请求次数：%d' % (i))
                                else:
                                    print(response.getcode())
                                    print('url地址：%s' % (url))
                                    break
            # 关闭输出流
            txt.close()
        except :
            print('异常')
