# -*- coding: UTF-8 -*-
#--------------------------------------------------------
#说明：socket练习，Client端，支持单线程。
#By Alkaid_Seven   2014.09.07
#

import socket

if __name__ == '__main__':
    #创建socket对象 sock
    sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    #设定主机和IP
    HOST = 'localhost'
    PORT = 8001
    #设置提示信息
    mesg = raw_input('Please input your message:(Input \'q\' to quit this socket):\n')
    #链接服务器
    sock.connect((HOST,PORT))
    #sock.gethostname()
    print "hostname"
    #请求处理 send()和recv()方法
    sock.send(mesg)
    data = sock.recv(1024)
    print 'Client received:',repr(data)
    #关闭
    sock.close()