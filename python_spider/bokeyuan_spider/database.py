# coding=utf-8

'''

Created on 2017年12月12日

 连接数据库操作

@author: Li Yongqiang

'''
import pymysql


# 数据持久化类
class Database(object):

    # 插入url的方法
    def insertUrl(self, url, url_type, url_title):
        # 插入操作
        insert_sql = "INSERT INTO bokeyuan_url_list(url,url_type,url_title,is_craw)VALUES('%s','%s','%s',0)" % (url, url_type, url_title)
        while self.selectUrl(url):
            try:
                conn = pymysql.connect(host='39.106.154.2', user='root', password='root', database='maven')
                cur = conn.cursor()
                cur.execute(insert_sql)
                conn.commit()
                print(url + '----------插入成功')
            except:
                conn.rollback()
                print(url + '----------已存在')

            # 关闭查询
            cur.close()
            
            # 关闭数据库连接
            conn.close()                       

    # 查询数据库是否存在此url
    def selectUrl(self, url):
        conn = pymysql.connect(host='39.106.154.2', user='root', password='root', database='maven')
        cur = conn.cursor()
        # 查询数据库是否存在当条数据
        select_sql = "SELECT COUNT(ID) FROM bokeyuan_url_list WHERE url = '%s'" % (url)
        # 执行查询sql查询数据库是否存在此条数据
        cur.execute(select_sql)
        # 判断数据库是否存在此条记录
        res = cur.fetchone()[0] == 0
        # 关闭查询
        cur.close()
        
        # 关闭数据库连接
        conn.close()      
        return res

    # 从数据库获取一条未被爬取过的url
    def getUrlByNotCraw(self):
        conn = pymysql.connect(host='39.106.154.2', user='root', password='root', database='maven')
        cur = conn.cursor()
        # 查询数据库是否存在当条数据
        select_sql = 'SELECT url FROM bokeyuan_url_list WHERE is_craw = 0 limit 1'
        # 执行查询sql查询数据库是否存在未爬取数据
        cur.execute(select_sql)
        res = cur.fetchone()[0]
        # 关闭查询
        cur.close()
        
        # 关闭数据库连接
        conn.close()      
        # 如何数据库不存在未爬取的url我们将返回no
        if res == '':
            return 'no'
        else:
            return res

    # 更新爬取过的url的状态为1(已爬取)
    def updateUrl(self, url):
        conn = pymysql.connect(host='39.106.154.2', user='root', password='root', database='maven')
        cur = conn.cursor()
        # 更新sql语句
        update_sql = "UPDATE bokeyuan_url_list SET is_craw = 1 WHERE url = '%s'" % (
            url)
        try:
            cur.execute(update_sql)
            # 事务提交
            conn.commit()
            print(url + ' --------状态已更新为已爬取状态')
        except Exception as e:
            print('-------更新异常 : ' + e)
            # 事务回滚
            conn.rollback()
        # 关闭查询
        cur.close()
        
        # 关闭数据库连接
        conn.close()      

