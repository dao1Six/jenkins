# -!- coding: utf-8 -!-
import json
import time

import jenkins

class ContrlJenlins:


    def __init__(self,url,username,password):
        self.url = url
        self.username = username
        self.password = password
        self.server = jenkins.Jenkins (url=self.url, username=self.username, password=self.password, timeout=50)

    def build_jenkinsJob(self,jobList,param_dict):
        for i in jobList:
            try:
                self.server.build_job (i, parameters=param_dict)
            except:
                print(i+"工程构建失败")

    def get_jenkinsJob_info(self,jobname):
        a = self.server.get_job_info(jobname)
        return a


# origin/fixbug-1.2.1
# origin/release-1.3.0
#,"七巧-前端/console","七巧-前端/official-web","七巧-前端/official-mobile","七巧-前端/m-runtime","七巧-前端/runtime","七巧-前端/operation","七巧-前端/help"

#"七巧-前端/official-web","七巧-前端/official-mobile",

if __name__ == '__main__':
    qianduan_jobList = ["七巧-前端/开发平台-在线编辑器IDE","七巧-前端/console","七巧-前端/m-runtime","七巧-前端/runtime","七巧-前端/operation","七巧-前端/help"]
    houduan_jobList = ["七巧-后端/bpms-workbench",
               "七巧-后端/日志服务","七巧-后端/集成中心","七巧-后端/bpms-repository",
               "七巧-后端/fdn-message","七巧-后端/fdn-authorize","七巧-后端/fdn-storage","七巧-后端/fdn-schema",
               "七巧-后端/bpms-operation", "七巧-后端/bpms-runtime","七巧-后端/bpms-portal",
               "七巧-后端/bpms-appstore","七巧-后端/调度服务"]
    jobList = qianduan_jobList+houduan_jobList
    qajenkins = {'url':'http://jenkins.qa.do1.work','username':'qiqiao','password':'1llR0lbA'}
    uatjenkins = {'url':'http://jenkins.uat.do1.work','username':'do1','password':'7HWoxn8Q'}
    param_dict = {'Branch':'origin/release-1.4.3','PublishVersion':'true'}
    execute_environment = qajenkins
    a = ContrlJenlins(url=execute_environment['url'],username=execute_environment['username'],password=execute_environment['password'])
    a.build_jenkinsJob(jobList,param_dict =param_dict)







