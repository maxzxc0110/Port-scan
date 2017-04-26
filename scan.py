# -*- coding:utf8 -*-
#!/usr/bin/python
import socket, time

def scan(ip,port):
    try:
        s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        result=s.connect_ex((ip,port))
        if result == 0:
            print ip+":"+str(port)+" 端口开放"
    except:
        print '端口扫描异常'

def run(ip):
    try:
        print "扫描开始:%s"%ip
        start_time=time.time()
        for i in range(0,65534):
            scan(ip,int(i))
        print '扫描结束，用时：'+str(time.time()-start_time)
    except:
        print 'ip错误'

if __name__=='__main__':
    ip = raw_input("请输入要扫描的ip:\n")
    run(ip)
