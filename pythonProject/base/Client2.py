# -*- coding:UTF-8 -*-

# author:tomoe
# contact: test@test.com
# datetime:2023/1/29 15:16
# software: PyCharm

"""
文件说明：
    
"""
import sys
import socket

from loggers import log


def client2():
    log.info("客户端启动")
    c = socket.socket()
    port = 18080
    host = socket.gethostname()
    c.connect((host, port))
    # log.info(c.getpeername())
    while True:
        log.info("客户端发送：")
        a = input()
        if a == 'quit':
            c.close()
            sys.exit(0)
        else:

            c.send(a.encode('utf-8'))
            data = c.recv(1024)
            log.info("客户端收到：{}".format(data))


if __name__ == '__main__':
    client2()


