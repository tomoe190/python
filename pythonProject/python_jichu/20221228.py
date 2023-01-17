import re


# type创建类
# def fn(self, name='world'):
#     print('Hello,%s' % name)
#
#
# Hello = type('Hello', (object,), dict(hello=fn))
# h = Hello()
# print(h.hello())
#
# print(type(Hello))
# print(type(h))

# metaclass给自定义的MyList增加一个add方法
# class ListMetaclass(type):
#     def __new__(cls, name, bases, attrs):
#         # 当前准备创建的类的对象；类的名称；类继承的父类集合；类的方法集合
#         attrs['add'] = lambda self, value: self.append(value)
#         return type.__new__(cls, name, bases, attrs)
#
#
# class MyList(list, metaclass=ListMetaclass):
#     pass
#
#
# L = MyList()
# L.add(1)
# L.add("aaaa")
# print(L)


# L2 = list()
# print(L2.add(1))


# ORM
# class Field(object):
#     def __init__(self, name, column_type):
#         self.name = name
#         self.column_type = column_type
#
#     def __str__(self):
#         return '<%s:%s>' % (self.__class__.__name__, self.name)  # self.__class__.__name__
#
#
# class IntegerField(Field):
#     def __init__(self, name):
#         super(IntegerField, self).__init__(name, 'bigint')  # bigint
#
#
# class StringField(Field):
#     def __init__(self, name):
#         super(StringField, self).__init__(name, 'varchar(100)')  # varchar
#
#
# class ModelMetaclass(type):
#     def __new__(cls, name, bases, attrs):
#         if name == 'Model':
#             return type.__new__(cls, name, bases, attrs)
#         print('Found model: %s' % name)
#         mappings = dict()
#         for k, v in attrs.items():
#             if isinstance(v, Field):
#                 print('Found mapping: %s ==> %s' % (k, v))
#                 mappings[k] = v
#         for k in mappings.keys():
#             attrs.pop(k)
#         # 如果找到一个Field属性，就把它保存到一个__mappings__的dict中;
#         # 同时从类属性中删除该Field属性，否则，容易造成运行时错误（实例的属性会遮盖类的同名属性）
#         attrs['__mappings__'] = mappings
#         attrs['__table__'] = name
#         return type.__new__(cls, name, bases, attrs)
#
#
# class Model(dict, metaclass=ModelMetaclass):
#     def __init__(self, **kw):
#         super(Model, self).__init__(**kw)
#
#     def __getattr__(self, key):
#         try:
#             return self[key]
#         except KeyError:
#             raise AttributeError(r"'Model' object has no attribute '%s'" % key)
#
#     def __setattr__(self, key, value):
#         self[key] = value
#
#     def save(self):
#         fields = []
#         params = []
#         args = []
#         for k, v in self.__mappings__.items():
#             fields.append(k)
#             params.append('?')
#             args.append(getattr(self, k, None))
#         sql = 'insert into %s (%s) values (%s)' % (self.__table__, ','.join(fields), ','.join(params))
#         print('SQL: %s' % sql)
#         print('ARGS: %s' % str(args))
#
#
# class User(Model):
#     id = IntegerField('id')
#     name = StringField('username')
#     email = StringField('email')
#     password = StringField('password')
#
#
# u = User(id=123456, name='Michael', email='test@orm.org', password='123456')
# u.save()


# print(u.id)
# print(u.name)


# 正则表达式
# s1 = 'ABC\\-001'
# print(s1)
# s2 = r'ABC\-001'
# print(s2)
# s3 = re.match(r'\d{3}\-\d{3,8}$', '010-12345')
# print(s3)
# s4 = re.match(r'\d{3}\-\d{3,8}$', '010 12345')
# print(s4)
#
# test = '010-1234567a'
# if re.match(r'\d{3}\-\d{3,8}$', test):
#     print('ok')
# else:
#     print('failed')
#
# print('a b   cd'.split(' '))
# print(re.split(r'\s+', 'a b   cd'))
# print(re.split(r'[\s\,\;]+', 'a; b,  ;; cd'))
#
# m = re.match(r'^(\d{3})(-)(\d{3,9})$', '110-12345678')
# print(m)
# print(m.group(0))
# print(m.group(1))
# print(m.group(2))
# print(m.group(3))
# m2 = re.match(r'^(\d+)(0*)', '1023000').groups()
# print(m2)
# m3 = re.match(r'^(\d+?)(0*)$', '1023000').groups()
# print(m3)
#
# m4 = re.compile(r'^(\d+?)(0*)-\d{3,9}$')
# print(m4.match('12300000-1234567').groups())
# m5 = re.compile(r'^(\d+?)(0*)-(\d{3,9})$')
# print(m5.match('12300000-1234567').groups())
# print(m5.match('12300000-1234567').group(3))


# def is_valid_email(addr):
#     re.match(r'(\w+?)(@+)(\w+)(.com)$', addr)
#     return True
#
#
# def name_of_email(addr):
#     return re.match(r'(\w+)(\.?)(\w+)\@(\w)(\.com)', addr).group(1)


#                   r'^([\w]+\.*)([\w]+)\@[\w]+\.\w{3}(\.\w{2}|)$'


# result1 = is_valid_email('someone@gmail.com')
# print(result1)
# result2 = is_valid_email('bill.gates@microsoft.com')
# print(result2)
# result3 = is_valid_email('bob#example.com')
# print(result3)
# result4 = is_valid_email('mr-bob@example.com')
# print(result4)
#
# name1 = name_of_email('<Tom Paris> tom@voyager.org')
# print(name1)
# name2 = name_of_email('bob@example.com')
# print(name2)

# s = ['apple']
# a = (1, 2, 'a', 'b', s)
# print(a[4])
# print(a)
# print(id(a[4]))
#
# s.append('banana')
# print(a[4])
# print(a)
# print(id(a[4]))

# L = ['apple', 2, 0.5, 'banana', 'peel', 1]

# r = []
# n = 3
# for i in range(n):
#     r.append(L[i])
# print(r)

# print(L[0:3])
# print(L[:3])
# print(L[1:3])
# print(L[-3:-1])
#
# L2 = list(range(100))
# print(L2)
# print(L2[:10])
# print(L2[-10:])
# print(L2[:10:2])
#
# t1 = (0, 1, 2, 3, 4, 5, 6)
# print(t1[:3])
# print(t1[-5:-2])
# print(t1[:3:2])
#
# s1 = 'ASDFGH'
# print(s1[:3])
# print(s1[-5:-2])
# print(s1[:3:2])
#
# s2 = ' a  b   cd '
# print(s2.strip())






