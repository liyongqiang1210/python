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
    def insertUrl(self, url) :
            # 打开数据连接
            conn = pymysql.connect(host='39.106.154.2', user='root', password='root', database='maven')
            # 使用cursor()方法创建一个游标对象cur
            cur = conn.cursor()
            # 查询数据库是否存在当条数据
            select_sql = "SELECT COUNT(ID) FROM baike_url_list WHERE URL = '%s'" % (url)
            # 插入操作
            insert_sql = "INSERT INTO baike_url_list(URL,IS_CRAW)VALUES('%s',%d)" % (url , 0)
            try:
                # 执行查询sql查询数据库是否存在此条数据
                cur.execute(select_sql)
                res = cur.fetchone()[0]
                if res < 1:
                    res = cur.execute(insert_sql)
                    conn.commit()
                    print('url:%s' % (url) + ' 插入成功---------------')
                else:
                    print('url:%s' % (url) + ' 已存在----------------')
            except:
                conn.rollback()
                print('url:%s' % (url) + ' Error: 插入数据失败')
                
            # 关闭查询
            cur.close()
            # 关闭数据库连接
            conn.close()
    
    # 获取一条未爬取的url
    def selectUrlNoCraw(self) :
        conn = pymysql.connect('39.106.154.2', 'root', 'root', 'maven')
        cur = conn.cursor()
        select_sql = 'select url from baike_url_list where is_craw = 0 limit 1'
        try:
            cur.execute(select_sql)
            res = cur.fetchone()[0]
            print('获取到的url: %s' % (res))
            update_sql = "update baike_url_list set is_craw = 1 where url = '%s'" % (res)
            cur.execute(update_sql)
            conn.commit()
            return res
        except:
            conn.rollback()
            print('selectUrlNoCraw Error')
        return ''
