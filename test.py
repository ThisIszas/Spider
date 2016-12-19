import wx
class TPStaticText(wx.StaticText):
    """ transparent StaticText """
    def __init__(self,parent,id,label='',
                 pos=wx.DefaultPosition,
                 size=wx.DefaultSize,
                 style=0,
                 name = 'TPStaticText'):
        style |= wx.CLIP_CHILDREN | wx.TRANSPARENT_WINDOW
        wx.StaticText.__init__(self,parent,id,label,pos,size,style = style)
        self.SetBackgroundStyle(wx.BG_STYLE_CUSTOM)
        self.Bind(wx.EVT_PAINT,self.OnPaint)
    def OnPaint(self,event):
        event.Skip()
        dc = wx.GCDC(wx.PaintDC(self) )
        dc.SetFont(self.GetFont())
        dc.DrawText(self.GetLabel(), 0, 0)

