# coding:gbk
import base64

s='Author:֣�� �Ŷ�� ղ��'
a = base64.b64encode(s)
print a
print base64.b64decode(a)