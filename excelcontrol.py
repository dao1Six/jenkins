import os

import xlrd,xlwt,xlutils
from xlutils.copy import copy
import openpyxl

class ExcelControl():
    """"""

    #
    def OpenXlxs(self,xlsxName,sheet_name):
        readOpenXlsx = xlrd.open_workbook (xlsxName)

        readXlsxSheet = readOpenXlsx.sheet_by_name (sheet_name)
        # copy管道作用
        writeOpenXlsx = copy (readOpenXlsx)

        return readXlsxSheet, writeOpenXlsx, xlsxName


    #获取文件某列数据
    def get_sheet_col_info(self,xlsxName,sheet_name,col_number):
        readOpenXlsx = xlrd.open_workbook (xlsxName)
        readXlsxSheet = readOpenXlsx.sheet_by_name(sheet_name)
        # 获取行数
        rowMax = readXlsxSheet.nrows
        # 获取列数
        colMax = readXlsxSheet.ncols
        result = []
        for r in range (0,rowMax):
            alldata = readXlsxSheet.row_values (r)  # 循环输出excel表中每一行，即所有数据
            cloValue = alldata[col_number]  # 取出表中某列数据
            result.append(cloValue)
        return result

    #给文件某列写入数据
    def write_info_into_row(self,filename,datalist,clo_number):
        book = xlrd.open_workbook (filename)  # 打开excel
        work_book = copy (book)  # 复制excel
        sheet = work_book.get_sheet(0)  # 获取表格的数据
        rowMax = len(datalist)
        for r in range(0,rowMax):
            sheet.write (r, clo_number,datalist[r])  # 修改行列的数据
            work_book.save (filename)  # 保存excel


    #获取两列数据生成字典
    def excle_generate_dict(self,xlsxName,sheet_name,keycol_number,col_number):
        readOpenXlsx = xlrd.open_workbook (xlsxName)
        readXlsxSheet = readOpenXlsx.sheet_by_name(sheet_name)
        # 获取行数
        rowMax = readXlsxSheet.nrows
        # 获取列数
        colMax = readXlsxSheet.ncols
        dic = {}
        for r in range (0,rowMax):
            alldata = readXlsxSheet.row_values (r)  # 循环输出excel表中每一行，即所有数据
            clokeyValue = alldata[keycol_number]  # 取出表中某列数据
            cloValue = alldata[col_number]  # 取出表中某列数据
            dic[clokeyValue] = cloValue
        return dic

    def baseWrite(self,sheetName,):
        workbook = xlwt.Workbook(encoding='utf-8')
        # 创建一个worksheet
        worksheet = workbook.add_sheet(sheetName)

        # 写入excel
        # 参数对应 行, 列, 值
        worksheet.write(1, 0, label='this is test')
        # 保存
        workbook.save('Excel_test.xls')



if __name__ == '__main__':
    filepath = "./banche.xlsx"
    sheet_name = "banche"
    e = ExcelControl()
    # result = e.get_sheet_col_info(filepath,sheet_name,0)
    # print(result)
    # e.write_info_into_row(filepath,datalist=result,clo_number=5)
    dic = e.excle_generate_dict(filepath,sheet_name,0,1)
    print(type(dic))
    for i in dic.items():
        print(i)




