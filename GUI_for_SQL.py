# coding:utf-8
# http://blog.csdn.net/chenghit/article/details/50421090
# http://www.cnblogs.com/dyx1024/archive/2012/07/05/2578579.html
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

        self.login_panel = wx.Panel(self)
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
        test = "True"
        self.login_panel.Show(False)
        print test

app = wx.App(False)
frame = RebuildFrame(None, title=u'学生数据库管理系统')
app.MainLoop()
