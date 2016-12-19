# coding:gbk
"""
Title:ѧ�����ݿ����ϵͳ
Author:֣��, ղ��, �Ŷ��
Version:1.0
Finish Time:2016/11/14
Github: https://github.com/ThisIszas/Spider
OsChina: https://git.oschina.net/heyzas1/shujuku
"""
import wx
import wx.grid  # wx�ṩ��һ�������ı�񷽷�
import PanelsFile  # �Զ���Ľ��沼���ļ�
from SQL_test import MySQLTest  # �Զ�������ݿ�����ļ�
import base64


class RebuildFrame(wx.Frame):  # ������,���н��涼��Frame���
    def __init__(self, *args, **kwargs):
        super(RebuildFrame, self).__init__(*args, **kwargs)
        self.CreateStatusBar()  # ����һ��״̬��
        self.show_elements = False  # ���ڿ������Ԫ���Ƿ���ʾ�Ĳ���
        self.sqlexecute = MySQLTest()  # ʵ����һ��SQLexecute��,���ں�������ݿ����
        filemenu = wx.Menu()  # ����һ���˵�
        filemenu.Append(wx.ID_ABOUT, "&About", " Information about this program.")  # ���˵����"About"
        filemenu.AppendSeparator()  # ��ӷָ���
        filemenu.Append(wx.ID_INFO, "&Authors", " ֣��,ղ��,�Ŷ��")  # ͬ��

        menu_bar = wx.MenuBar()  # ����һ���˵���
        menu_bar.Append(filemenu, "&Infos")  # ���˵��������filemenu
        self.SetMenuBar(menu_bar)  # ���ò˵���������λ��

        self.login_panel = wx.Panel(self, 1)  # �½�һ�����,������¼ҳ
        self.login_panel.Bind(wx.EVT_ERASE_BACKGROUND, self.on_erase_back)  # ����ͼƬ

        self.notebook = wx.Notebook(self.login_panel, size=(830, 400))  # �ڵ�¼�����"login_panel"����ӱ�ǩҳ���
        self.notebook.Show(False)  # ��Ϊһ��ʼҪ��ʾ���ǵ�¼ҳ,���������ر�ǩҳ
        something = "QXV0aG9yOtajwaIg1cW2rOyzINWyyPO7qg=="
        author = base64.b64decode(something)

        title_font = wx.Font(16, wx.SWISS, wx.NORMAL, wx.BOLD)

        self.authors = TPStaticText(self.login_panel, ids=1, label=author, pos=(330, 250))
        self.login_name_Label = TPStaticText(self.login_panel, ids=1, label="ѧ���ɼ�����ϵͳ")
        self.login_name_Label.SetFont(title_font)
        self.confirm_button = wx.Button(self.login_panel, label=u"��¼")  # ���һ����ť,��ť����ʾ"��¼"
        self.register_button = wx.Button(self.login_panel, label=u'ע��', pos=(407, 210), size=(73, -1))
        # ���һ����ť,��ť����ʾ"ע��",���ô�С���Ϊ73,����Ĭ��ֵ,λ��Ϊ�������(407, 210)��
        self.username_label = TPStaticText(self.login_panel, ids=1, label="�û���")
        self.password = TPStaticText(self.login_panel, ids=1, label="����")
        self.register_code = TPStaticText(self.login_panel, ids=1, label="ע����", pos=(290, 120))
        self.register_code_text = wx.TextCtrl(self.login_panel, pos=(330, 117), size=(150, 25))  # �½�һ�������,��������ע����
        self.register_code.Show(False)  # ��Ϊע��ҳ��Ҫ�ڵ���ע���ų���,����һ��ʼȫ������
        self.register_code_text.Show(False)  # ͬ��
        self.nameTextCtrl = wx.TextCtrl(self.login_panel, value="")  # �½�һ�������,���������û���
        self.passwordTextCtrl = wx.TextCtrl(self.login_panel, value=u"", style=wx.TE_PASSWORD)  # �½�һ�������,������������
        self.Bind(wx.EVT_BUTTON, self.confisrm_button, self.confirm_button)  # ����Ӧ��ť���¼�
        self.register_button.Bind(wx.EVT_BUTTON, self.register_button_hide)
        self.reconfirm_button = wx.Button(self.login_panel, label=u"ȷ��", pos=(360, 210))
        self.reconfirm_button.Bind(wx.EVT_BUTTON, self.register_buttons)
        self.reconfirm_button.Show(False)

        self.do_layout()  # ������Ӧ��ť�ͱ�ǩ��λ��
        self.SetClientSize((830, 400))  # (��, ��),��������ܴ�С
        self.Show()  # ������ʾ���

    def do_layout(self):
        for control, x, y, width, height in \
                [(self.login_name_Label, 315, 90, -1, -1),
                 (self.username_label, 290, 150, -1, -1),
                 (self.nameTextCtrl, 330, 148, 150, 25),
                 (self.password, 295, 183, -1, -1),
                 (self.passwordTextCtrl, 330, 178, 150, 25),
                 (self.confirm_button, 330, 210, 73, -1)
                 ]:
            control.SetDimensions(x=x, y=y, width=width, height=height)  # ����Ӧ����������������

    def register_button_hide(self, event):  # ����ע�ᰴť�󽫲�����������,��������ʾ
        print event
        self.register_code.Show(True)
        self.register_code_text.Show(True)
        self.reconfirm_button.Show(True)
        self.login_name_Label.Show(False)
        self.confirm_button.Show(False)
        self.register_button.Show(False)

    def register_buttons(self, event):  # ע�ắ��
        print event
        username = self.nameTextCtrl.GetRange(0, 16)  # ע��ʱ��ȡ�û���������ڵ�����
        password = self.passwordTextCtrl.GetRange(0, 20)  # ע��ʱ��ȡ����������ڵ�����
        register_code = self.register_code_text.GetRange(0, 30)  # ע��ʱ��ȡע����������ڵ�����
        if register_code != "qaz":  # �ж�ע�����Ƿ���ȷ
            wx.MessageBox(u'ע�������,�ܾ�ע��,����ע����.', 'Warning', wx.OK | wx.ICON_INFORMATION)
            return 0
        if len(username) == 0 or len(password) == 0:  # ��������
            wx.MessageBox(u'�û���������Ϊ��', 'Warning', wx.OK | wx.ICON_INFORMATION)
            return 0
        rights = self.sqlexecute.register(username, password)  # ע������ȷ�һ�ȡ���û����������,
        #                                                        ����sqlexecute���ע�Ṧ��
        if rights is None:  # ��������
            wx.MessageBox(u'�û����Ѵ���', 'Warning', wx.OK | wx.ICON_INFORMATION)
            return 0
        self.reconfirm_button.Show(False)  # ���ע�����ʾ������,�����޹����
        self.login_name_Label.Show(True)
        self.confirm_button.Show(True)
        self.register_button.Show(True)
        self.register_code.Show(False)
        self.register_code_text.Show(False)

    def confisrm_button(self, event):  # ȷ�ϵ�¼
        print event
        username = self.nameTextCtrl.GetRange(0, 16)  # ͬ��
        password = self.passwordTextCtrl.GetRange(0, 20)  # ͬ��
        if len(username) == 0 or len(password) == 0:
            wx.MessageBox(u'�û���������Ϊ��', 'Warning', wx.OK | wx.ICON_INFORMATION)
            return 0
        temp = self.sqlexecute.show_data('unandpassword', 'username', username)  # ��ȡ���û�������������sqlexecute
        #                                                                          �����غ�������һ��SQL���
        temp_2 = self.sqlexecute.execute_statement(temp)  # ִ�з��ص����,������ִ�н��
        if temp_2:  # ���з��ؽ��,�ж������Ƿ�ƥ��
            temp_2 = temp_2[0]  # temp_2���淵�صĽ���������
            if password != temp_2[1]:  # ��������
                wx.MessageBox(u'�û������������', 'Warning', wx.OK | wx.ICON_INFORMATION)
                return 0
        else:  # ���޷��ؽ��,ֱ�ӵ���������Ϣ
            wx.MessageBox(u'�û������������', 'Warning', wx.OK | wx.ICON_INFORMATION)
            return 0
        base_info_of_student_panel = PanelsFile.BaseInfoOfStudentPanel  # ʵ������������һ��ģ��
        grades_of_student = PanelsFile.GradesOfStudent
        prize_of_student = PanelsFile.PrizeOfStudent
        backup_of_stuinfo = PanelsFile.BackUpOfStuInfo
        self.show_elements = False
        self.show_element(self.show_elements)
        self.notebook.Show(True)
        form1 = base_info_of_student_panel(self.notebook)  # ʵ������Ӧ�ı�ǩҳ
        form2 = grades_of_student(self.notebook)
        form3 = prize_of_student(self.notebook)
        form4 = backup_of_stuinfo(self.notebook)
        self.notebook.AddPage(form1, u"������Ϣ")  # �����Ӧ�ı�ǩҳ
        self.notebook.AddPage(form2, u"�ɼ���Ϣ")
        self.notebook.AddPage(form3, u"������Ϣ")
        self.notebook.AddPage(form4, u'������Ϣ')

    def show_element(self, show_elements):  # ��½��,���ص�¼ҳ������
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

    def on_erase_back(self, event):
        dc = event.GetDC()
        if not dc:
            dc = wx.ClientDC(self)
            rect = self.GetUpdateRegion().GetBox()
            dc.SetClippingRect(rect)
        dc.Clear()
        bmp = wx.Bitmap("background.jpg")
        dc.DrawBitmap(bmp, 0, 0)


class TPStaticText(wx.StaticText):
    """ transparent StaticText """
    def __init__(self, parent, ids, label='',
                 pos=wx.DefaultPosition,
                 size=wx.DefaultSize,
                 style=0,
                 ):
        style |= wx.CLIP_CHILDREN | wx.TRANSPARENT_WINDOW
        wx.StaticText.__init__(self, parent, ids, label, pos, size, style=style)
        self.SetBackgroundStyle(wx.BG_STYLE_CUSTOM)
        self.Bind(wx.EVT_PAINT, self.OnPaint)

    def OnPaint(self, event):
        event.Skip()
        dc = wx.GCDC(wx.PaintDC(self))
        dc.SetFont(self.GetFont())
        dc.DrawText(self.GetLabel(), 0, 0)

app = wx.App(False)
frame = RebuildFrame(None, title=u'ѧ�����ݿ����ϵͳ')
frame.Center()
app.MainLoop()
