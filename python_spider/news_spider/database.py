#!/usr/bin/python3.6
# coding=utf-8

'''

Created on 2017年1月9日

 爬取的数据持久化

@author: Li Yongqiang

'''
import pymysql


# 数据持久化类
class Database(object): 

    # 插入资讯的方法
    def insert_news(self,news_list):

        print(news_list)
        
        # 打开数据连接
        conn = pymysql.connect(host='127.0.0.1', user='root', 
                password='root', database='lyq_db', charset='utf8')
        # 使用cursor()方法创建一个游标对象cur
        cur = conn.cursor()
        # 插入语句
        insert_sql = "insert into news(news_title, news_content, news_image, \
                        news_release_time,news_type, news_url, news_website, create_time) values "
        i = 0
        for news in news_list:
            if i == len(news_list):
                insert_sql += str(insert_sql) + str(news) + ";"
            else:
                insert_sql += str(insert_sql) + str(news) + ","
            i = i+1
        
        try:
            print(insert_sql)
            # cur.execute(str(insert_sql))
            # conn.commit()
            print('===================> 插入成功')
        except Exception as e:
            conn.rollback()
            print('===================> 插入失败' + e)
            
        cur.close()  # 关闭查询
        conn.close()  # 关闭数据库连接
    def select_news(self):
        
        # 打开数据连接
        conn = pymysql.connect(host='127.0.0.1', user='root', 
                password='root', database='lyq_db', charset='utf8')
        # 使用cursor()方法创建一个游标对象cur
        cur = conn.cursor()
        # 查询语句
        select_sql = "select * from news"

        try:
            cur.execute(select_sql)
            result = cur.fetchall()
            print(result)
        except Exception as e:
            raise e

        cur.close()
        conn.close()

if __name__ == '__main__':
    database = Database()
    database.insert_news()
    database.select_news()
    

