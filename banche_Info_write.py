from controlJenkins import ContrlJenlins
from excelcontrol import ExcelControl

prodjenkins = {'url':'http://jenkins.qiqiao-prod.do1.work','username':'qiqiao','password':'6LypDvN2'}
param_dict = {}
a = ContrlJenlins(url=prodjenkins['url'],username=prodjenkins['username'],password=prodjenkins['password'],param_dict =param_dict)
e = ExcelControl()

filepath = "./banche.xlsx"
sheet_name = "banche"


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



