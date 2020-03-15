#生产环境jenkins 信息
from controlJenkins import ContrlJenlins
from excelcontrol import ExcelControl
import jenkins
#调个excel控制器
ec = ExcelControl()
# excel信息
filepath = "./huidubanche.xlsx"
sheet_name = "banche"
#生成后端要构建的服务及参数
houdaundic = ec.excle_generate_dict(filepath,sheet_name,0,1)
#生成前端要构建的服务及参数
qiandaundic = ec.excle_generate_dict(filepath,sheet_name,2,3)
#合并字典
dictMerged = dict(houdaundic, **qiandaundic)
print(dictMerged)

#定义用户的User Id 和 API Token，获取方式同上文
jenkins_server_url='http://jenkins.qiqiao-prod.do1.work'
user_id='qiqiao'
api_token='6LypDvN2'

#实例化jenkins对象，连接远程的jenkins master server
server=jenkins.Jenkins(jenkins_server_url, username=user_id, password=api_token)


info = server.get_job_info(name='beta/backend/bpms-operation')
print(info)

server.build_job(name='beta/backend/bpms-operation',parameters={'DeployVersion': 'v20200225-160902'})









# formaljenkins = {'url':'http://jenkins.qiqiao-prod.do1.work','username':'qiqiao','password':'6LypDvN2'}



# #调个excel控制器
# ec = ExcelControl()
#
# #excel信息
# filepath = "./huidubanche.xlsx"
# sheet_name = "banche"
#
# #生成后端要构建的服务及参数
# houdaundic = ec.excle_generate_dict(filepath,sheet_name,0,1)
#
#
# #生成前端要构建的服务及参数
# qiandaundic = ec.excle_generate_dict(filepath,sheet_name,2,3)
#
# #合并字典
# dictMerged = dict(houdaundic, **qiandaundic)
# print(dictMerged)
#
#
# #调个Jenkins控制器
#
# server = jenkins.Jenkins (url=formaljenkins['url'],username=formaljenkins['username'],password=formaljenkins['password'], timeout=50)
#
#
# #构建服务
# # for key,value in dictMerged.items():
# #     param_dict = dict()
# #     param_dict['DeployVersion'] = value
# #     a.build_job(key,parameters=param_dict)
#
# server.build_job('beta/backend/fdn-schema',{'DeployVersion': 'v20200220-151739'})
