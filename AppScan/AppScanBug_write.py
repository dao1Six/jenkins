import xml.dom.minidom
from xml.etree import ElementTree as ET
from xml.dom.minidom import parse
#文件
filepath = "../20200429.xml"

per = ET.parse(filepath)
p = per.findall("./issue-type-group/item/name")
for i in p:
    print(i.text)

# DOMTree=parse(filepath)
# booklist=DOMTree.documentElement
# books=booklist.getElementsByTagName('issue-type-group')
# list = books[0].childNodes
# for i in list:
#     print(i)


#解析AppScan XML报告文件

#获取xml文档对象（对子节点和节点node都适用）

#获取bug标题




#获取bug内容


#写入excel文件
