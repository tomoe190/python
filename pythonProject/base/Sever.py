# -*- coding:UTF-8 -*-

# author:tomoe
# contact: test@test.com
# datetime:2023/1/29 11:09
# software: PyCharm

"""
文件说明：
    
"""
import socket
import threading

from loggers import log

# 绑定本地地址
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # AF_UNIX（本地协议） 或者 AF_INET（产生IPV4）
# AF_UNIX（本地协议） 或者 AF_INET（产生IPV4）
# type 套接字类型可以根据是面向连接的还是非连接分为
# SOCK_STREAM（这个协议是按照顺序的、可靠的、数据完整的基于字节流的连接。这是一个使用最多的socket类型，是用TCP协议来传输的。）
# 或SOCK_DGRAM（这个协议是无连接的，固定长度的连接调用。该协议是不可靠的，使用UDP来进行它的连接。）。
# 返回一个通信套接字，为本机向网络通信的接口。
port = 18080
host = socket.gethostname()
s.bind((host, port))
s.listen(3)
# 回环地址，只有主机上的进程可以连接到服务器，如果你传了空字符串，服务器将接受本机所有可用的 IPv4 地址。
# 建立最多三个连接监听,在拒绝连接之前，操作系统可以挂起的最大连接数量。

while True:
    # (阻塞式)等待连接的到来
    conn, addr = s.accept()
    # conn是新的套接字对象，可以用来接收和发送数据。address是连接客户端的地址。
    log.info("欢迎{}连接".format(addr))
    while True:
        data = conn.recv(1024)
        if not data:
            break
        dt = data.decode('utf-8')
        log.info("服务器收到{}".format(dt))
        log.info("服务器发送：")
        p1 = input()
        if p1 == 'quit':
            conn.close()
            s.close()
        else:
            conn.send(p1.encode('utf-8'))


# def text_recv(conn, addr):
#
#     data = conn.recv(1024)
#     dt = data.decode('utf-8')
#     log.info("服务器收到{}".format(dt))
#
#
# # def text_send():
#
#
# def socket_up():
#     s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#     port = 18080
#     host = socket.gethostname()
#     s.bind((host, port))
#     s.listen(3)
#     while True:
#         conn, addr = s.accept()
#         log.info("欢迎{}连接".format(addr))
#     return conn
#
#
# if __name__ == "__main__":
#     Host = {}
#     conn = socket_up()
#     while True:
#         try:
#             target_info = input('请输入要发送的信息及端口号（逗号隔开）： >\n').split(',')
#             msg = target_info[0]
#             port = target_info[1]
#             conn = Host[port]
#             conn.sendall(msg.encode('utf8'))
#         except Exception as e:
#             log.error(e)





