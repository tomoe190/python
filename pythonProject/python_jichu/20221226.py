import random
import sys
from random import *
from sys import *

"""for i in range(1,10):
    for j in range(1,10):
        n = j*i
        print'%d*%d=%d\t' % (j, i, n),
        if i == j:
            break"""

"""for i in range(1, 10):
    for j in range(1, 10):
        n = j * i
        print('%d*%d=%d\t' % (j, i, n),end = ''),
        if i == j:
            break"""

"""print("%s is %d years old" % ("xiaoming", 24))
a = input()
print(a + " is beautiful")"""
# s = []
# b = (1, 2.3, 4, s)
# c = list(b)
# c.append(10086)
# d = tuple(c)
# print(d)
# print(b)
# s.append('dd')
# print(b)

# s = {"a": 1, "b": 2, "c": 3}
#
# for key in s:
#     print("%s:%d" % (key, s[key]))

"""i = 1
while i <= 10:
    if i % 2 == 0:
        print(i)
    else:
        pass
    i += 1
print("over")"""

"""bingo = random.randint(1,200)
print("请输入1-200之间的整数")
while True:
    num = int(input())
    if num == bingo:
        print("恭喜你猜对了！")
        break
    elif (num > bingo):
        print("猜大了")
    elif (num < bingo):
        print("猜小了")"""

"""for i in range(1, 10):
    for j in range(1, i + 1):
        n = j * i
        print('%d*%d=%d' % (j, i, n)),
        if i != j:
            pass
        else:
            break
    print()

for i in range(1, 10):
    for j in range(1, i + 1):
        n = j * i
        sys.stdout.write('%d*%d=%d  ' % (j, i, n))
    sys.stdout.write("\n")"""

"""def add(*args):
    Len = len(args)
    sum = 0
    for i in range(Len):
        sum += args[i]
    return sum


print(add(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))


def add2(a, b):
    print(b)
    print(a)


print(add2(1, 2))"""

"""a = randint(1, 100)
print(a)"""

"""class Log:
    for i in range(3):
        username = input("请输入用户名: ")
        password = input("请输入密码: ")
        if username == "admin" and password == "admin":
            print("登陆成功")
            break
        else:
            print("用户名或密码输入错误")
        i += 1"""

"""try:
    try:
        num_str = "12.13"
        num = int(num_str)
        print(num)
    except(NameError, SyntaxError) as e:
        print("内层捕获：{}".format(e))
    finally:
        print("代码结束")
except Exception as e:
    print("外层捕获：{}".format(e))"""


class MoneyException(Exception):
    def __init__(self, money):
        self.money = int(money)

    def __str__(self):
        print("money", self.money)
        if self.money > 0:
            return "1"
        else:
            return "2"


try:
    money = -1
    if money > 0:
        exc = MoneyException(money)
        print(exc)
    else:
        # print(33333)
        raise MoneyException(money)
except MoneyException as e:
    print("abc", e)
    # print(type(e))
#
# print(2 ** 10)



