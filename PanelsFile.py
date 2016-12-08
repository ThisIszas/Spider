# coding:gbk
import wx
import wx.grid
import GenericTable
from SQL_test import MySQLTest


class BaseInfoOfStudentPanel(wx.Panel):
    def __init__(self, *args, **kwargs):
        self.sqlstament = MySQLTest()  # ��ʼ������,ͬ��¼ҳ�������,����д
        self.table_name = u'ѧ��������Ϣ'
        self.select_item_list = [u'*', u'ѧ��', u'����', u'��ͥסַ', u'�Ա�', u'����', u'�������']
        super(BaseInfoOfStudentPanel, self).__init__(*args, **kwargs)
        title_font = wx.Font(18, wx.SWISS, wx.NORMAL, wx.BOLD)  # ��������
        self.second_panel = wx.Panel(self, size=(238, 270), pos=(600, 100),
                                     style=wx.TAB_TRAVERSAL | wx.CLIP_CHILDREN | wx.FULL_REPAINT_ON_RESIZE)
        self.adv_select_panel = wx.Panel(self, size=(338, 270), pos=(230, 60),
                                     style=wx.TAB_TRAVERSAL | wx.CLIP_CHILDREN | wx.FULL_REPAINT_ON_RESIZE)

        self.title_label = wx.StaticText(self, label=u"ѧ��������Ϣ����", pos=(308, 10))
        wx.StaticText(self, label=u"��ѯ��:", pos=(10, 10))
        wx.StaticText(self, label=u"ֵ:", pos=(96, 10))
        self.title_label.SetFont(title_font)
        self.title_label.SetForegroundColour("#21c4c3")  # ����������ɫ
        self.more_use_time = 1
        self.SelectButton = wx.Button(self, label=u'��ѯ', pos=(144, 30), size=(33, 25))
        self.AdvanceQuireButton = wx.Button(self, label=u'�߼���ѯ', pos=(177, 30), size=(58, 25))
        self.AddButton = wx.Button(self, label=u'���һ��', pos=(680, 8), size=(60, 25))
        self.DropButton = wx.Button(self, label=u'ɾ��һ��', pos=(680, 35), size=(60, 25))
        self.UpdateButton = wx.Button(self, label=u'�޸�����', pos=(740, 8), size=(60, 25))
        self.RefreshButton = wx.Button(self, label=u'ˢ��', pos=(740, 35), size=(60, 25))
        self.SelectButton.Bind(wx.EVT_BUTTON, self.query_info)
        self.AdvanceQuireButton.Bind(wx.EVT_BUTTON, self.advance_quire_step1)
        self.DropButton.Bind(wx.EVT_BUTTON, self.delete_info)
        self.AddButton.Bind(wx.EVT_BUTTON, self.add_info)
        self.RefreshButton.Bind(wx.EVT_BUTTON, self.refresh)
        self.UpdateButton.Bind(wx.EVT_BUTTON, self.updata_info)

        self.adv_select_time_use = 1
        self.select_items = wx.ComboBox(self, pos=(10, 30), size=(80, -1), choices=self.select_item_list,
                                        style=wx.CB_DROPDOWN)
        self.valueTextCtrl = wx.TextCtrl(self, value="", pos=(92, 30), size=(50, 25))
        self.test_grid('select * from ѧ��������Ϣ')

    def test_grid(self, sqlsta):
        import SqlUtil
        data = SqlUtil.query_data(sqlsta)
        col_label = ("ѧ��", "����", "��ͥ��ַ", "�Ա�", "����", "�������")
        self.testgrid = wx.grid.Grid(self, size=(880, 300), pos=(10, 60))
        row_label = []
        if len(data):
            for i in range(len(data)):
                row_label.append(i+1)
            self.testgrid.baseModel = GenericTable.GenericTable(data, row_label, col_label)
            self.testgrid.SetTable(self.testgrid.baseModel)
        else:
            wx.MessageBox('ѧ����Ϣ�����޷�����Ϣ,�������Ϣ��ˢ��', 'Warning!', wx.OK | wx.ICON_INFORMATION)

    def refresh(self, event):
        try:
            self.testgrid.Destroy()
        except Exception as e:
            print e
            pass
        self.test_grid('select * from ѧ��������Ϣ')

    def advance_quire_step1(self, event):
        try:
            self.testgrid.Destroy()
        except Exception as e:
            print e
            pass
        if self.adv_select_time_use > 1:
            self.show_adv_select_panel()
            return 0
        self.more_choice_time = 1
        select_item_list2 = [u'ѧ��������Ϣ', u'ѧ���ɼ���Ϣ', u'ѧ��������Ϣ']
        self.more_choice_button = wx.Button(self.adv_select_panel, label='More', pos=(246, 29), size=(40, 27))
        self.more_choice_button.Bind(wx.EVT_BUTTON, self.more_choice_button_fun)
        self.adv_confirm_button = wx.Button(self.adv_select_panel, pos=(85, 100), size=(100,-1), label=u'ȷ��')
        self.adv_confirm_button.Bind(wx.EVT_BUTTON, self.unshow_adv_select_panel)
        self.adv_select_table1 = wx.ComboBox(self.adv_select_panel, pos=(10, 30), size=(100, -1), choices=select_item_list2,
                                        style=wx.CB_DROPDOWN)
        self.adv_select_item1 = wx.ComboBox(self.adv_select_panel, pos=(115, 30), size=(60, -1), choices=self.select_item_list,
                                        style=wx.CB_DROPDOWN)
        self.adv_symbol1 = wx.TextCtrl(self.adv_select_panel, pos=(180, 30), size=(20, -1))
        self.adv_items_value1 = wx.TextCtrl(self.adv_select_panel, pos=(205, 30), size=(40, -1))
        self.adv_select_time_use += 1

    def unshow_adv_select_panel(self, event):
        print "more_choice_time:" + str(self.more_choice_time)
        self.more_choice_button.Show(False)
        self.adv_select_table1.Show(False)
        self.adv_select_item1.Show(False)
        self.adv_symbol1.Show(False)
        self.adv_items_value1.Show(False)
        if self.more_choice_time == 2:
            self.adv_select_table2.Show(False)
            self.adv_select_item2.Show(False)
            self.adv_symbol2.Show(False)
            self.adv_items_value2.Show(False)
        self.adv_confirm_button.Show(False)
        self.real_adv_fun()
        self.more_choice_time = 1

    def real_adv_fun(self):
        print "test:"+ str(self.more_choice_time)
        table_name1_pos = self.adv_select_table1.GetSelection()
        table_name1 = self.adv_select_table1.GetItems()[table_name1_pos]
        items_pos1 = self.adv_select_item1.GetSelection()
        item_name1 = self.adv_select_item1.GetItems()[items_pos1]
        symbol1 = self.adv_symbol1.GetRange(0,6)
        value1 = self.adv_items_value1.GetRange(0,10)
        if self.more_choice_time > 1:
            table_name2_pos = self.adv_select_table2.GetSelection()
            table_name2 = self.adv_select_table2.GetItems()[table_name2_pos]
            items_pos2 = self.adv_select_item2.GetSelection()
            item_name2 = self.adv_select_item2.GetItems()[items_pos2]
            symbol2 = self.adv_symbol2.GetRange(0,6)
            value2 = self.adv_items_value2.GetRange(0,10)
            sqlste = self.sqlstament.adv_query(table_name1,item_name1,symbol1,value1,
                                               table_name2,item_name2,symbol2,value2, 2)
        else:
            sqlste = self.sqlstament.adv_query(table_name1, item_name1, symbol1, value1, 1)
        if sqlste is not None:
            print sqlste
            self.test_grid(sqlste)

    def show_adv_select_panel(self):
        print "more1"
        self.more_choice_button.Show(True)
        self.adv_select_table1.Show(True)
        self.adv_select_item1.Show(True)
        self.adv_symbol1.Show(True)
        self.adv_items_value1.Show(True)
        self.adv_confirm_button.Show(True)
        self.more_choice_time = 1

    def more_choice_2(self):
        print "more2"
        self.adv_select_table2.Show(True)
        self.adv_select_item2.Show(True)
        self.adv_symbol2.Show(True)
        self.adv_items_value2.Show(True)
        self.more_choice_time = 2

    def more_choice_button_fun(self, event):
        if self.adv_select_time_use > 1 and self.more_use_time > 1:
            self.more_choice_2()
            return 0
        self.more_use_time = 2
        self.more_choice_time += 1
        select_item_list2 = [u'ѧ��������Ϣ', u'ѧ���ɼ���Ϣ', u'ѧ��������Ϣ']
        self.adv_select_table2 = wx.ComboBox(self.adv_select_panel, pos=(10, 70), size=(100, -1), choices=select_item_list2,
                                        style=wx.CB_DROPDOWN)
        self.adv_select_item2 = wx.ComboBox(self.adv_select_panel, pos=(115, 70), size=(60, -1), choices=self.select_item_list,
                                        style=wx.CB_DROPDOWN)
        self.adv_symbol2 = wx.TextCtrl(self.adv_select_panel, pos=(180, 70), size=(20, -1))
        self.adv_items_value2 = wx.TextCtrl(self.adv_select_panel, pos=(205, 70), size=(40, -1))

    def delete_info(self, event):
        stunum = "00000000"
        entry_dlg = wx.TextEntryDialog(self, u'����һ��\"ѧ��\"��ɾ��', u'����һ��ѧ��')
        if entry_dlg.ShowModal() == wx.ID_OK:
            stunum = entry_dlg.GetValue()
        entry_dlg.Destroy()
        if stunum:
            splited_stunum = stunum.split(' ')  # ��Ϊ�û������ѧ�ſ��ܴ��ո�,�����Ȱ��ַ����ո���,�ٽ�������.(�ָ��Ϊһ������)
        # ͬ���������ʱҲ���ո���зָ�.
            joined_stunum = ''.join(splited_stunum)  # ���ѷָ����ַ���ƴ��
            stunum = joined_stunum
        sqlsta = self.sqlstament.delete_info(self.table_name, u'ѧ��', '=', stunum)
        print sqlsta
        self.sqlstament.execute_statement(sqlsta)

    def add_info(self, event):
        stu_infos = ""
        entry_dlg = wx.TextEntryDialog(self, u'����һ��ѧ����Ϣ,��ȱ����Ϣ��0����', u'����һ����Ϣ')
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
        if select_item_value == u"����":
            sqlsta = self.sqlstament.select_info(self.table_name, select_item_value, '=', value, 666)
        else:
            sqlsta = self.sqlstament.select_info(self.table_name, select_item_value, '=', value, 333)
        print sqlsta
        self.test_grid(sqlsta)

    def updata_info(self, event):
        self.select_item_list2 = [u'��ͥסַ', u'�Ա�', u'����', u'�������']
        self.stunum_temp_label = wx.StaticText(self.second_panel, label=u"�޸Ķ���ѧ��:", pos=(0, 5))
        self.stunumvalues_temp = wx.TextCtrl(self.second_panel, size=(80, 25), pos=(82, 0))
        self.column_name_temp = wx.StaticText(self.second_panel, label=u"Ҫ�޸ĵ�����:", pos=(0, 30))
        self.select_items_temp = wx.ComboBox(self.second_panel, size=(80, 25), pos=(0, 50),
                                        choices=self.select_item_list2, style=wx.CB_DROPDOWN)
        self.change_value = wx.StaticText(self.second_panel, label=u'  �޸ĺ��ֵ:', pos=(82, 30))
        self.values_temp = wx.TextCtrl(self.second_panel, size=(80, 25), pos=(85, 50))
        self.ok_button = wx.Button(self.second_panel, label=u"ȷ���޸�", pos=(0, 80), size=(80, 25))
        self.ok_button.Bind(wx.EVT_BUTTON, self.unshow_second_panel)
        self.cancel_button = wx.Button(self.second_panel, label=u"����", pos=(85, 80), size=(80, 25))
        self.cancel_button.Bind(wx.EVT_BUTTON, self.unshow_second_panel_ele)
        self.second_panel.Show(True)

    def unshow_second_panel(self, event):
        stunum = self.stunumvalues_temp.GetRange(0, 10)
        word = self.select_items_temp.GetSelection()
        colname = self.select_items_temp.GetItems()[word]
        colvalue = self.values_temp.GetRange(0, 30)
        if colname == u'����':
            sql = self.sqlstament.alter_info(self.table_name, colname, colvalue, u'ѧ��', stunum, 666)
        else:
            sql = self.sqlstament.alter_info(self.table_name, colname, colvalue, u'ѧ��', stunum, 333)
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
        self.table_name = u'ѧ���ɼ���Ϣ'
        super(GradesOfStudent, self).__init__(*args, **kwargs)
        title_font = wx.Font(18, wx.SWISS, wx.NORMAL, wx.BOLD)  # ��������   600,100
        self.second_panel = wx.Panel(self, size=(238, 270), pos=(300, 100),
                                     style=wx.TAB_TRAVERSAL | wx.CLIP_CHILDREN | wx.FULL_REPAINT_ON_RESIZE)
        self.adv_select_panel = wx.Panel(self, size=(338, 270), pos=(30, 60),
                                     style=wx.TAB_TRAVERSAL | wx.CLIP_CHILDREN | wx.FULL_REPAINT_ON_RESIZE)

        self.select_item_list = [u'*', u'ѧ��', u'����', u'���ݿ�', u'���ԭ��', u'����ϵͳ', u'���ݽṹ',
                                 u'�㷨', u'���������', u'����', u'�ܳɼ�', u'ƽ���ɼ�', u'�ον�ʦ']
        self.sqlstament = MySQLTest()
        self.title_label = wx.StaticText(self, label=u"ѧ���ɼ�����", pos=(308, 10))
        self.title_label.SetFont(title_font)
        self.title_label.SetForegroundColour("#21c4c3")
        self.warning_label = wx.StaticText(self, label=u'ע:�˱�ֻ�ܹ���ѧ���Ѵ���ѧ������Ϣ.', pos=(283, 35))
        self.warning_label.SetForegroundColour('red')

        wx.StaticText(self, label=u"��ѯ��:", pos=(10, 10))
        wx.StaticText(self, label=u"ֵ:", pos=(96, 10))
        self.more_use_time = 1
        self.adv_select_time_use = 1
        self.SelectButton = wx.Button(self, label=u'��ѯ', pos=(144, 30), size=(33, 25))
        self.AdvanceQuireButton = wx.Button(self, label=u'�߼���ѯ', pos=(177, 30), size=(58, 25))
        self.AdvanceQuireButton.Bind(wx.EVT_BUTTON, self.advance_quire_step1)
        self.AddButton = wx.Button(self, label=u'���һ��', pos=(680, 8), size=(60, 25))
        self.DropButton = wx.Button(self, label=u'ɾ��һ��', pos=(680, 35), size=(60, 25))
        self.UpdateButton = wx.Button(self, label=u'�޸�����', pos=(740, 8), size=(60, 25))
        self.RefreshButton = wx.Button(self, label=u'ˢ��', pos=(740, 35), size=(60, 25))
        self.cal_total_and_ave = wx.Button(self, label=u'�����ܳɼ���ƽ���ɼ�', pos=(540, 35), size=(-1, 25))
        self.cal_total_and_ave.Bind(wx.EVT_BUTTON, self.calculates)
        self.SelectButton.Bind(wx.EVT_BUTTON, self.query_info)
        self.DropButton.Bind(wx.EVT_BUTTON, self.delete_info)
        self.AddButton.Bind(wx.EVT_BUTTON, self.add_info)
        self.RefreshButton.Bind(wx.EVT_BUTTON, self.refresh)
        self.UpdateButton.Bind(wx.EVT_BUTTON, self.updata_info)
        self.select_items = wx.ComboBox(self, pos=(10, 30), size=(80, -1), choices=self.select_item_list,
                                        style=wx.CB_DROPDOWN)
        self.valueTextCtrl = wx.TextCtrl(self, value="", pos=(92, 30), size=(50, 25))
        self.test_grid('select * from ѧ���ɼ���Ϣ')

    def calculates(self, event):
        self.sqlstament.cal_all_grade()
        try:
            self.testgrid.Destroy()
        except Exception as e:
            print e
            pass
        self.test_grid('select * from ѧ���ɼ���Ϣ')

    def test_grid(self, sqlsta):
        import SqlUtil
        data = SqlUtil.query_data(sqlsta)
        col_label = (u'ѧ��', u'����', u'���ݿ�', u'���ԭ��', u'����ϵͳ', u'���ݽṹ',
                     u'�㷨', u'���������', u'����', u'�ܳɼ�', u'ƽ���ɼ�', u'�ον�ʦ')
        self.testgrid = wx.grid.Grid(self, size=(800, 300), pos=(10, 60))
        row_label = []
        if len(data):
            for i in range(len(data)):
                row_label.append(i+1)
            self.testgrid.baseModel = GenericTable.GenericTable(data, row_label, col_label)
            self.testgrid.SetTable(self.testgrid.baseModel)
        else:
            wx.MessageBox('�ɼ����������Ϣ,�������Ϣ', 'Warning!', wx.OK | wx.ICON_INFORMATION)

    def refresh(self, event):
        try:
            self.testgrid.Destroy()
        except Exception as e:
            print e
            pass
        self.test_grid('select * from ѧ��������Ϣ')

    def advance_quire_step1(self, event):
        try:
            self.testgrid.Destroy()
        except Exception as e:
            print e
            pass
        if self.adv_select_time_use > 1:
            self.show_adv_select_panel()
            return 0
        self.more_choice_time = 1
        select_item_list2 = [u'ѧ��������Ϣ', u'ѧ���ɼ���Ϣ', u'ѧ��������Ϣ']
        self.more_choice_button = wx.Button(self.adv_select_panel, label='More', pos=(246, 29), size=(40, 27))
        self.more_choice_button.Bind(wx.EVT_BUTTON, self.more_choice_button_fun)
        self.adv_confirm_button = wx.Button(self.adv_select_panel, pos=(85, 100), size=(100,-1), label=u'ȷ��')
        self.adv_confirm_button.Bind(wx.EVT_BUTTON, self.unshow_adv_select_panel)
        self.adv_select_table1 = wx.ComboBox(self.adv_select_panel, pos=(10, 30), size=(100, -1), choices=select_item_list2,
                                        style=wx.CB_DROPDOWN)
        self.adv_select_item1 = wx.ComboBox(self.adv_select_panel, pos=(115, 30), size=(60, -1), choices=self.select_item_list,
                                        style=wx.CB_DROPDOWN)
        self.adv_symbol1 = wx.TextCtrl(self.adv_select_panel, pos=(180, 30), size=(20, -1))
        self.adv_items_value1 = wx.TextCtrl(self.adv_select_panel, pos=(205, 30), size=(40, -1))
        self.adv_select_time_use += 1

    def unshow_adv_select_panel(self, event):
        print "more_choice_time:" + str(self.more_choice_time)
        self.more_choice_button.Show(False)
        self.adv_select_table1.Show(False)
        self.adv_select_item1.Show(False)
        self.adv_symbol1.Show(False)
        self.adv_items_value1.Show(False)
        if self.more_choice_time == 2:
            self.adv_select_table2.Show(False)
            self.adv_select_item2.Show(False)
            self.adv_symbol2.Show(False)
            self.adv_items_value2.Show(False)
        self.adv_confirm_button.Show(False)
        self.real_adv_fun()
        self.more_choice_time = 1

    def real_adv_fun(self):
        print "test:"+ str(self.more_choice_time)
        table_name1_pos = self.adv_select_table1.GetSelection()
        table_name1 = self.adv_select_table1.GetItems()[table_name1_pos]
        items_pos1 = self.adv_select_item1.GetSelection()
        item_name1 = self.adv_select_item1.GetItems()[items_pos1]
        symbol1 = self.adv_symbol1.GetRange(0,6)
        value1 = self.adv_items_value1.GetRange(0,10)
        if self.more_choice_time > 1:
            table_name2_pos = self.adv_select_table2.GetSelection()
            table_name2 = self.adv_select_table2.GetItems()[table_name2_pos]
            items_pos2 = self.adv_select_item2.GetSelection()
            item_name2 = self.adv_select_item2.GetItems()[items_pos2]
            symbol2 = self.adv_symbol2.GetRange(0,6)
            value2 = self.adv_items_value2.GetRange(0,10)
            sqlste = self.sqlstament.adv_query(table_name1,item_name1,symbol1,value1,
                                               table_name2,item_name2,symbol2,value2, 2)
        else:
            sqlste = self.sqlstament.adv_query(table_name1, item_name1, symbol1, value1, 1)
        if sqlste is not None:
            print sqlste
            self.test_grid(sqlste)

    def show_adv_select_panel(self):
        print "more1"
        self.more_choice_button.Show(True)
        self.adv_select_table1.Show(True)
        self.adv_select_item1.Show(True)
        self.adv_symbol1.Show(True)
        self.adv_items_value1.Show(True)
        self.adv_confirm_button.Show(True)
        self.more_choice_time = 1

    def more_choice_2(self):
        print "more2"
        self.adv_select_table2.Show(True)
        self.adv_select_item2.Show(True)
        self.adv_symbol2.Show(True)
        self.adv_items_value2.Show(True)
        self.more_choice_time = 2

    def more_choice_button_fun(self, event):
        if self.adv_select_time_use > 1 and self.more_use_time > 1:
            self.more_choice_2()
            return 0
        self.more_use_time = 2
        self.more_choice_time += 1
        select_item_list2 = [u'ѧ��������Ϣ', u'ѧ���ɼ���Ϣ', u'ѧ��������Ϣ']
        self.adv_select_table2 = wx.ComboBox(self.adv_select_panel, pos=(10, 70), size=(100, -1), choices=select_item_list2,
                                        style=wx.CB_DROPDOWN)
        self.adv_select_item2 = wx.ComboBox(self.adv_select_panel, pos=(115, 70), size=(60, -1), choices=self.select_item_list,
                                        style=wx.CB_DROPDOWN)
        self.adv_symbol2 = wx.TextCtrl(self.adv_select_panel, pos=(180, 70), size=(20, -1))
        self.adv_items_value2 = wx.TextCtrl(self.adv_select_panel, pos=(205, 70), size=(40, -1))

    def refresh(self, event):
        try:
            self.testgrid.Destroy()
        except Exception as e:
            print e
            pass
        self.test_grid('select * from ѧ���ɼ���Ϣ')

    def delete_info(self, event):
        stunum = "00000000"
        entry_dlg = wx.TextEntryDialog(self, u'����һ��\"ѧ��\"��ɾ��', u'����һ��ѧ��')
        if entry_dlg.ShowModal() == wx.ID_OK:
            stunum = entry_dlg.GetValue()
        entry_dlg.Destroy()
        if stunum:
            splited_stunum = stunum.split(' ')  # ͬ�ϸ�ģ���ڵĺ���
            joined_stunum = ''.join(splited_stunum)
            stunum = joined_stunum
        sqlsta = self.sqlstament.delete_info(self.table_name, u'ѧ��', '=', stunum)
        print sqlsta
        self.sqlstament.execute_statement(sqlsta)

    def add_info(self, event):
        stu_infos = ""
        entry_dlg = wx.TextEntryDialog(self, u'����һ��ѧ����Ϣ,��ȱ����Ϣ��0����', u'����һ����Ϣ')
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
        if select_item_value == u"����":
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
        self.select_item_list2 = [u'���ݿ�', u'���ԭ��', u'����ϵͳ', u'���ݽṹ',
                                  u'�㷨', u'���������', u'����', u'�ܳɼ�', u'ƽ���ɼ�', u'�ον�ʦ']
        self.stunum_temp_label = wx.StaticText(self.second_panel, label=u"�޸Ķ���ѧ��:", pos=(0, 5))
        self.stunumvalues_temp = wx.TextCtrl(self.second_panel, size=(80, 25), pos=(82, 0))
        self.column_name_temp = wx.StaticText(self.second_panel, label=u"Ҫ�޸ĵ�����:", pos=(0, 30))
        self.select_items_temp = wx.ComboBox(self.second_panel, size=(80, 25), pos=(0, 50),
                                        choices=self.select_item_list2, style=wx.CB_DROPDOWN)
        self.change_value = wx.StaticText(self.second_panel, label=u'  �޸ĺ��ֵ:', pos=(82, 30))
        self.values_temp = wx.TextCtrl(self.second_panel, size=(80, 25), pos=(85, 50))
        self.ok_button = wx.Button(self.second_panel, label=u"ȷ���޸�", pos=(0, 80), size=(80, 25))
        self.cancel_button = wx.Button(self.second_panel, label=u"����", pos=(85, 80), size=(80, 25))
        self.ok_button.Bind(wx.EVT_BUTTON, self.unshow_second_panel)
        self.cancel_button.Bind(wx.EVT_BUTTON, self.unshow_second_panel_ele)
        self.second_panel.Show(True)

    def unshow_second_panel(self, event):
        stunum = self.stunumvalues_temp.GetRange(0, 10)
        word = self.select_items_temp.GetSelection()
        colname = self.select_items_temp.GetItems()[word]
        colvalue = self.values_temp.GetRange(0, 30)
        if colname == u'����':
            sql = self.sqlstament.alter_info(self.table_name, colname, colvalue, u'ѧ��', stunum, 666)
        else:
            sql = self.sqlstament.alter_info(self.table_name, colname, colvalue, u'ѧ��', stunum, 333)
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
        self.test_grid('select * from ѧ���ɼ���Ϣ')

    def unshow_second_panel_ele(self, event):
        self.stunumvalues_temp.Show(False)
        self.select_items_temp.Show(False)
        self.values_temp.Show(False)
        self.stunum_temp_label.Show(False)
        self.column_name_temp.Show(False)
        self.change_value.Show(False)
        self.ok_button.Show(False)
        self.cancel_button.Show(False)
        self.test_grid('select * from ѧ���ɼ���Ϣ')


class PrizeOfStudent(wx.Panel):
    def __init__(self, *args, **kwargs):
        self.sqlstament = MySQLTest()
        self.table_name = u'ѧ��������Ϣ'
        self.select_item_list = [u'*', u'ѧ��', u'����', u'����1', u'����2', u'����3', u'�׶�����', u'ʱ��']
        super(PrizeOfStudent, self).__init__(*args, **kwargs)
        title_font = wx.Font(18, wx.SWISS, wx.NORMAL, wx.BOLD)  # ��������
        self.second_panel = wx.Panel(self, size=(238, 270), pos=(655, 100),
                                     style=wx.TAB_TRAVERSAL | wx.CLIP_CHILDREN | wx.FULL_REPAINT_ON_RESIZE)
        self.adv_select_panel = wx.Panel(self, size=(338, 270), pos=(230, 60),
                                     style=wx.TAB_TRAVERSAL | wx.CLIP_CHILDREN | wx.FULL_REPAINT_ON_RESIZE)

        self.title_label = wx.StaticText(self, label=u"ѧ��������Ϣ����", pos=(308, 10))
        wx.StaticText(self, label=u"��ѯ��:", pos=(10, 10))
        wx.StaticText(self, label=u"ֵ:", pos=(96, 10))
        self.title_label.SetFont(title_font)
        self.title_label.SetForegroundColour("#21c4c3")  # ����������ɫ
        self.more_use_time = 1
        self.adv_select_time_use = 1

        self.SelectButton = wx.Button(self, label=u'��ѯ', pos=(144, 30), size=(33, 25))
        self.AdvanceQuireButton = wx.Button(self, label=u'�߼���ѯ', pos=(177, 30), size=(58, 25))
        self.AdvanceQuireButton.Bind(wx.EVT_BUTTON, self.advance_quire_step1)
        self.AddButton = wx.Button(self, label=u'���һ��', pos=(680, 8), size=(60, 25))
        self.DropButton = wx.Button(self, label=u'ɾ��һ��', pos=(680, 35), size=(60, 25))
        self.UpdateButton = wx.Button(self, label=u'�޸�����', pos=(740, 8), size=(60, 25))
        self.RefreshButton = wx.Button(self, label=u'ˢ��', pos=(740, 35), size=(60, 25))
        self.SelectButton.Bind(wx.EVT_BUTTON, self.query_info)
        self.DropButton.Bind(wx.EVT_BUTTON, self.delete_info)
        self.AddButton.Bind(wx.EVT_BUTTON, self.add_info)
        self.RefreshButton.Bind(wx.EVT_BUTTON, self.refresh)
        self.UpdateButton.Bind(wx.EVT_BUTTON, self.updata_info)

        self.select_items = wx.ComboBox(self, pos=(10, 30), size=(80, -1), choices=self.select_item_list,
                                        style=wx.CB_DROPDOWN)
        self.valueTextCtrl = wx.TextCtrl(self, value="", pos=(92, 30), size=(50, 25))
        self.test_grid('select * from ѧ��������Ϣ')

    def test_grid(self, sqlsta):
        import SqlUtil
        data = SqlUtil.query_data(sqlsta)
        col_label = ("ѧ��", "����", "����1", "����2", "����3", "�׶�����", "ʱ��")
        self.testgrid = wx.grid.Grid(self, size=(880, 300), pos=(10, 60))
        row_label = []
        if len(data):
            for i in range(len(data)):
                row_label.append(i+1)
            self.testgrid.baseModel = GenericTable.GenericTable(data, row_label, col_label)
            self.testgrid.SetTable(self.testgrid.baseModel)
        else:
            wx.MessageBox('���ͱ�������Ϣ,�������Ϣ', 'Warning!', wx.OK | wx.ICON_INFORMATION)

    def refresh(self, event):
        try:
            self.testgrid.Destroy()
        except Exception as e:
            print e
            pass
        self.test_grid('select * from ѧ��������Ϣ')

    def refresh(self, event):
        try:
            self.testgrid.Destroy()
        except Exception as e:
            print e
            pass
        self.test_grid('select * from ѧ��������Ϣ')

    def advance_quire_step1(self, event):
        try:
            self.testgrid.Destroy()
        except Exception as e:
            print e
            pass
        if self.adv_select_time_use > 1:
            self.show_adv_select_panel()
            return 0
        self.more_choice_time = 1
        select_item_list2 = [u'ѧ��������Ϣ', u'ѧ���ɼ���Ϣ', u'ѧ��������Ϣ']
        self.more_choice_button = wx.Button(self.adv_select_panel, label='More', pos=(246, 29), size=(40, 27))
        self.more_choice_button.Bind(wx.EVT_BUTTON, self.more_choice_button_fun)
        self.adv_confirm_button = wx.Button(self.adv_select_panel, pos=(85, 100), size=(100,-1), label=u'ȷ��')
        self.adv_confirm_button.Bind(wx.EVT_BUTTON, self.unshow_adv_select_panel)
        self.adv_select_table1 = wx.ComboBox(self.adv_select_panel, pos=(10, 30), size=(100, -1), choices=select_item_list2,
                                        style=wx.CB_DROPDOWN)
        self.adv_select_item1 = wx.ComboBox(self.adv_select_panel, pos=(115, 30), size=(60, -1), choices=self.select_item_list,
                                        style=wx.CB_DROPDOWN)
        self.adv_symbol1 = wx.TextCtrl(self.adv_select_panel, pos=(180, 30), size=(20, -1))
        self.adv_items_value1 = wx.TextCtrl(self.adv_select_panel, pos=(205, 30), size=(40, -1))
        self.adv_select_time_use += 1

    def unshow_adv_select_panel(self, event):
        print "more_choice_time:" + str(self.more_choice_time)
        self.more_choice_button.Show(False)
        self.adv_select_table1.Show(False)
        self.adv_select_item1.Show(False)
        self.adv_symbol1.Show(False)
        self.adv_items_value1.Show(False)
        if self.more_choice_time == 2:
            self.adv_select_table2.Show(False)
            self.adv_select_item2.Show(False)
            self.adv_symbol2.Show(False)
            self.adv_items_value2.Show(False)
        self.adv_confirm_button.Show(False)
        self.real_adv_fun()
        self.more_choice_time = 1

    def real_adv_fun(self):
        print "test:"+ str(self.more_choice_time)
        table_name1_pos = self.adv_select_table1.GetSelection()
        table_name1 = self.adv_select_table1.GetItems()[table_name1_pos]
        items_pos1 = self.adv_select_item1.GetSelection()
        item_name1 = self.adv_select_item1.GetItems()[items_pos1]
        symbol1 = self.adv_symbol1.GetRange(0,6)
        value1 = self.adv_items_value1.GetRange(0,10)
        if self.more_choice_time > 1:
            table_name2_pos = self.adv_select_table2.GetSelection()
            table_name2 = self.adv_select_table2.GetItems()[table_name2_pos]
            items_pos2 = self.adv_select_item2.GetSelection()
            item_name2 = self.adv_select_item2.GetItems()[items_pos2]
            symbol2 = self.adv_symbol2.GetRange(0,6)
            value2 = self.adv_items_value2.GetRange(0,10)
            sqlste = self.sqlstament.adv_query(table_name1,item_name1,symbol1,value1,
                                               table_name2,item_name2,symbol2,value2, 2)
        else:
            sqlste = self.sqlstament.adv_query(table_name1, item_name1, symbol1, value1, 1)
        if sqlste is not None:
            print sqlste
            self.test_grid(sqlste)

    def show_adv_select_panel(self):
        print "more1"
        self.more_choice_button.Show(True)
        self.adv_select_table1.Show(True)
        self.adv_select_item1.Show(True)
        self.adv_symbol1.Show(True)
        self.adv_items_value1.Show(True)
        self.adv_confirm_button.Show(True)
        self.more_choice_time = 1

    def more_choice_2(self):
        print "more2"
        self.adv_select_table2.Show(True)
        self.adv_select_item2.Show(True)
        self.adv_symbol2.Show(True)
        self.adv_items_value2.Show(True)
        self.more_choice_time = 2

    def more_choice_button_fun(self, event):
        if self.adv_select_time_use > 1 and self.more_use_time > 1:
            self.more_choice_2()
            return 0
        self.more_use_time = 2
        self.more_choice_time += 1
        select_item_list2 = [u'ѧ��������Ϣ', u'ѧ���ɼ���Ϣ', u'ѧ��������Ϣ']
        self.adv_select_table2 = wx.ComboBox(self.adv_select_panel, pos=(10, 70), size=(100, -1), choices=select_item_list2,
                                        style=wx.CB_DROPDOWN)
        self.adv_select_item2 = wx.ComboBox(self.adv_select_panel, pos=(115, 70), size=(60, -1), choices=self.select_item_list,
                                        style=wx.CB_DROPDOWN)
        self.adv_symbol2 = wx.TextCtrl(self.adv_select_panel, pos=(180, 70), size=(20, -1))
        self.adv_items_value2 = wx.TextCtrl(self.adv_select_panel, pos=(205, 70), size=(40, -1))

    def delete_info(self, event):
        stunum = "00000000"
        entry_dlg = wx.TextEntryDialog(self, u'����һ��\"ѧ��\"��ɾ��', u'����һ��ѧ��')
        if entry_dlg.ShowModal() == wx.ID_OK:
            stunum = entry_dlg.GetValue()
        entry_dlg.Destroy()
        if stunum:
            splited_stunum = stunum.split(' ')  # ��Ϊ�û������ѧ�ſ��ܴ��ո�,�����Ȱ��ַ����ո���,�ٽ�������.(�ָ��Ϊһ������)
        # ͬ���������ʱҲ���ո���зָ�.
            joined_stunum = ''.join(splited_stunum)  # ���ѷָ����ַ���ƴ��
            stunum = joined_stunum
        sqlsta = self.sqlstament.delete_info(self.table_name, u'ѧ��', '=', stunum)
        print sqlsta
        self.sqlstament.execute_statement(sqlsta)

    def add_info(self, event):
        stu_infos = ""
        entry_dlg = wx.TextEntryDialog(self, u'����һ��ѧ����Ϣ,��ȱ����Ϣ��0����', u'����һ����Ϣ')
        if entry_dlg.ShowModal() == wx.ID_OK:
            stu_infos = entry_dlg.GetValue()
        entry_dlg.Destroy()
        if stu_infos:
            splited_stu_info = stu_infos.split(' ')
            stunum = splited_stu_info[0]
            stuname = splited_stu_info[1]
            prize_1 = splited_stu_info[2]
            prize_2 = splited_stu_info[3]
            prize_3 = splited_stu_info[4]
            stage_ranking = splited_stu_info[5]
            the_data = splited_stu_info[6]
            sqlsta = self.sqlstament.insert_info3(self.table_name, stunum, stuname, prize_1, prize_2, prize_3,
                                                  stage_ranking, the_data)
            print sqlsta
            self.sqlstament.execute_statement(sqlsta)
        else:
            return stu_infos

    def query_info(self, event):
        self.testgrid.Destroy()
        word = self.select_items.GetSelection()
        select_item_value = self.select_items.GetItems()[word]
        value = self.valueTextCtrl.GetRange(0, 50)
        if select_item_value == u"����":
            sqlsta = self.sqlstament.select_info(self.table_name, select_item_value, '=', value, 666)
        else:
            sqlsta = self.sqlstament.select_info(self.table_name, select_item_value, '=', value, 333)
        print sqlsta
        self.test_grid(sqlsta)

    def updata_info(self, event):
        self.select_item_list2 = [u'����1', u'����2', u'����3', u'�׶�����', u'ʱ��']
        self.stunum_temp_label = wx.StaticText(self.second_panel, label=u"�޸Ķ���ѧ��:", pos=(0, 5))
        self.stunumvalues_temp = wx.TextCtrl(self.second_panel, size=(80, 25), pos=(82, 0))
        self.column_name_temp = wx.StaticText(self.second_panel, label=u"Ҫ�޸ĵ�����:", pos=(0, 30))
        self.select_items_temp = wx.ComboBox(self.second_panel, size=(80, 25), pos=(0, 50),
                                        choices=self.select_item_list2, style=wx.CB_DROPDOWN)
        self.change_value = wx.StaticText(self.second_panel, label=u'  �޸ĺ��ֵ:', pos=(82, 30))
        self.values_temp = wx.TextCtrl(self.second_panel, size=(80, 25), pos=(85, 50))
        self.ok_button = wx.Button(self.second_panel, label=u"ȷ���޸�", pos=(0, 80), size=(80, 25))
        self.ok_button.Bind(wx.EVT_BUTTON, self.unshow_second_panel)
        self.cancel_button = wx.Button(self.second_panel, label=u"����", pos=(85, 80), size=(80, 25))
        self.cancel_button.Bind(wx.EVT_BUTTON, self.unshow_second_panel_ele)
        self.second_panel.Show(True)

    def unshow_second_panel(self, event):
        stunum = self.stunumvalues_temp.GetRange(0, 10)
        word = self.select_items_temp.GetSelection()
        colname = self.select_items_temp.GetItems()[word]
        colvalue = self.values_temp.GetRange(0, 30)
        if colname == u'����':
            sql = self.sqlstament.alter_info(self.table_name, colname, colvalue, u'ѧ��', stunum, 666)
        else:
            sql = self.sqlstament.alter_info(self.table_name, colname, colvalue, u'ѧ��', stunum, 333)
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


class BackUpOfStuInfo(wx.Panel):
    def __init__(self, *args, **kwargs):
        self.sqlstament = MySQLTest()
        self.table_name = u'ѧ��������Ϣ_bak'
        self.select_item_list = [u'*', u'ѧ��', u'����', u'��ͥסַ', u'�Ա�', u'����', u'�������']
        super(BackUpOfStuInfo, self).__init__(*args, **kwargs)
        title_font = wx.Font(18, wx.SWISS, wx.NORMAL, wx.BOLD)  # ��������

        self.warning_label = wx.StaticText(self, label=u'ע:�˱�ֻ��¼��ɾ��ѧ������Ϣ', pos=(325, 35))
        self.warning_label.SetForegroundColour('red')
        self.title_label = wx.StaticText(self, label=u"ѧ��������Ϣ����", pos=(308, 10))
        wx.StaticText(self, label=u"��ѯ��:", pos=(10, 10))
        wx.StaticText(self, label=u"ֵ:", pos=(96, 10))
        self.title_label.SetFont(title_font)
        self.title_label.SetForegroundColour("#21c4c3")  # ����������ɫ
        self.SelectButton = wx.Button(self, label=u'��ѯ', pos=(144, 30), size=(33, 25))
        self.select_items = wx.ComboBox(self, pos=(10, 30), size=(80, -1), choices=self.select_item_list,
                                        style=wx.CB_DROPDOWN)
        self.valueTextCtrl = wx.TextCtrl(self, value="", pos=(92, 30), size=(50, 25))
        self.test_grid('select * from ѧ��������Ϣ_bak')
        self.SelectButton.Bind(wx.EVT_BUTTON, self.query_info)

        self.RefreshButton = wx.Button(self, label=u'ˢ��', pos=(180, 30), size=(33, 25))
        self.RefreshButton.Bind(wx.EVT_BUTTON, self.refresh)

    def test_grid(self, sqlsta):
        import SqlUtil
        data = SqlUtil.query_data(sqlsta)
        col_label = (u'ѧ��', u'����', u'��ͥסַ', u'�Ա�', u'����', u'�������')
        self.testgrid = wx.grid.Grid(self, size=(800, 300), pos=(10, 60))
        row_label = []
        if len(data):
            for i in range(len(data)):
                row_label.append(i+1)
            self.testgrid.baseModel = GenericTable.GenericTable(data, row_label, col_label)
            self.testgrid.SetTable(self.testgrid.baseModel)
        else:
            pass

    def query_info(self, event):
        self.testgrid.Destroy()
        word = self.select_items.GetSelection()
        select_item_value = self.select_items.GetItems()[word]
        value = self.valueTextCtrl.GetRange(0, 50)
        if select_item_value == u"����":
            sqlsta = self.sqlstament.select_info(self.table_name, select_item_value, '=', value, 666)
        else:
            sqlsta = self.sqlstament.select_info(self.table_name, select_item_value, '=', value, 333)
        print sqlsta
        self.test_grid(sqlsta)

    def refresh(self, event):
        self.testgrid.Destroy()
        self.test_grid('SELECT * FROM testdb.ѧ��������Ϣ_bak')
