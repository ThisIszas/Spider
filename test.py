import wx


class create_bu(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None, -1, 'Button Example',
                size=(1000, 500))
        self.panel=wx.Panel(self,-1)
        self.num = 1
        self.create_button(self.num)
        self.Show()

    def create_button(self, n):
        button_name="button"+str(n)
        self.num += 1
        print button_name
        a=wx.Button(self.panel, label=button_name, pos=(n*100, n+100))
        a.Bind(wx.EVT_BUTTON,self.create_button)
    def c(self,):
app = wx.App()
frame = create_bu()
app.MainLoop()