import xml.dom.minidom
from xml.etree import ElementTree as ET

#文件
filepath = "../20200429.xml"

per = ET.parse(filepath)
p = per.findall("./issue-type-group/item")
print(len(p))
for opener in p:
    for child in opener.getchildren():
        print(child.tag, ":", child.text)


#解析AppScan XML报告文件

#获取xml文档对象（对子节点和节点node都适用）

#获取bug标题




#获取bug内容


#写入excel文件
