import datetime
import time

import threadpool


def run_case(f,c):
    '''hhhh'''
    print(f+c)
    time.sleep(2)

def runThread( Threads ):
    '''多线程执行用例'''
    func_var = []
    case_path_List = ["a","b","c","d","e"]  # 用例目录
    testAppNameList = ["A","B","C","D","E"] # app名
    # 生成多个列表
    for c,f in zip(case_path_List,testAppNameList):
        list = [f,c]
        func_var.append((list,None))
    # 定义了一个线程池，最多创建Threads个线程
    pool = threadpool.ThreadPool(Threads)
    # 创建要开启多线程的函数，以及函数相关参数和回调函数，其中回调数可以不写，default是none
    requests = threadpool.makeRequests(run_case,func_var)
    # 将所有要运行多线程的请求扔进线程池
    [pool.putRequest(req) for req in requests]
    pool.wait()



if __name__ == "__main__":
    time1 = datetime.datetime.now()
    start_time = datetime.datetime.strftime(datetime.datetime.now(),'%Y-%m-%d %H:%M:%S')
    runThread(3)
    time.sleep(10)
    time2 = datetime.datetime.now()
    end_time = datetime.datetime.strftime(datetime.datetime.now(),'%Y-%m-%d %H:%M:%S')
    print('开始时间：' + start_time + '    结束时间：' + end_time + "   总耗时：" + str(time2 - time1))




