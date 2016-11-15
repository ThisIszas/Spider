# coding:gbk
# http://blog.csdn.net/chenghit/article/details/50421090  �������İ�
# http://www.cnblogs.com/dyx1024/archive/2012/07/05/2578579.html xxx
# http://blog.csdn.net/lyhdream/article/details/39702765
# http://www.cnblogs.com/hester/p/4696519.html
# http://blog.csdn.net/gzh0222/article/details/10376227
# http://blog.csdn.net/infoworld/article/details/17260627 grib
# http://tool.oschina.net/commons?type=3 ������ɫRGB��ȡ��վ
# http://www.yiibai.com/wxpython/wx_dialog_class.html
# http://www.cnblogs.com/ankier/archive/2012/10/14/2723364.html
import wx
import wx.grid
import PanelsFile
from SQL_test import MySQLTest


class RebuildFrame(wx.Frame):  # ������,���н��涼��Frame���
    def __init__(self, *args, **kwargs):
        super(RebuildFrame, self).__init__(*args, **kwargs)
        self.CreateStatusBar()
        self.show_elements = False
        self.sqlexecute = MySQLTest()
        filemenu = wx.Menu()
        filemenu.Append(wx.ID_ABOUT, "&About", " Information about this program.")
        filemenu.AppendSeparator()
        filemenu.Append(wx.ID_EXIT, "&Save", " Save information.")
        filemenu.AppendSeparator()
        filemenu.Append(wx.ID_EXIT, "&Exit", " Terminate the program.")

        menu_bar = wx.MenuBar()
        menu_bar.Append(filemenu, "&File")
        self.SetMenuBar(menu_bar)

        self.login_panel = wx.Panel(self, 1)

        self.notebook = wx.Notebook(self.login_panel, size=(830, 400))
        self.notebook.Show(False)

        self.login_name_Label = wx.StaticText(self.login_panel, label=u"ѧ���ɼ�����ϵͳ")
        self.confirm_button = wx.Button(self.login_panel, label=u"��¼")
        self.register_button = wx.Button(self.login_panel, label=u'ע��', pos=(407, 210), size=(73, -1))
        self.username_label = wx.StaticText(self.login_panel, label=u"�û���")
        self.password = wx.StaticText(self.login_panel, label=u"����")
        self.register_code = wx.StaticText(self.login_panel, label=u'ע����', pos=(290, 120))
        self.register_code_text = wx.TextCtrl(self.login_panel, pos=(330, 117), size=(150, 25))
        self.register_code.Show(False)
        self.register_code_text.Show(False)
        self.nameTextCtrl = wx.TextCtrl(self.login_panel, value="")
        self.passwordTextCtrl = wx.TextCtrl(self.login_panel, value=u"", style=wx.TE_PASSWORD)
        self.Bind(wx.EVT_BUTTON, self.confisrm_button, self.confirm_button)
        self.register_button.Bind(wx.EVT_BUTTON, self.register_button_hide)
        self.reconfirm_button = wx.Button(self.login_panel, label=u"ȷ��", pos=(360, 210))
        self.reconfirm_button.Bind(wx.EVT_BUTTON, self.register_buttons)
        self.reconfirm_button.Show(False)

        self.do_layout()
        self.SetClientSize((830, 400))  # (��, ��)
        self.Show()

    def do_layout(self):
        for control, x, y, width, height in \
                [(self.login_name_Label, 360, 90, -1, -1),
                 (self.username_label, 290, 150, -1, -1),
                 (self.nameTextCtrl, 330, 148, 150, 25),
                 (self.password, 295, 183, -1, -1),
                 (self.passwordTextCtrl, 330, 178, 150, 25),
                 (self.confirm_button, 330, 210, 73, -1)
                 ]:
            control.SetDimensions(x=x, y=y, width=width, height=height)

    def register_button_hide(self, event):
        self.register_code.Show(True)
        self.register_code_text.Show(True)
        self.reconfirm_button.Show(True)
        self.login_name_Label.Show(False)
        self.confirm_button.Show(False)
        self.register_button.Show(False)

    def register_buttons(self, event):
        username = self.nameTextCtrl.GetRange(0, 16)
        password = self.passwordTextCtrl.GetRange(0, 20)
        register_code = self.register_code_text.GetRange(0, 30)
        if register_code != "sjuxhnsk45fds":
            wx.MessageBox(u'ע�������,�ܾ�ע��,����ע����.', 'Warning', wx.OK | wx.ICON_INFORMATION)
            return 0
        if len(username) == 0 or len(password) == 0:
            wx.MessageBox(u'�û���������Ϊ��', 'Warning', wx.OK | wx.ICON_INFORMATION)
            return 0
        rights = self.sqlexecute.register(username, password)
        if rights is None:
            wx.MessageBox(u'�û����Ѵ���', 'Warning', wx.OK | wx.ICON_INFORMATION)
            return 0
        self.reconfirm_button.Show(False)
        self.login_name_Label.Show(True)
        self.confirm_button.Show(True)
        self.register_button.Show(True)
        self.register_code.Show(False)
        self.register_code_text.Show(False)

    def confisrm_button(self, event):
        username = self.nameTextCtrl.GetRange(0, 16)
        password = self.passwordTextCtrl.GetRange(0, 20)
        if len(username) == 0 or len(password) == 0:
            wx.MessageBox(u'�û���������Ϊ��', 'Warning', wx.OK | wx.ICON_INFORMATION)
            return 0
        temp = self.sqlexecute.show_data('unandpassword', 'username', username)
        temp_2 = self.sqlexecute.execute_statement(temp)
        if temp_2:
            temp_2 = temp_2[0]
            if password != temp_2[1]:
                wx.MessageBox(u'�û������������', 'Warning', wx.OK | wx.ICON_INFORMATION)
                return 0
        else:
            wx.MessageBox(u'�û������������', 'Warning', wx.OK | wx.ICON_INFORMATION)
            return 0
        base_info_of_student_panel = PanelsFile.BaseInfoOfStudentPanel
        grades_of_student = PanelsFile.GradesOfStudent
        prize_of_student = PanelsFile.PrizeOfStudent
        backup_of_stuinfo = PanelsFile.BackUpOfStuInfo
        self.show_elements = False
        self.show_element(self.show_elements)
        self.notebook.Show(True)
        form1 = base_info_of_student_panel(self.notebook)
        form2 = grades_of_student(self.notebook)
        form3 = prize_of_student(self.notebook)
        form4 = backup_of_stuinfo(self.notebook)
        self.notebook.AddPage(form1, u"������Ϣ")
        self.notebook.AddPage(form2, u"�ɼ���Ϣ")
        self.notebook.AddPage(form3, u"������Ϣ")
        self.notebook.AddPage(form4, u'������Ϣ')

    def show_element(self, show_elements):
        self.login_name_Label.Show(show_elements)
        self.confirm_button.Show(show_elements)
        self.username_label.Show(show_elements)
        self.password.Show(show_elements)
        self.nameTextCtrl.Show(show_elements)
        self.passwordTextCtrl.Show(show_elements)
        self.register_button.Show(show_elements)
        self.register_code.Show(show_elements)
        self.register_code_text.Show(show_elements)




app = wx.App(False)
frame = RebuildFrame(None, title=u'ѧ�����ݿ����ϵͳ')
frame.Center()
app.MainLoop()
