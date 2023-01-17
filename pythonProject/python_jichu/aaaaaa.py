# -*- coding:UTF-8 -*-

# author:tomoe
# contact: test@test.com
# datetime:2023/1/12 11:54
# software: PyCharm

"""
文件说明：

"""


import requests
import re
from urllib import request
from http import cookiejar


# def getCookie(url):
#     body = {
#         'redirect': 'http://192.168.150.2:8000/workbench',
#         'username': 'xiechen',
#         'password': '123456'
#     }
#     headers = {
#         'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
#         'Accept-Encoding': 'gzip, deflate',
#         'Accept-Language': 'zh-CN,zh;q=0.9',
#         'Connection': 'keep-alive',
#         'Host': '192.168.150.2:8000',
#         'If-None-Match': 'W/"1871-HTG8aNWZGmIQ35a6amOQi2eeIQk"',
#         'Referer': 'http://192.168.150.2:8000/user/login?redirect=http%3A%2F%2F192.168.150.2%3A8000%2Fworkbench',
#         'Upgrade-Insecure-Requests': '1',
#         'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36'
#     }
#     res = requests.post(url, data=body, headers=headers, verify=False, allow_redirects=False)
#     set_cookie = res.headers['Set-Cookie']
#     array = re.split('[;,]', set_cookie)
#     cookieValue = ''
#     for arr in array:
#         if arr.find('DZSW_SESSIONID') >= 0 or arr.find('bl0gm1HBTB') >= 0:
#             cookieValue += arr + ';'
#
# # getCookie("http://192.168.150.2:8000/workbench")
#
#
#
# if __name__ == '__main__':
#     # 声明一个CookieJar对象实例来保存cookie
#     cookie = cookiejar.CookieJar()
#     # 利用urllib.request库的HTTPCookieProcessor对象来创建cookie处理器,也就CookieHandler
#     handler = request.HTTPCookieProcessor(cookie)
#     # 通过CookieHandler创建opener
#     opener = request.build_opener(handler)
#     # 此处的open方法打开网页
#     response = opener.open("http://192.168.150.2:8000/workbench")
#     # 打印cookie信息
#     for item in cookie:
#         print("----")
#         print('Name = %s' % item.name)
#         print('Value = %s' % item.value)


import requests


class GetToken():
    """获取token"""

    def __init__(self):
        self.url = 'http://192.168.150.2:8000/workbench'
        self.data = {
            'redirect': 'http://192.168.150.2:8000/workbench',
            'username': 'xiechen',
            'password': '123456'
        }
        self.timeout = 10.0
        self.headers = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'Accept-Encoding': 'gzip, deflate',
            'Accept-Language': 'zh-CN,zh;q=0.9',
            'Connection': 'keep-alive',
            'Host': '192.168.150.2:8000',
            'If-None-Match': 'W/"1871-HTG8aNWZGmIQ35a6amOQi2eeIQk"',
            'Referer': 'http://192.168.150.2:8000/user/login?redirect=http%3A%2F%2F192.168.150.2%3A8000%2Fworkbench',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36'
        }

    def loginAdmin(self):
        """登录admin获取cookie"""
        session = requests.session()
        session.post(self.url, json=self.data, headers=self.headers, timeout=float(self.timeout))
        cook = session.cookies
        return cook


# import requests
#
# headers = {
#     'Host': 'accounts.douban.com',
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36',
#     'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
#     'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
#     'Accept-Encoding': 'gzip, deflate, br',
#     'Connection': 'keep-alive'
#            }
# request_url = "https://accounts.douban.com/passport/login"
# res = requests.get(request_url, headers=headers)
#
# status_code = res.status_code
# res_header = res.headers
# res_cookies = res.cookies
# cookie1111 = res.cookies.get_dict()                             # 格式化 字典形式输出
# cookie2222 = requests.utils.dict_from_cookiejar(res_cookies)    # 格式化 字典形式输出
# for cookie in res_cookies:
#     print(cookie.name+"\t"+cookie.value)
#
# print("响应状态码：", status_code)
# print("响应请求请求头：", res_header)
# print("响应cookies：", res_cookies)
# print("格式化cookie1111 :", cookie1111)
# print("格式化cookie2222 :", cookie2222)


# if __name__ == '__main__':
#     gettoken = GetToken()
#     return_json = gettoken.loginAdmin()
#     # print(return_json)
#     print(requests.utils.dict_from_cookiejar(return_json))
#     print(requests.utils.dict_from_cookiejar(return_json)['JSESSIONID'])


from http.cookiejar import CookieJar,LWPCookieJar
from urllib.request import Request,urlopen,HTTPCookieProcessor,build_opener
from urllib.parse import urlencode
import ssl
# ----------------------------------------获取cookie---------------------------
# 生成一个管理cookie的对象
cookie_obj = CookieJar()
# 创建一个支持cookie的对象，对象属于HTTPCookieProcessor
cookie_handler = HTTPCookieProcessor(cookie_obj)
#创建一个opener
opener = build_opener(cookie_handler)
response = opener.open('https://accounts.douban.com/passport/login')
print(response)
#打印cookie
for cookie in cookie_obj:
  print('key:',cookie.name)
  print('value:',cookie.value)


