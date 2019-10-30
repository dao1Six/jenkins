#生产环境jenkins 信息
from controlJenkins import ContrlJenlins
from excelcontrol import ExcelControl

formaljenkins = {'url':'http://jenkins.qiqiao-prod.do1.work','username':'qiqiao','password':'6LypDvN2','param_dict':{}}

#调个Jenkins控制器
jc = ContrlJenlins(url=formaljenkins['url'],username=formaljenkins['username'],password=formaljenkins['password'],param_dict =formaljenkins['param_dict'])

#调个excel控制器
ec = ExcelControl()

#excel信息
filepath = "./banche.xlsx"
sheet_name = "banche"

#生成后端要构建的服务及参数
houdaundic = ec.excle_generate_dict(filepath,sheet_name,0,1)

#生成前端要构建的服务及参数
qiandaundic = ec.excle_generate_dict(filepath,sheet_name,2,3)

#合并字典
dictMerged = dict(houdaundic, **qiandaundic)

#构建服务
for i in dictMerged.items():
    jc.server.build_job (i, parameters={'DeployVersion':i})