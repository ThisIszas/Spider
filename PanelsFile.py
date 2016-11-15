# coding:gbk
import wx
import wx.grid
import GenericTable
from SQL_test import MySQLTest


class BaseInfoOfStudentPanel(wx.Panel):
    def __init__(self, *args, **kwargs):
        self.sqlstament = MySQLTest()
        self.table_name = u'学生基本信息'
        self.select_item_list = [u'*', u'学号', u'姓名', u'家庭住址', u'性别', u'年龄', u'基本情况']
        super(BaseInfoOfStudentPanel, self).__init__(*args, **kwargs)
        title_font = wx.Font(18, wx.SWISS, wx.NORMAL, wx.BOLD)  # 设置字体
        self.gbsizer = wx.GridBagSizer(hgap=10, vgap=10)
        self.second_panel = wx.Panel(self, size=(238, 270), pos=(600, 100),
                                     style=wx.TAB_TRAVERSAL | wx.CLIP_CHILDREN | wx.FULL_REPAINT_ON_RESIZE)

        self.title_label = wx.StaticText(self, label=u"学生基本信息管理", pos=(308, 10))
        wx.StaticText(self, label=u"查询项:", pos=(10, 10))
        wx.StaticText(self, label=u"值:", pos=(96, 10))
        self.title_label.SetFont(title_font)
        self.title_label.SetForegroundColour("#21c4c3")  # 设置字体颜色

        self.SelectButton = wx.Button(self, label=u'查询', pos=(144, 30), size=(33, 25))
        self.AddButton = wx.Button(self, label=u'添加一行', pos=(680, 8), size=(60, 25))
        self.DropButton = wx.Button(self, label=u'删除一行', pos=(680, 35), size=(60, 25))
        self.UpdateButton = wx.Button(self, label=u'修改数据', pos=(740, 8), size=(60, 25))
        self.RefreshButton = wx.Button(self, label=u'刷新', pos=(740, 35), size=(60, 25))
        self.SelectButton.Bind(wx.EVT_BUTTON, self.query_info)
        self.DropButton.Bind(wx.EVT_BUTTON, self.delete_info)
        self.AddButton.Bind(wx.EVT_BUTTON, self.add_info)
        self.RefreshButton.Bind(wx.EVT_BUTTON, self.refresh)
        self.UpdateButton.Bind(wx.EVT_BUTTON, self.updata_info)

        self.select_items = wx.ComboBox(self, pos=(10, 30), size=(80, -1), choices=self.select_item_list,
                                        style=wx.CB_DROPDOWN)
        self.valueTextCtrl = wx.TextCtrl(self, value="", pos=(92, 30), size=(50, 25))
        self.test_grid('select * from 学生基本信息')

    def test_grid(self, sqlsta):
        import SqlUtil
        data = SqlUtil.query_data(sqlsta)
        col_label = ("学号", "姓名", "家庭地址", "性别", "年龄", "基本情况")
        self.testgrid = wx.grid.Grid(self, size=(880, 300), pos=(10, 60))
        row_label = []
        for i in range(len(data)):
            row_label.append(i+1)
        self.testgrid.baseModel = GenericTable.GenericTable(data, row_label, col_label)
        self.testgrid.SetTable(self.testgrid.baseModel)

    def refresh(self, event):
        self.testgrid.Destroy()
        self.test_grid('select * from 学生基本信息')

    def delete_info(self, event):
        stunum = "00000000"
        entry_dlg = wx.TextEntryDialog(self, u'输入一个\"学号\"来删除', u'输入一个学号')
        if entry_dlg.ShowModal() == wx.ID_OK:
            stunum = entry_dlg.GetValue()
        entry_dlg.Destroy()
        if stunum:
            splited_stunum = stunum.split(' ')  # 因为用户输入的学号可能带空格,所以先把字符按空格拆分,再进行连接.(分割后为一个数组)
        # 同理添加数据时也按空格进行分割.
            joined_stunum = ''.join(splited_stunum)  # 对已分割后的字符串拼接
            stunum = joined_stunum
        sqlsta = self.sqlstament.delete_info(self.table_name, u'学号', '=', stunum)
        print sqlsta
        self.sqlstament.execute_statement(sqlsta)

    def add_info(self, event):
        stu_infos = ""
        entry_dlg = wx.TextEntryDialog(self, u'输入一组学生信息,空缺的信息用0代替', u'输入一组信息')
        if entry_dlg.ShowModal() == wx.ID_OK:
            stu_infos = entry_dlg.GetValue()
        entry_dlg.Destroy()
        if stu_infos:
            splited_stu_info = stu_infos.split(' ')
            stunum = splited_stu_info[0]
            stuname = splited_stu_info[1]
            stu_adress = splited_stu_info[2]
            stusex = splited_stu_info[3]
            stuage = splited_stu_info[4]
            stusituation = splited_stu_info[5]
            sqlsta = self.sqlstament.insert_info(stunum, stuname, stu_adress, stusex, stuage, stusituation,
                                                 self.table_name)
            print sqlsta
            self.sqlstament.execute_statement(sqlsta)
        else:
            return stu_infos

    def query_info(self, event):
        self.testgrid.Destroy()
        word = self.select_items.GetSelection()
        select_item_value = self.select_items.GetItems()[word]
        value = self.valueTextCtrl.GetRange(0, 50)
        if select_item_value == u"年龄":
            sqlsta = self.sqlstament.select_info(self.table_name, select_item_value, '=', value, 666)
        else:
            sqlsta = self.sqlstament.select_info(self.table_name, select_item_value, '=', value, 333)
        print sqlsta
        self.test_grid(sqlsta)

    def updata_info(self, event):
        self.select_item_list2 = [u'姓名', u'家庭住址', u'性别', u'年龄', u'基本情况']
        self.stunum_temp_label = wx.StaticText(self.second_panel, label=u"修改对象学号:", pos=(0, 5))
        self.stunumvalues_temp = wx.TextCtrl(self.second_panel, size=(80, 25), pos=(82, 0))
        self.column_name_temp = wx.StaticText(self.second_panel, label=u"要修改的列名:", pos=(0, 30))
        self.select_items_temp = wx.ComboBox(self.second_panel, size=(80, 25), pos=(0, 50),
                                        choices=self.select_item_list2, style=wx.CB_DROPDOWN)
        self.change_value = wx.StaticText(self.second_panel, label=u'  修改后的值:', pos=(82, 30))
        self.values_temp = wx.TextCtrl(self.second_panel, size=(80, 25), pos=(85, 50))
        self.ok_button = wx.Button(self.second_panel, label=u"确定修改", pos=(0, 80), size=(80, 25))
        self.ok_button.Bind(wx.EVT_BUTTON, self.unshow_second_panel)
        self.cancel_button = wx.Button(self.second_panel, label=u"返回", pos=(85, 80), size=(80, 25))
        self.cancel_button.Bind(wx.EVT_BUTTON, self.unshow_second_panel_ele)
        self.second_panel.Show(True)

    def unshow_second_panel(self, event):
        stunum = self.stunumvalues_temp.GetRange(0, 10)
        word = self.select_items_temp.GetSelection()
        colname = self.select_items_temp.GetItems()[word]
        colvalue = self.values_temp.GetRange(0, 30)
        if colname == u'年龄':
            sql = self.sqlstament.alter_info(self.table_name, colname, colvalue, u'学号', stunum, 666)
        else:
            sql = self.sqlstament.alter_info(self.table_name, colname, colvalue, u'学号', stunum, 333)
        self.stunumvalues_temp.Show(False)
        self.select_items_temp.Show(False)
        self.values_temp.Show(False)
        self.stunum_temp_label.Show(False)
        self.column_name_temp.Show(False)
        self.change_value.Show(False)
        self.ok_button.Show(False)
        self.cancel_button.Show(False)
        self.sqlstament.execute_statement(sql)
        print sql

    def unshow_second_panel_ele(self, event):
        self.stunumvalues_temp.Show(False)
        self.select_items_temp.Show(False)
        self.values_temp.Show(False)
        self.stunum_temp_label.Show(False)
        self.column_name_temp.Show(False)
        self.change_value.Show(False)
        self.ok_button.Show(False)
        self.cancel_button.Show(False)


class GradesOfStudent(wx.Panel):
    def __init__(self, *args, **kwargs):
        self.table_name = u'学生成绩信息'
        super(GradesOfStudent, self).__init__(*args, **kwargs)
        title_font = wx.Font(18, wx.SWISS, wx.NORMAL, wx.BOLD)  # 设置字体   600,100
        self.second_panel = wx.Panel(self, size=(238, 270), pos=(300, 100),
                                     style=wx.TAB_TRAVERSAL | wx.CLIP_CHILDREN | wx.FULL_REPAINT_ON_RESIZE)
        self.select_item_list = [u'*', u'学号', u'姓名', u'数据库', u'组成原理', u'操作系统', u'数据结构',
                                 u'算法', u'计算机网络', u'高数', u'总成绩', u'平均成绩', u'任课教师']
        self.sqlstament = MySQLTest()
        self.title_label = wx.StaticText(self, label=u"学生成绩管理", pos=(308, 10))
        self.title_label.SetFont(title_font)
        self.title_label.SetForegroundColour("#21c4c3")
        self.warning_label = wx.StaticText(self, label=u'注:此表只能管理学号已存在学生的信息.', pos=(283, 35))
        self.warning_label.SetForegroundColour('red')

        wx.StaticText(self, label=u"查询项:", pos=(10, 10))
        wx.StaticText(self, label=u"值:", pos=(96, 10))

        self.SelectButton = wx.Button(self, label=u'查询', pos=(144, 30), size=(33, 25))
        self.AddButton = wx.Button(self, label=u'添加一行', pos=(680, 8), size=(60, 25))
        self.DropButton = wx.Button(self, label=u'删除一行', pos=(680, 35), size=(60, 25))
        self.UpdateButton = wx.Button(self, label=u'修改数据', pos=(740, 8), size=(60, 25))
        self.RefreshButton = wx.Button(self, label=u'刷新', pos=(740, 35), size=(60, 25))
        self.cal_total_and_ave = wx.Button(self, label=u'计算总成绩和平均成绩', pos=(540, 35), size=(-1, 25))
        self.cal_total_and_ave.Bind(wx.EVT_BUTTON, self.calculates)
        self.SelectButton.Bind(wx.EVT_BUTTON, self.query_info)
        self.DropButton.Bind(wx.EVT_BUTTON, self.delete_info)
        self.AddButton.Bind(wx.EVT_BUTTON, self.add_info)
        self.RefreshButton.Bind(wx.EVT_BUTTON, self.refresh)
        self.UpdateButton.Bind(wx.EVT_BUTTON, self.updata_info)
        self.select_items = wx.ComboBox(self, pos=(10, 30), size=(80, -1), choices=self.select_item_list,
                                        style=wx.CB_DROPDOWN)
        self.valueTextCtrl = wx.TextCtrl(self, value="", pos=(92, 30), size=(50, 25))
        self.test_grid('select * from 学生成绩信息')

    def calculates(self, event):
        self.sqlstament.cal_all_grade()
        try:
            self.testgrid.Destroy()
        except:
            pass
        self.test_grid('select * from 学生成绩信息')

    def test_grid(self, sqlsta):
        import SqlUtil
        data = SqlUtil.query_data(sqlsta)
        col_label = (u'学号', u'姓名', u'数据库', u'组成原理', u'操作系统', u'数据结构',
                     u'算法', u'计算机网络', u'高数', u'总成绩', u'平均成绩', u'任课教师')
        self.testgrid = wx.grid.Grid(self, size=(800, 300), pos=(10, 60))
        row_label = []
        if len(data):
            for i in range(len(data)):
                row_label.append(i+1)
            self.testgrid.baseModel = GenericTable.GenericTable(data, row_label, col_label)
            self.testgrid.SetTable(self.testgrid.baseModel)
        else:
            wx.MessageBox('成绩表表中无信息,请插入信息', 'Warning!', wx.OK | wx.ICON_INFORMATION)

    def refresh(self, event):
        try:
            self.testgrid.Destroy()
        except:
            pass
        self.test_grid('select * from 学生成绩信息')

    def delete_info(self, event):
        stunum = "00000000"
        entry_dlg = wx.TextEntryDialog(self, u'输入一个\"学号\"来删除', u'输入一个学号')
        if entry_dlg.ShowModal() == wx.ID_OK:
            stunum = entry_dlg.GetValue()
        entry_dlg.Destroy()
        if stunum:
            splited_stunum = stunum.split(' ')  # 因为用户输入的学号可能带空格,所以先把字符按空格拆分,再进行连接.(分割后为一个数组)
        # 同理添加数据时也按空格进行分割.
            joined_stunum = ''.join(splited_stunum)  # 对已分割后的字符串拼接
            stunum = joined_stunum
        sqlsta = self.sqlstament.delete_info(self.table_name, u'学号', '=', stunum)
        print sqlsta
        self.sqlstament.execute_statement(sqlsta)

    def add_info(self, event):
        stu_infos = ""
        entry_dlg = wx.TextEntryDialog(self, u'输入一组学生信息,空缺的信息用0代替', u'输入一组信息')
        if entry_dlg.ShowModal() == wx.ID_OK:
            stu_infos = entry_dlg.GetValue()
        entry_dlg.Destroy()
        if stu_infos:
            splited_stu_info = stu_infos.split(' ')
            sqlsta = self.sqlstament.insert_info_2(self.table_name, splited_stu_info)
            #print sqlsta
            #self.sqlstament.execute_statement(sqlsta)

    def query_info(self, event):
        self.testgrid.Destroy()
        word = self.select_items.GetSelection()
        select_item_value = self.select_items.GetItems()[word]
        value = self.valueTextCtrl.GetRange(0, 50)
        if select_item_value == u"年龄":
            sqlsta = self.sqlstament.select_info(self.table_name, select_item_value, '=', value, 666)
        else:
            sqlsta = self.sqlstament.select_info(self.table_name, select_item_value, '=', value, 333)
        print sqlsta
        self.test_grid(sqlsta)

    def updata_info(self, event):
        try:
            self.testgrid.Destroy()
        except Exception as e:
            print e
            pass
        self.select_item_list2 = [u'数据库', u'组成原理', u'操作系统', u'数据结构',
                                  u'算法', u'计算机网络', u'高数', u'总成绩', u'平均成绩', u'任课教师']
        self.stunum_temp_label = wx.StaticText(self.second_panel, label=u"修改对象学号:", pos=(0, 5))
        self.stunumvalues_temp = wx.TextCtrl(self.second_panel, size=(80, 25), pos=(82, 0))
        self.column_name_temp = wx.StaticText(self.second_panel, label=u"要修改的列名:", pos=(0, 30))
        self.select_items_temp = wx.ComboBox(self.second_panel, size=(80, 25), pos=(0, 50),
                                        choices=self.select_item_list2, style=wx.CB_DROPDOWN)
        self.change_value = wx.StaticText(self.second_panel, label=u'  修改后的值:', pos=(82, 30))
        self.values_temp = wx.TextCtrl(self.second_panel, size=(80, 25), pos=(85, 50))
        self.ok_button = wx.Button(self.second_panel, label=u"确定修改", pos=(0, 80), size=(80, 25))
        self.cancel_button = wx.Button(self.second_panel, label=u"返回", pos=(85, 80), size=(80, 25))
        self.ok_button.Bind(wx.EVT_BUTTON, self.unshow_second_panel)
        self.cancel_button.Bind(wx.EVT_BUTTON, self.unshow_second_panel_ele)
        self.second_panel.Show(True)

    def unshow_second_panel(self, event):
        stunum = self.stunumvalues_temp.GetRange(0, 10)
        word = self.select_items_temp.GetSelection()
        colname = self.select_items_temp.GetItems()[word]
        colvalue = self.values_temp.GetRange(0, 30)
        if colname == u'年龄':
            sql = self.sqlstament.alter_info(self.table_name, colname, colvalue, u'学号', stunum, 666)
        else:
            sql = self.sqlstament.alter_info(self.table_name, colname, colvalue, u'学号', stunum, 333)
        self.stunumvalues_temp.Show(False)
        self.select_items_temp.Show(False)
        self.values_temp.Show(False)
        self.stunum_temp_label.Show(False)
        self.column_name_temp.Show(False)
        self.change_value.Show(False)
        self.ok_button.Show(False)
        self.cancel_button.Show(False)
        self.sqlstament.execute_statement(sql)
        print sql
        self.test_grid('select * from 学生成绩信息')

    def unshow_second_panel_ele(self, event):
        self.stunumvalues_temp.Show(False)
        self.select_items_temp.Show(False)
        self.values_temp.Show(False)
        self.stunum_temp_label.Show(False)
        self.column_name_temp.Show(False)
        self.change_value.Show(False)
        self.ok_button.Show(False)
        self.cancel_button.Show(False)
        self.test_grid('select * from 学生成绩信息')


class ATestPanel3(wx.Panel):
    def __init__(self, *args, **kwargs):
        self.sqlstament = MySQLTest()
        self.table_name = u'学生基本信息'
        self.select_item_list = [u'*', u'学号', u'姓名', u'家庭住址', u'性别', u'年龄', u'基本情况']
        super(ATestPanel3, self).__init__(*args, **kwargs)
        title_font = wx.Font(18, wx.SWISS, wx.NORMAL, wx.BOLD)  # 设置字体
        self.gbsizer = wx.GridBagSizer(hgap=10, vgap=10)
        self.second_panel = wx.Panel(self, size=(238, 270), pos=(600, 100),
                                     style=wx.TAB_TRAVERSAL | wx.CLIP_CHILDREN | wx.FULL_REPAINT_ON_RESIZE)

        self.title_label = wx.StaticText(self, label=u"学生基本信息管理", pos=(308, 10))
        wx.StaticText(self, label=u"查询项:", pos=(10, 10))
        wx.StaticText(self, label=u"值:", pos=(96, 10))
        self.title_label.SetFont(title_font)
        self.title_label.SetForegroundColour("#21c4c3")  # 设置字体颜色

        self.SelectButton = wx.Button(self, label=u'查询', pos=(144, 30), size=(33, 25))
        self.AddButton = wx.Button(self, label=u'添加一行', pos=(680, 8), size=(60, 25))
        self.DropButton = wx.Button(self, label=u'删除一行', pos=(680, 35), size=(60, 25))
        self.UpdateButton = wx.Button(self, label=u'修改数据', pos=(740, 8), size=(60, 25))
        self.RefreshButton = wx.Button(self, label=u'刷新', pos=(740, 35), size=(60, 25))
        self.SelectButton.Bind(wx.EVT_BUTTON, self.query_info)
        self.DropButton.Bind(wx.EVT_BUTTON, self.delete_info)
        self.AddButton.Bind(wx.EVT_BUTTON, self.add_info)
        self.RefreshButton.Bind(wx.EVT_BUTTON, self.refresh)
        self.UpdateButton.Bind(wx.EVT_BUTTON, self.updata_info)

        self.select_items = wx.ComboBox(self, pos=(10, 30), size=(80, -1), choices=self.select_item_list,
                                        style=wx.CB_DROPDOWN)
        self.valueTextCtrl = wx.TextCtrl(self, value="", pos=(92, 30), size=(50, 25))
        self.test_grid('select * from 学生基本信息')

    def test_grid(self, sqlsta):
        import SqlUtil
        data = SqlUtil.query_data(sqlsta)
        col_label = ("学号", "姓名", "家庭地址", "性别", "年龄", "基本情况")
        self.testgrid = wx.grid.Grid(self, size=(880, 300), pos=(10, 60))
        row_label = []
        for i in range(len(data)):
            row_label.append(i+1)
        self.testgrid.baseModel = GenericTable.GenericTable(data, row_label, col_label)
        self.testgrid.SetTable(self.testgrid.baseModel)

    def refresh(self, event):
        self.testgrid.Destroy()
        self.test_grid('select * from 学生基本信息')

    def delete_info(self, event):
        stunum = "00000000"
        entry_dlg = wx.TextEntryDialog(self, u'输入一个\"学号\"来删除', u'输入一个学号')
        if entry_dlg.ShowModal() == wx.ID_OK:
            stunum = entry_dlg.GetValue()
        entry_dlg.Destroy()
        if stunum:
            splited_stunum = stunum.split(' ')  # 因为用户输入的学号可能带空格,所以先把字符按空格拆分,再进行连接.(分割后为一个数组)
        # 同理添加数据时也按空格进行分割.
            joined_stunum = ''.join(splited_stunum)  # 对已分割后的字符串拼接
            stunum = joined_stunum
        sqlsta = self.sqlstament.delete_info(self.table_name, u'学号', '=', stunum)
        print sqlsta
        self.sqlstament.execute_statement(sqlsta)

    def add_info(self, event):
        stu_infos = ""
        entry_dlg = wx.TextEntryDialog(self, u'输入一组学生信息,空缺的信息用0代替', u'输入一组信息')
        if entry_dlg.ShowModal() == wx.ID_OK:
            stu_infos = entry_dlg.GetValue()
        entry_dlg.Destroy()
        if stu_infos:
            splited_stu_info = stu_infos.split(' ')
            stunum = splited_stu_info[0]
            stuname = splited_stu_info[1]
            stu_adress = splited_stu_info[2]
            stusex = splited_stu_info[3]
            stuage = splited_stu_info[4]
            stusituation = splited_stu_info[5]
            sqlsta = self.sqlstament.insert_info(stunum, stuname, stu_adress, stusex, stuage, stusituation,
                                                 self.table_name)
            print sqlsta
            self.sqlstament.execute_statement(sqlsta)
        else:
            return stu_infos

    def query_info(self, event):
        self.testgrid.Destroy()
        word = self.select_items.GetSelection()
        select_item_value = self.select_items.GetItems()[word]
        value = self.valueTextCtrl.GetRange(0, 50)
        if select_item_value == u"年龄":
            sqlsta = self.sqlstament.select_info(self.table_name, select_item_value, '=', value, 666)
        else:
            sqlsta = self.sqlstament.select_info(self.table_name, select_item_value, '=', value, 333)
        print sqlsta
        self.test_grid(sqlsta)

    def updata_info(self, event):
        self.select_item_list2 = [u'姓名', u'家庭住址', u'性别', u'年龄', u'基本情况']
        self.stunum_temp_label = wx.StaticText(self.second_panel, label=u"修改对象学号:", pos=(0, 5))
        self.stunumvalues_temp = wx.TextCtrl(self.second_panel, size=(80, 25), pos=(82, 0))
        self.column_name_temp = wx.StaticText(self.second_panel, label=u"要修改的列名:", pos=(0, 30))
        self.select_items_temp = wx.ComboBox(self.second_panel, size=(80, 25), pos=(0, 50),
                                        choices=self.select_item_list2, style=wx.CB_DROPDOWN)
        self.change_value = wx.StaticText(self.second_panel, label=u'  修改后的值:', pos=(82, 30))
        self.values_temp = wx.TextCtrl(self.second_panel, size=(80, 25), pos=(85, 50))
        self.ok_button = wx.Button(self.second_panel, label=u"确定修改", pos=(0, 80), size=(80, 25))
        self.ok_button.Bind(wx.EVT_BUTTON, self.unshow_second_panel)
        self.cancel_button = wx.Button(self.second_panel, label=u"返回", pos=(85, 80), size=(80, 25))
        self.cancel_button.Bind(wx.EVT_BUTTON, self.unshow_second_panel_ele)
        self.second_panel.Show(True)

    def unshow_second_panel(self, event):
        stunum = self.stunumvalues_temp.GetRange(0, 10)
        word = self.select_items_temp.GetSelection()
        colname = self.select_items_temp.GetItems()[word]
        colvalue = self.values_temp.GetRange(0, 30)
        if colname == u'年龄':
            sql = self.sqlstament.alter_info(self.table_name, colname, colvalue, u'学号', stunum, 666)
        else:
            sql = self.sqlstament.alter_info(self.table_name, colname, colvalue, u'学号', stunum, 333)
        self.stunumvalues_temp.Show(False)
        self.select_items_temp.Show(False)
        self.values_temp.Show(False)
        self.stunum_temp_label.Show(False)
        self.column_name_temp.Show(False)
        self.change_value.Show(False)
        self.ok_button.Show(False)
        self.cancel_button.Show(False)
        self.sqlstament.execute_statement(sql)
        print sql

    def unshow_second_panel_ele(self, event):
        self.stunumvalues_temp.Show(False)
        self.select_items_temp.Show(False)
        self.values_temp.Show(False)
        self.stunum_temp_label.Show(False)
        self.column_name_temp.Show(False)
        self.change_value.Show(False)
        self.ok_button.Show(False)
        self.cancel_button.Show(False)