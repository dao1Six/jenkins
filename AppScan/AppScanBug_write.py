#使用说明：
#1、提供 AppScan xml格式报告至filepath参数

import xml.dom.minidom
from xml.etree import ElementTree as ET
from xml.dom.minidom import parse
#文件
import xlwt

from excelcontrol import ExcelControl
filepath = "20200430.xml"


per = ET.parse(filepath)
#修复建议集合
map = dict()
remediations = per.findall("./remediation-group/item")
for r in remediations:
    map[r.attrib["id"]] = r[0].text

item = per.findall("./issue-type-group/item")

workbook = xlwt.Workbook(encoding = 'ascii')
worksheet = workbook.add_sheet('My Worksheet',cell_overwrite_ok=True)
row = 0
for i in item:
    print("bug标题："+i[0].text+"   修复意见："+map[i[4][0].text])
    #写入excel

    # 参数对应 行, 列, 值
    worksheet.write(row, 0, label="【中交建运行平台安全漏洞】"+i[0].text)
    worksheet.write(row, 1, label="修复建议：  "+map[i[4][0].text])
    row = row+1
# 保存
workbook.save('AppScanReport2.xls')


