# coding:gbk
"""
Title:学生数据库管理系统
Author:郑立, 詹润华, 张冬斐
Version:1.0
Finish Time:2016/11/14
Github: https://github.com/ThisIszas/Spider
OsChina: https://git.oschina.net/heyzas1/SQLDesign
"""
import wx
import wx.grid  # wx提供的一个创建的表格方法
import PanelsFile  # 自定义的界面布局文件
from SQL_test import MySQLTest  # 自定义的数据库操作文件
import base64


class RebuildFrame(wx.Frame):  # 主框体,所有界面都往Frame里加
    def __init__(self, *args, **kwargs):
        super(RebuildFrame, self).__init__(*args, **kwargs)
        self.CreateStatusBar()  # 创建一个状态栏
        self.show_elements = False  # 用于控制面板元素是否显示的参数
        self.sqlexecute = MySQLTest()  # 实例化一个SQLexecute类,用于后面的数据库操作
        filemenu = wx.Menu()  # 创建一个菜单
        filemenu.Append(wx.ID_ABOUT, "&About", " Information about this program.")  # 往菜单里加"About"
        filemenu.AppendSeparator()  # 添加分割线
        filemenu.Append(wx.ID_EXIT, "&Save", " Save information.")  # 同上
        filemenu.AppendSeparator()
        filemenu.Append(wx.ID_EXIT, "&Exit", " Terminate the program.")

        menu_bar = wx.MenuBar()  # 创建一个菜单栏
        menu_bar.Append(filemenu, "&File")  # 往菜单栏里添加filemenu
        self.SetMenuBar(menu_bar)  # 设置菜单栏到合适位置

        self.login_panel = wx.Panel(self, 1)  # 新建一个面板,用作登录页

        self.notebook = wx.Notebook(self.login_panel, size=(830, 400))  # 在登录面板里"login_panel"里添加标签页面板
        self.notebook.Show(False)  # 因为一开始要显示得是登录页,所以先隐藏标签页
        something = "QXV0aG9yOtajwaIg1cW2rOyzINWyyPO7qg=="
        author = base64.b64decode(something)

        self.authors = wx.StaticText(self.login_panel, label=author, pos=(330, 250))
        self.login_name_Label = wx.StaticText(self.login_panel, label=u"学生成绩管理系统")
        # 在login_panel内添加一个标签,标签内容为"学生成绩管理系统", u表示将后面内容按UTF-8格式编码
        self.confirm_button = wx.Button(self.login_panel, label=u"登录")  # 添加一个按钮,按钮上显示"登录"
        self.register_button = wx.Button(self.login_panel, label=u'注册', pos=(407, 210), size=(73, -1))
        # 添加一个按钮,按钮上显示"注册",设置大小宽度为73,长度默认值,位置为相对坐标(407, 210)处
        self.username_label = wx.StaticText(self.login_panel, label=u"用户名")  # 同上
        self.password = wx.StaticText(self.login_panel, label=u"密码")  # 同上
        self.register_code = wx.StaticText(self.login_panel, label=u'注册码', pos=(290, 120))  # 同上
        self.register_code_text = wx.TextCtrl(self.login_panel, pos=(330, 117), size=(150, 25))  # 新建一个输入框,用以输入注册码
        self.register_code.Show(False)  # 因为注册页面要在点了注册后才出现,所以一开始全都隐藏
        self.register_code_text.Show(False)  # 同上
        self.nameTextCtrl = wx.TextCtrl(self.login_panel, value="")  # 新建一个输入框,用以输入用户名
        self.passwordTextCtrl = wx.TextCtrl(self.login_panel, value=u"", style=wx.TE_PASSWORD)  # 新建一个输入框,用以输入密码
        self.Bind(wx.EVT_BUTTON, self.confisrm_button, self.confirm_button)  # 绑定相应按钮的事件
        self.register_button.Bind(wx.EVT_BUTTON, self.register_button_hide)
        self.reconfirm_button = wx.Button(self.login_panel, label=u"确定", pos=(360, 210))
        self.reconfirm_button.Bind(wx.EVT_BUTTON, self.register_buttons)
        self.reconfirm_button.Show(False)

        self.do_layout()  # 设置相应按钮和标签的位置
        self.SetClientSize((830, 400))  # (宽, 高),设置主框架大小
        self.Show()  # 设置显示框架

    def do_layout(self):
        for control, x, y, width, height in \
                [(self.login_name_Label, 360, 90, -1, -1),
                 (self.username_label, 290, 150, -1, -1),
                 (self.nameTextCtrl, 330, 148, 150, 25),
                 (self.password, 295, 183, -1, -1),
                 (self.passwordTextCtrl, 330, 178, 150, 25),
                 (self.confirm_button, 330, 210, 73, -1)
                 ]:
            control.SetDimensions(x=x, y=y, width=width, height=height)  # 将相应组件按后面参数设置

    def register_button_hide(self, event):  # 点了注册按钮后将不相关组件隐藏,相关组件显示
        print event
        self.register_code.Show(True)
        self.register_code_text.Show(True)
        self.reconfirm_button.Show(True)
        self.login_name_Label.Show(False)
        self.confirm_button.Show(False)
        self.register_button.Show(False)

    def register_buttons(self, event):  # 注册函数
        print event
        username = self.nameTextCtrl.GetRange(0, 16)  # 注册时获取用户名输入框内的文字
        password = self.passwordTextCtrl.GetRange(0, 20)  # 注册时获取密码输入框内的文字
        register_code = self.register_code_text.GetRange(0, 30)  # 注册时获取注册码输入框内的文字
        if register_code != "qaz":  # 判断注册码是否正确
            wx.MessageBox(u'注册码错误,拒绝注册,请检查注册码.', 'Warning', wx.OK | wx.ICON_INFORMATION)
            return 0
        if len(username) == 0 or len(password) == 0:  # 很明显了
            wx.MessageBox(u'用户名或密码为空', 'Warning', wx.OK | wx.ICON_INFORMATION)
            return 0
        rights = self.sqlexecute.register(username, password)  # 注册码正确且获取到用户名和密码后,
        #                                                        调用sqlexecute里的注册功能
        if rights is None:  # 很明显了
            wx.MessageBox(u'用户名已存在', 'Warning', wx.OK | wx.ICON_INFORMATION)
            return 0
        self.reconfirm_button.Show(False)  # 完成注册后显示相关组件,隐藏无关组件
        self.login_name_Label.Show(True)
        self.confirm_button.Show(True)
        self.register_button.Show(True)
        self.register_code.Show(False)
        self.register_code_text.Show(False)

    def confisrm_button(self, event):  # 确认登录函数
        print event
        username = self.nameTextCtrl.GetRange(0, 16)  # 同上
        password = self.passwordTextCtrl.GetRange(0, 20)  # 同上
        if len(username) == 0 or len(password) == 0:
            wx.MessageBox(u'用户名或密码为空', 'Warning', wx.OK | wx.ICON_INFORMATION)
            return 0
        temp = self.sqlexecute.show_data('unandpassword', 'username', username)  # 获取到用户名和密码后调用sqlexecute
        #                                                                          里的相关函数返回一条SQL语句
        temp_2 = self.sqlexecute.execute_statement(temp)  # 执行返回的语句,并返回执行结果
        if temp_2:  # 若有返回结果,判断密码是否匹配
            temp_2 = temp_2[0]  # temp_2储存返回的结果里的密码
            if password != temp_2[1]:  # 很明显了
                wx.MessageBox(u'用户名或密码错误', 'Warning', wx.OK | wx.ICON_INFORMATION)
                return 0
        else:  # 若无返回结果,直接弹出错误信息
            wx.MessageBox(u'用户名或密码错误', 'Warning', wx.OK | wx.ICON_INFORMATION)
            return 0
        base_info_of_student_panel = PanelsFile.BaseInfoOfStudentPanel  # 实例化面板类里的一个模块
        grades_of_student = PanelsFile.GradesOfStudent
        prize_of_student = PanelsFile.PrizeOfStudent
        backup_of_stuinfo = PanelsFile.BackUpOfStuInfo
        self.show_elements = False
        self.show_element(self.show_elements)
        self.notebook.Show(True)
        form1 = base_info_of_student_panel(self.notebook)  # 实例化相应的标签页
        form2 = grades_of_student(self.notebook)
        form3 = prize_of_student(self.notebook)
        form4 = backup_of_stuinfo(self.notebook)
        self.notebook.AddPage(form1, u"基本信息")  # 添加相应的标签页
        self.notebook.AddPage(form2, u"成绩信息")
        self.notebook.AddPage(form3, u"奖惩信息")
        self.notebook.AddPage(form4, u'备份信息')

    def show_element(self, show_elements):  # 登陆后,隐藏登录页的内容
        self.login_name_Label.Show(show_elements)
        self.confirm_button.Show(show_elements)
        self.username_label.Show(show_elements)
        self.password.Show(show_elements)
        self.nameTextCtrl.Show(show_elements)
        self.passwordTextCtrl.Show(show_elements)
        self.register_button.Show(show_elements)
        self.register_code.Show(show_elements)
        self.register_code_text.Show(show_elements)
        self.authors.Show(show_elements)

app = wx.App(False)
frame = RebuildFrame(None, title=u'学生数据库管理系统')
frame.Center()
app.MainLoop()
