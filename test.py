# coding:gbk
import base64

s='Author:郑立 张冬斐 詹润华'
a = base64.b64encode(s)
print a
print base64.b64decode(a)