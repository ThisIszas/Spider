# coding:utf-8
# http://www.runoob.com/python/python-mysql.html
import MySQLdb


class MySQLTest:
    def __init__(self):
        self.db = MySQLdb.Connection('localhost', 'root', '123456.qaz', 'TESTDB')
        self.cursor = self.db.cursor()
        self.fname = "hehe"
        self.lname = "hehe"
        self.age = 0
        self.sex = "M"
        self.income = 0
        self.table_name = "test"
        self.fields_name = "test"

    def create_table(self, table_name):
        self.drop_table(table_name)

        sql = 'CREATE TABLE %s (\
         FIRST_NAME  CHAR(20) NOT NULL,\
         LAST_NAME  CHAR(20),\
         AGE INT,  \
         SEX CHAR(1),\
         INCOME FLOAT )' % table_name

        self.execute_statement(sql)

    def drop_table(self, table_name):
        sql = " DROP TABLE IF EXISTS %s" % table_name
        self.execute_statement(sql)

    def insert_info(self, fname, lname, age, sex, income, table_name):
        sql_1 = "INSERT INTO %s(FIRST_NAME,\
                 LAST_NAME, AGE, SEX, INCOME)\
                 VALUES ('%s', '%s', '%d', '%c', '%d' )" % (table_name, fname, lname, age, sex, income)
        self.execute_statement(sql_1)

    def delete_info(self, table_name, fields_name, symbol, temp_value):
        sql = "DELETE FROM %s WHERE %s %c %s" % (table_name, fields_name, symbol, temp_value)
        self.execute_statement(sql)

    def alter_info(self, table_name, fields_name_1, temp_value, fields_name_2, temp_value_2):
        sql = "UPDATE %s SET %s = %s WHERE %s = %s" % (table_name, fields_name_1, temp_value,
                                                       fields_name_2, temp_value_2)
        self.cursor.execute(sql)

    def execute_statement(self, sql):
        try:
            self.cursor.execute(sql)
            self.db.commit()
        except Exception as e:
            print e
            self.db.rollback()

    def show_data(self, table_name):
        sql = "select * from %s where income > '%d'" % (table_name, 1000)
        try:
            self.execute_statement(sql)
            results = self.cursor.fetchall()
            for each in results:
                fname = each[0]
                lname = each[1]
                age = each[2]
                sex = each[3]
                income = each[4]
                print "fname:%s lname:%s age:%d sex:%s income:%d" % (fname, lname, age, sex, income)
        except Exception as e:
            print e
            print "Error : unable to fetch data"

    def close_db(self):
        self.db.close()


tt = MySQLTest()
tt.drop_table("justAqTest")
tt.create_table("justAqTest")
tt.insert_info('zas', 'Zheng', 18, 'M', 100000, 'justAqTest')
tt.show_data("justAqTest")
tt.close_db()
