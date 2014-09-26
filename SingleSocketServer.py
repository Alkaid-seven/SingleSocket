# -*- coding: UTF-8 -*-
#--------------------------------------------------------
#说明：socket练习，Server端，支持单线程。
#By Alkaid_Seven   2014.09.07
#

import socket

if __name__ == '__main__':
    #创建Socket对象 sock
    sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    #设定主机和IP
    HOST = 'localhost'
    PORT = 8001
    #将sock绑定到定义的地址
    sock.bind((HOST,PORT))
    #监听链接请求
    sock.listen(1)
    while True:
        #接受连接请求
        connection,address = sock.accept()
        print 'Server connected by ',address
        #处理请求，使用recv()方法和send()方法
        data = connection.recv(1024)
        print 'The message received from client is :\n' + data
        if data == 'q':
            print 'Now break...'
            break
        else:
            connection.send(data.upper())
            #break
    #关闭连接（一定要）
    connection.close（）

