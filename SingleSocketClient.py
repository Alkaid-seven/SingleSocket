# -*- coding: UTF-8 -*-
#--------------------------------------------------------
#˵����socket��ϰ��Client�ˣ�֧�ֵ��̡߳�
#By Alkaid_Seven   2014.09.07
#

import socket

if __name__ == '__main__':
    #����socket���� sock
    sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    #�趨������IP
    HOST = 'localhost'
    PORT = 8001
    #������ʾ��Ϣ
    mesg = raw_input('Please input your message:(Input \'q\' to quit this socket):\n')
    #���ӷ�����
    sock.connect((HOST,PORT))
    #sock.gethostname()
    print "hostname"
    #������ send()��recv()����
    sock.send(mesg)
    data = sock.recv(1024)
    print 'Client received:',repr(data)
    #�ر�
    sock.close()