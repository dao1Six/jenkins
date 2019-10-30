class Ren():

    #刷牙
    def shuayazhaungshiqi(func):
        def shuaya(*args,**kw):
            print("我开始刷牙了")
            print("我刷完牙了")
            func(*args,**kw)
        return shuaya


    @shuayazhaungshiqi
    def chifan(self):
        dic = {'A':{'Branch':'origin/release-1.1.5'},'B':{'Branch':'origin/release-1.1.5'}}
        print(type(dic))


if __name__ == '__main__':
    xiaoming = Ren()
    print(type(xiaoming))
    xiaoming.chifan()