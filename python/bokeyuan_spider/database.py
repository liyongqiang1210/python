# coding=utf-8

'''

Created on 2017年12月12日

 连接数据库操作

@author: Li Yongqiang

'''
import pymysql


# 数据持久化类
class Database(object):

    # 初始化变量
    def __init__(self):
        # 打开数据连接
        self.conn = pymysql.connect(
            host='39.106.154.2', user='root', password='root', database='maven')
        # 使用cursor()方法创建一个游标对象cur
        self.cur = self.conn.cursor()

    # 插入url的方法
    def insertUrl(self, url, url_type, url_title):
        # 插入操作
        insert_sql = 'INSERT INTO bokeyuan_url_list(url,url_type,url_title,is_craw)VALUES(%s,%s,%s,0)'
        try:
            while self.selectUrl(url):
                self.cur.execute(insert_sql, [url_type, url_title])
                self.conn.commit()
                print(url + '-' * 10 + '插入成功')
        except:
            self.conn.rollback()
            print(url + '-' * 10 + '插入失败')

        # 关闭查询
        self.cur.close()

        # 关闭数据库连接
        self.conn.close()

    # 查询数据库是否存在此url
    def selectUrl(self, url):
        # 查询数据库是否存在当条数据
        select_sql = 'SELECT COUNT(ID) FROM bokeyuan_url_list WHERE url = %s' % (url)
        # 执行查询sql查询数据库是否存在此条数据
        self.cur.execute(select_sql)
        # 判断数据库是否存在此条记录
        res = self.cur.fetchone()[0] != ''
        return res

    # 从数据库获取一条未被爬取过的url
    def getUrlByNotCraw(self):
        # 查询数据库是否存在当条数据
        select_sql = 'SELECT url FROM bokeyuan_url_list WHERE is_craw = 0 limit 1'
        # 执行查询sql查询数据库是否存在未爬取数据
        self.cur.execute(select_sql)
        res = self.cur.fetchone()[0]
        # 如何数据库不存在未爬取的url我们将返回no
        if res == '':
            return 'no'
        else:
            return res

    # 更新爬取过的url的状态为1(已爬取)
    def updateUrl(self, url):
        # 更新sql语句
        update_sql = 'UPDATE bokeyuan_url_list SET is_craw = 1 WHERE url = %s' % (
            url)
        try:
            self.cur.execute(update_sql)
            # 事务提交
            self.conn.commit()
            print(url + ' --------状态已更新为已爬取状态')
        except Exception as e:
            print('-------更新异常 : ' + e)
            # 事务回滚
            self.conn.rollback()
# if __name__ == '__main__':
#         data = Database()
#         url = data.getUrlByNotCraw()
#         print(url)