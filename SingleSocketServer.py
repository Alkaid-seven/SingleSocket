# -*- coding: UTF-8 -*-
#--------------------------------------------------------
#˵����socket��ϰ��Server�ˣ�֧�ֵ��̡߳�
#By Alkaid_Seven   2014.09.07
#

import socket

if __name__ == '__main__':
    #����Socket���� sock
    sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    #�趨������IP
    HOST = 'localhost'
    PORT = 8001
    #��sock�󶨵�����ĵ�ַ
    sock.bind((HOST,PORT))
    #������������
    sock.listen(1)
    while True:
        #������������
        connection,address = sock.accept()
        print 'Server connected by ',address
        #��������ʹ��recv()������send()����
        data = connection.recv(1024)
        print 'The message received from client is :\n' + data
        if data == 'q':
            print 'Now break...'
            break
        else:
            connection.send(data.upper())
            #break
    #�ر����ӣ�һ��Ҫ��
    connection.close����

