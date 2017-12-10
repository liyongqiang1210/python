# coding=utf-8

'''

Created on 2017年12月6日

 爬取的数据持久化

@author: Li Yongqiang

'''
import pymysql


# 数据持久化类
class Database(object): 

    # 插入url的方法
    def insertUrl(self, new_full_url) :
            # 打开数据连接
            conn = pymysql.connect(host='127.0.0.1', user='root', password='root', database='maven')
            # 使用cursor()方法创建一个游标对象cur
            cur = conn.cursor()
            # 查询数据库是否存在当条数据
            select_sql = 'SELECT COUNT(ID) FROM URL_LIST WHERE URL = (%s)'
            # 插入操作
            insert_sql = 'INSERT INTO URL_LIST(URL,IS_USE)VALUES(%s,%s)'
            try:
                # 执行查询sql查询数据库是否存在此条数据
                cur.execute(select_sql, [new_full_url])
                res = cur.fetchone()[0];
                if res < 1:
                    print('开始插入数据---------------')
                    print('url:%s' % (new_full_url))
                    res = cur.execute(insert_sql, [new_full_url, 0])
                    conn.commit()
                    print('插入数据成功---------------')
                else:
                    print('数据已存在')
            except:
                conn.rollback()
                print('Error: 插入数据失败')
                
            # 关闭查询
            cur.close()
            
            # 关闭数据库连接
            conn.close()
            return None
