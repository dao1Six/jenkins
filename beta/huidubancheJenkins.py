#灰度构建
#生产环境jenkins 信息
from datetime import time
from time import strftime, localtime

from excelcontrol import ExcelControl
import jenkins
# 调个excel控制器
ec = ExcelControl()
# excel信息
filepath = "../huidubanche.xlsx"
sheet_name = "banche"
#生成后端要构建的服务及参数
houdaundic = ec.excle_generate_dict(filepath,sheet_name,0,1)
#生成前端要构建的服务及参数
qiandaundic = ec.excle_generate_dict(filepath,sheet_name,3,4)
#合并字典
dictMerged = dict(houdaundic, **qiandaundic)
print(dictMerged)

#定义用户的User Id 和 API Token，获取方式同上文
jenkins_server_url='http://jenkins.qiqiao-prod.do1.work'
user_id='qiqiao'
api_token='6LypDvN2'

#实例化jenkins对象，连接远程的jenkins master server
server=jenkins.Jenkins(jenkins_server_url, username=user_id, password=api_token)


#构建服务
for key,value in dictMerged.items():
    if key != "":
        param_dict = dict()
        param_dict['name'] = 'DeployVersion'
        param_dict['value'] = value
        print ("灰度已构建服务: " + key +"版本号为: "+ value+"  构建时间: "+strftime("%Y-%m-%d %H:%M:%S",localtime()))
        server.build_job(key,parameters=param_dict)



