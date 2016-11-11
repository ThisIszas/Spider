# coding:utf-8
# http://blog.csdn.net/chenghit/article/details/50421090  入门中文版
# http://www.cnblogs.com/dyx1024/archive/2012/07/05/2578579.html xxx
# http://blog.csdn.net/lyhdream/article/details/39702765
# http://www.cnblogs.com/hester/p/4696519.html
# http://blog.csdn.net/gzh0222/article/details/10376227
# http://tool.oschina.net/commons?type=3 字体颜色RGB获取网站
import wx


class RebuildFrame(wx.Frame):  # 主框体,所有界面都往Frame里加
    def __init__(self, *args, **kwargs):
        super(RebuildFrame, self).__init__(*args, **kwargs)
        self.CreateStatusBar()

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
        self.notebook.Show(True)
        form1 = BaseInfoOfStudentPanel(self.notebook)
        form2 = ATestPanel2(self.notebook)
        form3 = ATestPanel3(self.notebook)
        self.notebook.AddPage(form1, u"基本信息")
        self.notebook.AddPage(form2, "test1")
        self.notebook.AddPage(form3, "test2")


class BaseInfoOfStudentPanel(wx.Panel):
    def __init__(self,  *args, **kwargs):
        super(BaseInfoOfStudentPanel, self).__init__(*args, **kwargs)
        title_font = wx.Font(18, wx.SWISS, wx.NORMAL, wx.BOLD)  # 设置字体

        self.login_name_label = wx.StaticText(self, label=u"学生基本信息管理", pos=(308, 10))
        select_item_label = wx.StaticText(self, label=u"查询项:", pos=(10, 10))
        value_label = wx.StaticText(self, label=u"值:", pos=(96, 10))
        self.login_name_label.SetFont(title_font)
        self.login_name_label.SetForegroundColour("#21c4c3")  # 设置字体颜色

        select_item_list = [u'姓名', u'家庭住址', u'性别', u'年龄', u'基本情况']
        self.SelectButton = wx.Button(self, label=u'查询', pos=(144, 30), size=(33, 25))
        select_items = wx.ComboBox(self, pos=(10, 30), size=(80, -1), choices=select_item_list,
                                   style=wx.CB_DROPDOWN)
        self.valueTextCtrl = wx.TextCtrl(self, value="", pos=(92, 30), size=(50, 25))


class ATestPanel2(wx.Panel):
    def __init__(self,  *args, **kwargs):
        super(ATestPanel2, self).__init__(*args, **kwargs)
        self.login_name_label = wx.StaticText(self, label=u"妈的.终于写完框架了-1", pos=(120, 160))


class ATestPanel3(wx.Panel):
    def __init__(self,  *args, **kwargs):
        super(ATestPanel3, self).__init__(*args, **kwargs)
        self.login_name_label = wx.StaticText(self, label=u"妈的.终于写完框架了-3", pos=(120, 160))

app = wx.App(False)
frame = RebuildFrame(None, title=u'学生数据库管理系统')
app.MainLoop()
