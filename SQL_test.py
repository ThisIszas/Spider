# coding:utf-8
# http://www.runoob.com/python/python-mysql.html
import MySQLdb


class MySQLTest:
    def __init__(self):
        self.db = MySQLdb.Connection('localhost', 'root', '123456.qaz', 'TESTDB', charset='utf8')
        # self.db.set_character_set('utf-8')
        self.cursor = self.db.cursor()
        # self.cursor.execute('SET NAMES utf8;')
        # self.cursor.execute('SET CHARACTER SET utf8;')
        # self.cursor.execute('SET character_set_connection=utf8;')
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
        return sql
        # self.execute_statement(sql)

    def drop_table(self, table_name):
        sql = " DROP TABLE IF EXISTS %s" % table_name
        return sql
        # self.execute_statement(sql)

    def insert_info(self, stunum, stuname, stuadress, stusex, stuage, stusituation, table_name):
        sql_1 = "INSERT INTO %s VALUES ('%s', '%s', '%s', '%s', '%s', '%s')" % (table_name, stunum, stuname,
                                                                                stuadress, stusex, stuage, stusituation)
        # self.execute_statement(sql_1)
        return sql_1

    def insert_info_2(self, table_name, splited_stu_info):
        stunum = splited_stu_info[0]
        stuname = splited_stu_info[1]
        sql_grade = splited_stu_info[2]
        composition_principle_grade = splited_stu_info[3]
        operate_system_grade = splited_stu_info[4]
        data_structure_grade = splited_stu_info[5]
        algorithm_grade = splited_stu_info[6]
        computer_networks_grade = splited_stu_info[7]
        higher_mathematics_grade = splited_stu_info[8]
        total_grade = splited_stu_info[9]
        average_grade = splited_stu_info[10]
        teacher = splited_stu_info[11]
        sql_1 = "INSERT INTO %s VALUES ('%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s'," \
                " '%s')" % (table_name, stunum, stuname, sql_grade, composition_principle_grade,
                            operate_system_grade, data_structure_grade, algorithm_grade, computer_networks_grade,
                            higher_mathematics_grade, total_grade, average_grade, teacher)
        # self.execute_statement(sql_1)
        return sql_1

    def delete_info(self, table_name, fields_name, symbol, temp_value):
        sql = "DELETE FROM %s WHERE %s %s \"%s\"" % (table_name, fields_name, symbol, temp_value)
        # self.execute_statement(sql)
        return sql

    def alter_info(self, table_name, fields_name_1, temp_value, fields_name_2, temp_value_2, flag):
        if flag == 666:
            sql = "UPDATE %s SET %s = %s WHERE %s = \"%s\"" % (table_name, fields_name_1, temp_value,
                                                               fields_name_2, temp_value_2)
        else:
            sql = "UPDATE %s SET %s = \"%s\" WHERE %s = \"%s\"" % (table_name, fields_name_1, temp_value,
                                                                   fields_name_2, temp_value_2)
        return sql

    def execute_statement(self, sql):
        try:
            cursor = self.db.cursor()
            # temp = self.cursor.execute(sql)
            # self.db.commit()
            cursor.execute(sql)
            self.db.commit()
            return cursor.fetchall()
        except Exception as e:
            print e
            self.db.rollback()

    def show_data(self, table_name, colname, values, symbol='='):
        sql = "select * from %s where %s %s '%s'" % (table_name, colname, symbol, values)
        return sql
        """
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
        """
    def close_db(self):
        self.db.close()

    def select_info(self, tablename, item, symbol, values, flag):
        if flag == 333:
            sql = 'select * from %s WHERE %s %s \"%s\"' % (tablename, item, symbol, values)
        else:
            sql = 'select * from %s WHERE %s %s %s' % (tablename, item, symbol, values)
        return sql

    def register(self, username, password):
        sql = "insert into unandpassword VALUES (\"%s\",\"%s\")" %(username, password)
        ww = self.execute_statement(sql)
        # print type(ww)
        # if ww is None:
        #     print 'helloworld'
        return ww
tt = MySQLTest()
# tt.drop_table("justAqTest")
# tt.create_table("justAqTest")
# tt.insert_info('zas', 'Zheng', 18, 'M', 100000, 'justAqTest')
# tt.show_data("justAqTest")
# tt.close_db()
# tt.delete_info(u"学生基本信息", u'学号', '=', '25180')
# sql = tt.show_data('unandpassword', 'username', '2014021073')
# print sql
# ss = tt.execute_statement(sql)
# for e in ss:
#     print e[1]
# ww = tt.register('2014021065', '021065')
# ee = tt.execute_statement(ww)
# if ee:
#     print 0
# else:
#     print 2
