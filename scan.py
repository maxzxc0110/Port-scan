# -*- coding:utf8 -*-
#!/usr/bin/python
import socket, time,threading

#扫描函数
def scan(ip,port):
    try:
        s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        result=s.connect_ex((ip,port))
        #print 'running~~~~~~\n'
        if result == 0:
            print ip+":"+str(port)+" 端口开放\n"
        s.close()
    except:
        print '端口扫描异常'
        
def main(ip):
    portList = getList()
    for i in portList:
        start = i[0]
        end = i[1]
        threads = []
        for x in xrange(int(start),int(end)):  #开启500个线程
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

#获取端口数组        
def getList():
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
    print "扫描开始:%s"%ip
    start_time=time.time()
    main(ip)
    print '扫描结束，用时：'+str(time.time()-start_time)
