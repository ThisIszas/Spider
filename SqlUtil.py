# coding:utf-8
import MySQLdb

dbHost = 'localhost'
userName = 'root'
pwd = '123456.qaz'
databaseStr = 'testdb'
charsetStr = 'gbk'


def get_conn():
    return MySQLdb.connect(host=dbHost, user=userName, passwd=pwd, db=databaseStr,
                           charset=charsetStr)


def query_data(sql):
    try:
        conn = get_conn()
        cursor = conn.cursor()
        cursor.execute(sql)
#        print cursor.fetchall()
#        for row in cursor.fetchall():
#            print unicode(row)
        return cursor.fetchall()
    except Exception, e:
        print e
        return - 1
    finally:
        cursor.close()
        conn.close()


def createOrInitTable(sql):
    try:
        conn = get_conn()
        cursor = conn.cursor()
        n = cursor.execute(sql)
        print 'Execute SQL return ', n
    except Exception, e:
        print e
    finally:
        cursor.close()
        conn.close()

if __name__ == '__main__':
    data = query_data(u'select * from 学生基本信息')
    for e in data:
        print e
