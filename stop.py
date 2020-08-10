from urllib import parse

import jenkins

qajenkins = {'url': 'http://jenkins.qa.do1.work', 'username': 'qiqiao', 'password': '1llR0lbA'}
uatjenkins = {'url': 'http://jenkins.uat.do1.work', 'username': 'do1', 'password': '7HWoxn8Q'}
prodjenkins = {'url':'http://jenkins.qiqiao-prod.do1.work','username':'qiqiao','password':'6LypDvN2'}



runjenkins = uatjenkins

server = jenkins.Jenkins(url=runjenkins['url'], username=runjenkins['username'],password=runjenkins['password'])

queue_info = server.get_queue_info()
running_builds = server.get_running_builds()



#停队列
for i in queue_info:
    server.cancel_queue(i['id'])
#
#停止构建中的任务
for b in running_builds:
    server.stop_build(parse.unquote(b['url'].split('/')[4] + '/' + b['url'].split('/')[6]),b['number'])





