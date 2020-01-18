#生产环境jenkins 信息
from controlJenkins import ContrlJenlins
from excelcontrol import ExcelControl

formaljenkins = {'url':'http://jenkins.qiqiao-prod.do1.work','username':'qiqiao','password':'6LypDvN2'}

#调个Jenkins控制器
jc = ContrlJenlins(url=formaljenkins['url'],username=formaljenkins['username'],password=formaljenkins['password'])

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
for key,value in dictMerged.items():
    parametersValue = {'DeployVersion':value}
    print(parametersValue)
    jc.server.build_job(key,param_dict=parametersValue)
