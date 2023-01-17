import os
import time
from enum import unique
from datetime import datetime


# print([x * x for x in range(1, 11)])
#
# print([x * x for x in range(1, 10) if x % 2 == 0])
#
# print([m + n for m in 'ABC' for n in '123'])
#
# print([s for s in os.listdir('.')])
#
# d = {'x': '1', 'y': '2', 'z': '3'}
# print([k + '=' + v for k, v in d.items()])
# print([x if x % 2 == 0 else -x for x in range(1, 11)])

# L1 = ['Hello', 'World', 18, 'Apple', None]
# L2 = [s.lower() for s in L1 if isinstance(s, str)]
# print(L2)
# if L2 == ['hello', 'world', 'apple']:
#     print('通过')
# else:
#     print('不通过')

# L = [x * x for x in range(1, 11)]
# print(L)
# g = (x * x for x in range(1, 11))
# print(g)
# for i in g:
#     print(i)

def fib0(num):
    a = 0
    b = 1
    for i in range(num):
        print(a, end='\t')
        a, b = b, a + b



def fib(num):
    a = 0
    b = 1
    for i in range(num):
        yield a
        a, b = b, a + b
    print(a)



# 普通循环
print(fib0(6))

# 使用yield，fib成为generator
for n in fib(6):
    pass
    # print(n, end='\t')


# return的值在StopIteration中
# g = fib(6)
# while True:
#     try:
#         x = next(g)
#         print('g: ', x, end='\t')
#     except StopIteration as e:
#         print('Generator return value: ', e.value)
#         break
#
#
def index(x, y):
    time.sleep(3)
    print('index %s %s' % (x, y))


index(111, 222)


def home(name):
    time.sleep(3)
    print('welcome %s to home page' % name)


# 添加统计运行时间,改变了源代码
def index1(x, y):
    start = time.time()
    time.sleep(3)
    print('index %s %s' % (x, y))
    end = time.time()
    print(end - start)
#
#
# index1(111, 222)


# 函数调用方式改变
def wrapper2():
    start = time.time()
    index(111, 222)
    end = time.time()
    print(end - start)
#
#
# wrapper2()


# 将index参数写活
def wrapper3(*args, **kwargs):
    start = time.time()
    index(*args, **kwargs)
    end = time.time()
    print(end - start)


wrapper3(12345, 0000, 9999)
wrapper3(x=000, y=111)


# 装饰对象写活，不止能装饰index
def timmer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        res = func(*args, **kwargs)
        end = time.time()
        print(end - start)
        return res

    return wrapper


home = timmer(home)
res = home('egon')
print('返回值--》', res)

# 杨辉三角
# def triangles(n):
#     if n <= 0:
#         return None
#     L = [[1]]
#     for i in range(2, n):
#         yield L
#
#
#     print(L)
#     return L
#
# triangles(5)

# n = 0
# results = []
# for t in triangles(n):
#     results.append(t)
#     n += 1
#     if n == 10:
#         break
#
# for t in results:
#     print(t)
#
# if results == [
#     [1],
#     [1, 1],
#     [1, 2, 1],
#     [1, 3, 3, 1],
#     [1, 4, 6, 4, 1],
#     [1, 5, 10, 10, 5, 1],
#     [1, 6, 15, 20, 15, 6, 1],
#     [1, 7, 21, 35, 35, 21, 7, 1],
#     [1, 8, 28, 56, 70, 56, 28, 8, 1],
#     [1, 9, 36, 84, 126, 126, 84, 36, 9, 1]
# ]:
#     print('通过')
# else:
#     print('不通过')

# now = datetime.now()
# print(now)
# print(type(now))
#
# dt = datetime(2022, 12, 30, 15, 42)
# print(dt)
# print(dt.timestamp())
# t = 1429417200.0
# print(datetime.fromtimestamp(t))
# print(datetime.utcfromtimestamp(t))

# cday = datetime.strptime('2022-11-15 11:15', '%Y-%m-%d %H:%M')
# print(cday)
# print(cday.timestamp())


