# coding:gbk
import wx.grid
import GenericTable  
import SqlUtil  
  
colLabel=("ID","版本号","类型","版本ID","显示名称")  
frameTitle="查询结果"  
  
  
class SimpleGrid(wx.grid.Grid):
    def __init__(self,parnet):  
          
        wx.grid.Grid.__init__(self,parnet,-1)  
        data = SqlUtil.queryData('select * from 学生基本信息');
        rowLabel = []  
        for i in range(len(data)):  
            rowLabel.append(i)  
        self.baseModel = GenericTable.GenericTable(data,rowLabel,colLabel)
        self.SetTable(self.baseModel)

    def GetModel(self):  
        return  self.baseModel

class TestFrame(wx.Frame):  
      
    def __init__(self,parent):  
        wx.Frame.__init__(self,parent,-1,frameTitle,size=(400,300))  
        SimpleGrid(self)  
          
if __name__=='__main__':  
    app = wx.PySimpleApp()  
    test = TestFrame(None)  
    test.Center()       
    test.Show()     
    app.MainLoop()  