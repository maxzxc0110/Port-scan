# -*- coding:utf8 -*-
#!/usr/bin/python
import socket, time,threading,re

"""
关于main函数flag传参

一,扫描指定端口频段传参格式:
1-500，
表示扫描从1到500的端口

二,扫描指定端口传参格式:
'80','8080','3128','443',
表示扫描['80','8080','3128','443']这个端口列表

三,扫描默认端口列表传参格式:
1
表示扫描默认端口列表

四,其他
表示扫描全端口

"""


#扫描函数
def scan(ip,port):
    try:
        s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        result=s.connect_ex((ip,port))
        # print 'running~~~~~~\n'
        if result == 0:
            print ip+":"+str(port)+" 端口开放\n"
        s.close()
    except:
        print '端口扫描异常'

#主函数
def main(ip,flag='1'):
    flag = str(flag);
    #扫描指定端口频段
    if '-' in flag:  
        l =  re.findall(r"\d+\.?\d*",flag)
        start = l[0]
        end = l[1]
        doActionB(start,end)
    #扫描指定端口           
    elif ',' in flag:  
        portList =  re.findall(r"\d+\.?\d*",flag)
        doActionA(portList)
    #扫描默认端口列表
    elif flag == '1':  
        portList = ['21','23','80','8080','3128','8081','9080','1080','443','69','22','25','110','7001','9080','9090','3389','8081','1521','1158','2100','1433','1080']
        doActionA(portList)
    #全端口扫描
    else:  
        portList = getAllPortList()
        for i in portList:
            start = i[0]
            end = i[1]
            doActionB(start,end)


def doActionA(portList):
        threads = []
        for x in portList:
            threads.append(threading.Thread(target=scan,args=(ip,int(x),)))
        try:
            for t in threads:
                 t.start()
        except:
              print 'can\'t start new thread'

        try:
            for t in threads:
                t.join()
        except:
            print 'oops~'

def doActionB(start,end):
    threads = []
    for x in xrange(int(start),int(end)):  
                threads.append(threading.Thread(target=scan,args=(ip,int(x),)))
    try:
        for t in threads:
             t.start()
    except:
        print 'can\'t start new thread'

    try:
        for t in threads:
                    t.join()
    except:
        print 'oops~'


#获取全端口数组        
def getAllPortList():
    l = []
    s = []
    num = 0
    for i in range(0,132):        
        x = num + 500
        if x > 65534:
            x = 65534
        s.append(num)
        s.append(x)
        l.append(s)
        s = []
        num = num + 500
    return l


if __name__=='__main__':
    ip = raw_input("请输入要扫描的ip:\n")
#     ip = '101.200.139.133' //test data
    print "扫描开始:%s"%ip
    start_time=time.time()
    main(ip,'0')
    print '扫描结束，用时：'+str(time.time()-start_time)
