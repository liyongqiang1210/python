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

    # 插入视频链接的方法
    def insertVideoUrl(self, video_url, video_title, video_classHour, video_number, video_price):
        # 打开数据连接
        conn = pymysql.connect(host='39.106.154.2', user='root', password='root', database='maven', charset='utf8')
        # 使用cursor()方法创建一个游标对象cur
        cur = conn.cursor()
        insert_sql = "insert into 51cto_video_url_list(video_url,video_title,video_class_hour,video_number,video_price,video_is_craw)values('%s','%s','%s','%s','%s',0)" % (video_url, video_title, video_classHour, video_number, video_price)  # 插入语句
        try:
            cur.execute(insert_sql)
            conn.commit()
            print('%s ===================> 插入成功' % (video_title))
        except:
            conn.rollback()
            print('%s ===================> 插入失败' % (video_title))
            
        cur.close()  # 关闭查询
        conn.close()  # 关闭数据库连接
    
    # 获取一条未爬取的视频url链接 
    def selectVideoUrlIsCraw(self):
        conn = pymysql.connect(host='39.106.154.2', user='root', password='root', database='maven', charset='utf8')
        cur = conn.cursor()
        select_sql = 'select video_id,video_url from 51cto_video_url_list where video_is_craw = 0 limit 1'
        
        try :
            cur.execute(select_sql)
            results = cur.fetchone()  # 查询的结果集
            video_id = results[0]  # 视频id
            video_url = results[1]  # 视频url地址
            print('成功取出一条数据==============>' + video_url)
            update_sql = "update 51cto_video_url_list set video_is_craw = 1 where video_id ='%d'" % (video_id)
            cur.execute(update_sql)
            conn.commit()
            return video_id, video_url
        except :
            conn.rollback()
            print('selectVideoUrlIsCraw Exception')
                    
    # 插入课程视频url的方法
    def insertCourseUrl(self, course_url, course_title, video_url_id) :
            # 打开数据连接
            conn = pymysql.connect(host='39.106.154.2', user='root', password='root', database='maven', charset='utf8')
            # 使用cursor()方法创建一个游标对象cur
            cur = conn.cursor()
            # 插入操作
            insert_sql = "insert into 51cto_course_url(course_url,course_title,video_url_id)values('%s','%s',%d)" % (course_url , course_title, video_url_id)
            try:
                cur.execute(insert_sql)
                conn.commit()
                print(course_url + '===============> 数据插入成功')
            except:
                conn.rollback()
                print('===============> insertCourseUrl方法异常')
                
            # 关闭查询
            cur.close()
            # 关闭数据库连接
            conn.close()
    
    # 获取一条未爬取的url
    def selectCourseUrlNoCraw(self) :
        conn = pymysql.connect(host='39.106.154.2', user='root', password='root', database='maven', charset='utf8')
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
