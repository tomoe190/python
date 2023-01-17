from collections.abc import Iterable
from multiprocessing import Process, Queue
from multiprocessing import Pool
import os, time, random
import subprocess

# 去掉首尾空格
# def trim(s):
#     length = len(s)
#     if length > 0:
#         i = 0
#         while i < length - 1:
#             if s[i] == ' ':
#                 i += 1
#             else:
#                 break
#         j = length - 1
#         while j >= i:
#             if s[j] == ' ':
#                 j -= 1
#             else:
#                 break
#         return s[i: j + 1]
#     else:
#         return s


# s = '  he  llo '
# print(trim(s))

# if trim('hello  ') != 'hello':
#     print('测试1失败!')
# elif trim('  hello') != 'hello':
#     print('测试失败!')
# elif trim('  hello  ') != 'hello':
#     print('测试失败!')
# elif trim('  hello  world  ') != 'hello  world':
#     print('测试失败!')
# elif trim('') != '':
#     print('测试失败!')
# elif trim('    ') != '':
#     print('测试2失败!')
# else:
#     print('测试成功!')


# 是否可迭代
# a = isinstance('abcd', Iterable)
# print(a)
#
#
# # 用迭代查找一个list中最小和最大值，并返回一个tuple：
# def findMinAndMax(L):
#     length = len(L)
#     if length > 0:
#         maxnum = L[0]
#         minnum = L[0]
#         for i in range(length):
#             if L[i] > maxnum:
#                 maxnum = L[i]
#             elif L[i] < minnum:
#                 minnum = L[i]
#             i += 1
#         print(minnum, maxnum)
#         return (minnum, maxnum)
#     else:
#         return (None, None)
#
#
# if findMinAndMax([]) != (None, None):
#     print('测试1失败!')
# elif findMinAndMax([7]) != (7, 7):
#     print('测试2失败!')
# elif findMinAndMax([7, 1]) != (1, 7):
#     print('测试3失败!')
# elif findMinAndMax([7, 1, 3, 9, 5]) != (1, 9):
#     print('测试4失败!')
# else:
#     print('测试成功!')
#

def run_proc(name):
    print('Run child process %s (%s)...' % (name, os.getpid()))


def long_time_task(name):
    print('Run task %s (%s)...' % (name, os.getpid()))
    start = time.time()
    #   返回当前时间的时间戳
    time.sleep(random.random() * 3)
    end = time.time()
    print('Task %s runs %0.2f seconds.' % (name, end - start))


def process1():
    print('子进程')
    print('当前进程PID: ', os.getpid(), '父进程PID： ', os.getppid())
    time.sleep(200)


def process2():
    print('子进程')
    print('当前进程PID: ', os.getpid(), '父进程PID： ', os.getppid())
    time.sleep(200)


def write(q):
    print('Process to write: %s' % os.getpid())
    for value in ['A', 'B', '1']:
        print('Put %s to queue.' % value)
        q.put(value)
        time.sleep(random.random())


def read(q):
    print('Process to read: %s' % os.getpid())
    while True:
        value = q.get(True)
        print('Get %s from queue.' % value)


if __name__ == '__main__':
    # 进程间通信
    # q = Queue()
    # pw = Process(target=write, args=(q,))
    # pr = Process(target=read, args=(q,))
    #
    # pw.start()
    # pr.start()
    #
    # pw.join()
    # pr.terminate()

    # 进程池批量创建子进程
    print('Parent process %s.' % os.getpid())
    p = Pool(4)     # 默认大小是CPU的核数
    for i in range(5):
        p.apply_async(long_time_task, args=(i,))    # 运行程序和程序的传入参数
    print('Waiting for all subprocesses done...')
    p.close()
    p.join()  # 等待所有子进程执行完毕
    print('All subprocesses done')

    # 启动子进程
    print('Parent process %s.' % os.getpid())
    p = Process(target=run_proc, args=('test',))
    print('Child process will start.')
    p.start()
    p.join()
    print('Child process end.')
