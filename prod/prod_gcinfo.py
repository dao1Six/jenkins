# 获取最新包的版本填写到班车表
import time

import jenkins

from controlJenkins import ContrlJenlins
from excelcontrol import ExcelControl

prodjenkins = {'url':'http://jenkins.qiqiao-prod.do1.work','username':'qiqiao','password':'6LypDvN2'}
param_dict = {}

filepath = "../banche.xlsx"
sheet_name = "banche"




# a = ContrlJenlins(url=prodjenkins['url'],username=prodjenkins['username'],password=prodjenkins['password'])
e = ExcelControl()

server = jenkins.Jenkins(url=prodjenkins['url'], username=prodjenkins['username'],password=prodjenkins['password'])







#后端job数据
backend = e.get_sheet_col_info(xlsxName=filepath,sheet_name=sheet_name,col_number=0)
parametersValueList = []
#获取job名为name的job的最后次构建号， 不会计算排队中的构建，
#例如正在构建的number是3， 在排队的有4和5， 那么最后次构建号是3
for i in backend:
    banbenValue = server.get_job_info(i)['lastBuild']
    number = banbenValue['number']
    info = server.get_build_info(i, number)
    param = info['actions'][0]['parameters'][0]['value']
    # banbenValue = a.get_jenkinsJob_info (i)['actions'][0]['parameterDefinitions'][0]['defaultParameterValue']['value']
    parametersValueList.append(param)
    #写入excel

e.write_info_into_row(filename=filepath,datalist=parametersValueList,clo_number=2)


#前端班车jobname数据
frontend = e.get_sheet_col_info(xlsxName=filepath,sheet_name=sheet_name,col_number=3)
frontendValueList = []
#获取prodjenkins上服务对应最新版本值
for i in frontend:
    if i != "":
        banbenValue = server.get_job_info(i)['lastBuild']
        number = banbenValue['number']
        info = server.get_build_info(i, number)
        param = info['actions'][0]['parameters'][0]['value']
        frontendValueList.append(param)
    #写入excel

e.write_info_into_row(filename=filepath,datalist=frontendValueList,clo_number=5)



