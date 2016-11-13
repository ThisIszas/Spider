# coding:gbk
# http://blog.csdn.net/chenghit/article/details/50421090  入门中文版
# http://www.cnblogs.com/dyx1024/archive/2012/07/05/2578579.html xxx
# http://blog.csdn.net/lyhdream/article/details/39702765
# http://www.cnblogs.com/hester/p/4696519.html
# http://blog.csdn.net/gzh0222/article/details/10376227
# http://blog.csdn.net/infoworld/article/details/17260627 grib
# http://tool.oschina.net/commons?type=3 字体颜色RGB获取网站
# http://www.yiibai.com/wxpython/wx_dialog_class.html
# http://www.cnblogs.com/ankier/archive/2012/10/14/2723364.html
import wx
import wx.grid
import PanelsFile
import GenericTable
from SQL_test import MySQLTest


class RebuildFrame(wx.Frame):  # 主框体,所有界面都往Frame里加
    def __init__(self, *args, **kwargs):
        super(RebuildFrame, self).__init__(*args, **kwargs)
        self.CreateStatusBar()
        self.show_elements = False

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
        self.username_label = wx.StaticText(self.login_panel, label=u"用户名")
        self.password = wx.StaticText(self.login_panel, label=u"密码")
        self.nameTextCtrl = wx.TextCtrl(self.login_panel, value="")
        self.passwordTextCtrl = wx.TextCtrl(self.login_panel, value=u"", style=wx.TE_PASSWORD)
        self.Bind(wx.EVT_BUTTON, self.confisrm_button, self.confirm_button)

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
                 (self.confirm_button, 350, 210, -1, -1)
                 ]:
            control.SetDimensions(x=x, y=y, width=width, height=height)

    def confisrm_button(self, event):
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


# class GradesOfStudent(wx.Panel):
#     def __init__(self, *args, **kwargs):
#         super(GradesOfStudent, self).__init__(*args, **kwargs)
#         title_font = wx.Font(18, wx.SWISS, wx.NORMAL, wx.BOLD)  # 设置字体
#
#         self.title_label = wx.StaticText(self, label=u"学生成绩管理", pos=(308, 10))
#         self.title_label.SetFont(title_font)
#         self.title_label.SetForegroundColour("#21c4c3")
#         self.warning_label = wx.StaticText(self, label=u'注:此表只能管理学号已存在学生的信息.', pos=(283, 35))
#         self.warning_label.SetForegroundColour('red')


class ATestPanel3(wx.Panel):
    def __init__(self, *args, **kwargs):
        super(ATestPanel3, self).__init__(*args, **kwargs)
        self.login_name_label = wx.StaticText(self, label=u"妈的.终于写完框架了-3", pos=(120, 160))


app = wx.App(False)
frame = RebuildFrame(None, title=u'学生数据库管理系统')
frame.Center()
app.MainLoop()
