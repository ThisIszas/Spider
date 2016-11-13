# coding:gbk
import wx
import wx.grid
import PanelsFile
from SQL_test import MySQLTest


class RebuildFrame(wx.Frame):  # 主框体,所有界面都往Frame里加
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

        self.login_name_Label = wx.StaticText(self.login_panel, label=u"学生成绩管理系统")
        self.confirm_button = wx.Button(self.login_panel, label=u"登录")
        self.register_button = wx.Button(self.login_panel, label=u'注册', pos=(407, 210), size=(73, -1))
        self.username_label = wx.StaticText(self.login_panel, label=u"用户名")
        self.password = wx.StaticText(self.login_panel, label=u"密码")
        self.nameTextCtrl = wx.TextCtrl(self.login_panel, value="")
        self.passwordTextCtrl = wx.TextCtrl(self.login_panel, value=u"", style=wx.TE_PASSWORD)
        self.Bind(wx.EVT_BUTTON, self.confisrm_button, self.confirm_button)
        self.register_button.Bind(wx.EVT_BUTTON, self.register_button_hide)
        self.reconfirm_button = wx.Button(self.login_panel, label=u"确定", pos=(360, 210))
        self.reconfirm_button.Bind(wx.EVT_BUTTON, self.register_buttons)
        self.reconfirm_button.Show(False)

        self.do_layout()
        self.SetClientSize((830, 400))  # (宽, 高)
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
        self.reconfirm_button.Show(True)
        self.login_name_Label.Show(False)
        self.confirm_button.Show(False)
        self.register_button.Show(False)

    def register_buttons(self, event):
        username = self.nameTextCtrl.GetRange(0, 16)
        password = self.passwordTextCtrl.GetRange(0, 20)
        rights = self.sqlexecute.register(username, password)
        if rights is None:
            wx.MessageBox(u'用户名已存在', 'Warning', wx.OK | wx.ICON_INFORMATION)
            return 0
        self.reconfirm_button.Show(False)
        self.login_name_Label.Show(True)
        self.confirm_button.Show(True)
        self.register_button.Show(True)

    def confisrm_button(self, event):
        username = self.nameTextCtrl.GetRange(0, 16)
        password = self.passwordTextCtrl.GetRange(0, 20)
        temp = self.sqlexecute.show_data('unandpassword', 'username', username)
        temp_2 = self.sqlexecute.execute_statement(temp)
        if temp_2:
            temp_2 = temp_2[0]
            if password != temp_2[1]:
                wx.MessageBox(u'用户名或密码错误', 'Warning', wx.OK | wx.ICON_INFORMATION)
                return 0
        else:
            wx.MessageBox(u'用户名或密码错误', 'Warning', wx.OK | wx.ICON_INFORMATION)
            return 0
        base_info_of_student_panel = PanelsFile.BaseInfoOfStudentPanel
        grades_of_student = PanelsFile.GradesOfStudent
        self.show_elements = False
        self.show_element(self.show_elements)
        self.notebook.Show(True)
        form1 = base_info_of_student_panel(self.notebook)
        form2 = grades_of_student(self.notebook)
        form3 = ATestPanel3(self.notebook)
        self.notebook.AddPage(form1, u"基本信息")
        self.notebook.AddPage(form2, u"成绩信息")
        self.notebook.AddPage(form3, "test2")

    def show_element(self, show_elements):
        self.login_name_Label.Show(show_elements)
        self.confirm_button.Show(show_elements)
        self.username_label.Show(show_elements)
        self.password.Show(show_elements)
        self.nameTextCtrl.Show(show_elements)
        self.passwordTextCtrl.Show(show_elements)
        self.register_button.Show(show_elements)


class ATestPanel3(wx.Panel):
    def __init__(self, *args, **kwargs):
        super(ATestPanel3, self).__init__(*args, **kwargs)
        self.login_name_label = wx.StaticText(self, label=u"妈的.终于写完框架了-3", pos=(120, 160))


app = wx.App(False)
frame = RebuildFrame(None, title=u'学生数据库管理系统')
frame.Center()
app.MainLoop()
