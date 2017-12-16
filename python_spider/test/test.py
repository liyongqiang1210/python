# coding=utf-8

'''

Created on 2017年12月4日

 

@author: Li Yongqiang

'''
import pymysql


class Test(object):
    if __name__ == '__main__':
        for i in range(21):
            conn = pymysql.connect(host='127.0.0.1', user='root', password='root', database='maven')
            cur = conn.cursor()
            sql_select = 'select DISTINCT url from url_list LIMIT %d,%d' % (i*10000,10000)
            sql_insert = 'insert into baike_url_list(url,is_craw)values(%s,0)'
            list = cur.execute(sql_select)
            res = cur.fetchall()
            for li in res:
                cur.execute(sql_insert,(li[0]))
            conn.commit()
            cur.close()
            conn.close()

