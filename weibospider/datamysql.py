#-*- coding:utf-8 -*-
import sys
import logging
from scrapy.utils.project import get_project_settings
import MySQLdb

reload(sys)
sys.setdefaultencoding('utf-8')

class MysqlStore:
    '''Mysql数据库连接与命令操作'''
    settings = get_project_settings()

    def get_connection(self):
        '''连接数据库'''
        try:
            conn = MySQLdb.connect(host=MysqlStore.settings['MYSQL_HOST'],user=MysqlStore.settings['MYSQL_USER'],passwd=MysqlStore.settings['MYSQL_PASSWD'],db=MysqlStore.settings['MYSQL_DBNAME'],port=3306)
            conn.set_character_set('utf8')
            print 'mysql_connectinon success!!'
            return conn
        except MySQLdb.Error,e:
            print "Mysql Error %d: %s" % (e.args[0],e.args[1])
    
    def close_connection(self,cursor,conn):
        '''关闭数据库'''
        cursor.close()
        conn.close()
        print "mysql_connection close!!"

    def insert_operation(self,conn,sql):
        '''插入数据操作'''
        cur = conn.cursor()
        cur.execute('set names utf8;')
        cur.execute('set character set utf8;')
        cur.execute('set character_set_connection=utf8;')
        cur.execute(sql)
        print 'insertion success!!'

    def select_operation(self,conn,sql):
        '''从数据库中选择出数据'''
        cur = conn.cursor()
        cur.execute('set names utf8;')
        cur.execute('set character set utf8;')
        cur.execute('set character_set_connection=utf8;')
        cur.execute(sql)
        return cur


if __name__ == '__main__':
    mysql = MysqlStore();
    mysql.get_connection();
