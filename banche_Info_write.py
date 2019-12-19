# 获取最新包的版本填写到班车表
import time

from controlJenkins import ContrlJenlins
from excelcontrol import ExcelControl

prodjenkins = {'url':'http://jenkins.qiqiao-prod.do1.work','username':'qiqiao','password':'6LypDvN2'}
param_dict = {}

filepath = "./banche.xlsx"
sheet_name = "banche"




a = ContrlJenlins(url=prodjenkins['url'],username=prodjenkins['username'],password=prodjenkins['password'],param_dict =param_dict)
e = ExcelControl()

#更新版本库
param_list = ['fdn-schema', 'bpms-repository', 'fdn-storage', 'bpms-appstore', 'bpms-workbench', 'fdn-authorize',
              'bpms-portal', 'bpms-operation', 'bpms-runtime', 'fdn-message', 'console-web', 'runtime-web',
              'runtime-mobile', 'operation-web']
for i in param_list:
    a.server.build_job ('other/SyncPublishVersion', parameters={'ModuleName': i, 'BuildTime': 'TODAY'})
    time.sleep (2)
    print (i)


# time.sleep(10)
jenkinsJobNames = []
#获取班车jobname数据
#后端job数据
backend = e.get_sheet_col_info(xlsxName=filepath,sheet_name=sheet_name,col_number=0)
banbenValueList = []
#获取prodjenkins上服务对应最新版本值
for i in backend:
    banbenValue = a.get_jenkinsJob_info (i)['actions'][0]['parameterDefinitions'][0]['defaultParameterValue']['value']
    banbenValueList.append(banbenValue)
    #写入excel
e.write_info_into_row(filename=filepath,datalist=banbenValueList,clo_number=1)


#前端班车jobname数据
frontend = e.get_sheet_col_info(xlsxName=filepath,sheet_name=sheet_name,col_number=2)
frontendValueList = []
#获取prodjenkins上服务对应最新版本值
for i in frontend:
    if i != "":
        frontendValue = a.get_jenkinsJob_info (i)['actions'][0]['parameterDefinitions'][0]['defaultParameterValue']['value']
        frontendValueList.append(frontendValue)
    #写入excel
e.write_info_into_row(filename=filepath,datalist=frontendValueList,clo_number=3)




