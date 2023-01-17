from enum import Enum, unique
from hello import Hello


# print(len('中文'))
#
#
# print(len('中文'.encode('utf8')))
#
# print('%d-%02d' % (3, 1))
# print('%.2f' % 3.1415926)
#
# s1 = 72
# s2 = 85
# r = (s2 - s1) / 72
# print('小明成绩提升的百分点：%.2f' % r)
#
# L = [
#     ['Apple', 'Google', 'Microsoft'],
#     ['Java', 'Python', 'Ruby', 'PHP'],
#     ['Adam', 'Bart', 'Lisa']
# ]
#
# print(L[0][0])
# print(L[1][1])
# print(L[2][2])


class Student(object):
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade
        # self.grades = []
        # for i in range(3):
        #     self.grades.append(self.grade)
        #     self.grade += 1

    def __str__(self):
        # return self.name, self.grade
        # 返回值没有拼接字符串或没有包含在字符串内的话必须使用对象调用__str__方法而且返回的是个元组,否则会报错
        return "%s 的成绩是 %d" % (self.name, self.grade)
        # 返回值拼接过字符串的话可以直接使用print或对象调用__str__方法打印对象得到的是一个字符串


bart = Student("Bart", 60)
bart.name = "Tom"
bart.grade = 100
print(bart)
# 注意这里直接调用的话会触发__str__方法但是返回值必须结合字符串否则会报错
# print(bart.__str__())
# 如果__str__的返回值没有拼接字符串并且直接使用print打印的话会报错，所以只有这样调用才不会报错


Month = Enum('Month', ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',))
for name, member in Month.__members__.items():    # 怎么看有两个参数
    print(name,  '=>', member, ',', member.value)


@unique
class Weekday(Enum):
    Sun = 0
    Mon = 1
    Tue = 2
    Wed = 3
    Thu = 4
    Fri = 5
    Sat = 6


day1 = Weekday.Mon
print(day1)
print(Weekday.Tue)
print(Weekday['Tue'])

print(Weekday.Tue.value)
print(day1 == Weekday.Wed)
print(Weekday(4))


class Gender(Enum):
    Male = 0
    Female = 1


class Student(object):
    def __init__(self, name, gender):
        self.name = name
        self.gender = gender


bart = Student('July', Gender.Male)
if bart.gender == Gender.Male:
    print("测试通过")
else:
    print("测试不通过")


h = Hello()
h.hello()
print(type(Hello))
print(type(h))
# print(type(h.hello))
