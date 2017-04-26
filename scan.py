# -*- coding:utf8 -*-
#!/usr/bin/python
import socket, time,threading


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
    threads = []
    for x in xrange(0,1024):
        threads.append(threading.Thread(target=scan,args=(ip,int(x),)))
    
    for t in threads:
        t.start()

    for t in threads:
        t.join()
    

if __name__=='__main__':
    ip = raw_input("请输入要扫描的ip:\n")
    print "扫描开始:%s"%ip
    start_time=time.time()
    main(ip)
    print '扫描结束，用时：'+str(time.time()-start_time)
