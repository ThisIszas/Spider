# coding:utf-8
import MySQLdb


class MySQLTest:
    def __init__(self):
        self.db = MySQLdb.Connection('localhost', 'root', '123456.qaz', 'TESTDB', charset='utf8')
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
        return sql

    def drop_table(self, table_name):
        sql = " DROP TABLE IF EXISTS %s" % table_name
        return sql

    def insert_info(self, stunum, stuname, stuadress, stusex, stuage, stusituation, table_name):
        sql_1 = u"INSERT INTO %s VALUES ('%s', '%s', '%s', '%s', '%s', '%s')" % (table_name, stunum, stuname,
                                                                                stuadress, stusex, stuage, stusituation)
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
        teacher = splited_stu_info[9]
        sql_1 = u"INSERT INTO %s (学号,姓名,数据库,组成原理,操作系统,数据结构,算法,计算机网络,高数,任课教师) " \
                u"VALUES ('%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s','%s')" \
                 % (table_name, stunum, stuname, sql_grade, composition_principle_grade,
                            operate_system_grade, data_structure_grade, algorithm_grade, computer_networks_grade,
                            higher_mathematics_grade, teacher)
        print sql_1
        self.execute_statement(sql_1)

    def insert_info3(self, table_name, stunum, stuname, prize_1, prize_2, prize_3, stage_ranking, the_data):
        sql = u"INSERT INTO %s VALUES ('%s', '%s', '%s', '%s', '%s', '%s', '%s')" % \
              (table_name, stunum, stuname, prize_1, prize_2, prize_3, stage_ranking, the_data)
        return sql

    def delete_info(self, table_name, fields_name, symbol, temp_value):
        sql = "DELETE FROM %s WHERE %s %s \"%s\"" % (table_name, fields_name, symbol, temp_value)
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
            cursor.execute(sql)
            self.db.commit()
            return cursor.fetchall()
        except Exception as e:
            print e
            self.db.rollback()

    def show_data(self, table_name, colname, values, symbol='='):
        sql = "select * from %s where %s %s '%s'" % (table_name, colname, symbol, values)
        return sql

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
        print type(ww)
        return ww

    def cal_all_grade(self):
        sql = "update 学生成绩信息 set 总成绩=(数据库+组成原理+操作系统+数据结构+算法+计算机网络+高数);"
        self.execute_statement(sql)
        sql_2 = "update 学生成绩信息 set 平均成绩=总成绩/7;"
        self.execute_statement(sql_2)

    def adv_query(self, tn1, in1, s1, v1, tn2='0', in2='0', s2='0', v2='0', flag=1):
        if flag > 1:
            sql = "select * from %s WHERE %s in (SELECT %s FROM %s WHERE %s %s %s)" % (tn1, in1, in1, tn2,
                                                                                      in2, s2, v2)
        else:
            sql = "select * from %s WHERE %s %s %s" %(tn1, in1, s1, v1)
        return sql