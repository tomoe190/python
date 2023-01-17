import json
from urllib import request, parse
from http import cookiejar
import requests
import urllib3


# r = requests.get('http://192.168.1.1')
# print("响应对象的类型:", type(r))
# print("状态码:", r.status_code)
# print("编码格式:", r.encoding)
# print("cookie信息:", r.cookies)
# print('响应的内容:', r.text)
# print('响应内容的类型:', type(r.text))


# response = requests.head('http://192.168.1.1')
# response.encoding = 'utf-8'
# print(response.headers)
# print(response.text)
# r4 = requests.get('http://192.168.1.1')
# print(r4.cookies)
# for key, value in r4.cookies.items():
#         print(key+'='+value)


# r = requests.get('http://192.168.1.1/admin/login.asp')
# print(r.text)


# sess = requests.session()
# body = {
#     'username': ' admin',
#     'password': 'admin',
# }
# body1 = {
#         'band': '2',
#         'mode': '0',
#         'ssid': 'Tenda-D41065222222',
#         'chanwid': '3',
#         'chan': '4',
#         'txpower': '4',
#         'wl_limitstanum': '0',
#         'wl_stanum': '',
#         'regdomain_demo': '1',
#         'submit-url': '/admin/wlbasic.asp',
#         'save': 'Apply Changes',
#         'basicrates': '15',
#         'operrates': '4095',
#         'wlan_idx': '0',
#         'Band2G5GSupport': '1',
#         'wlanBand2G5GSelect': '',
#         'dfs_enable': '0',
#         'postSecurityFlag': '30126',
# }
# headers = {
#         'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
#         'Accept-Encoding': 'gzip, deflate',
#         'Accept-Language': 'zh-CN,zh;q=0.9',
#         'Cache-Control': 'max-age=0',
#         'Connection': 'keep-alive',
#         'Content-Type': 'application/x-www-form-urlencoded',
#         'Host': '192.168.1.1',
#         'Origin':'http://192.168.1.1',
#         'Referer': 'http://192.168.1.1/wlbasic.asp?v=1673339477000',
#         'Upgrade-Insecure-Requests': '1',
#         'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36',
# }
#
# url_login = 'http://192.168.1.1/boaform/admin/formLogin'
# url_change_mode = 'http://192.168.1.1/boaform/formWlanSetup'
#
# response_login = requests.post(url=url_login, headers=headers, data=body)
# print("-------------------")
# print(response_login.status_code)
# print(response_login.text)
# response_change = requests.post(url=url_change_mode, headers=headers, data=body1)
# print("=================")
# print(response_change.status_code)
# print(response_change.text)


def logout():
    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'Accept - Encoding': 'gzip, deflate',
        'Accept - Language': 'zh - CN, zh;q = 0.9',
        'Connection': 'keep - alive',
        'Host': '192.168.1.1',
        'Referer': 'http://192.168.1.1/boaform/admin/formLogout',
        'User - Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36'
    }
    return requests.get('http://192.168.1.1/boaform/admin/formLogout', headers=headers)


def login():
    login_url = 'http://192.168.1.1/boaform/admin/formLogin'
    headers = {
        'Host': '192.168.1.1',
        'Origin': 'http://192.168.1.1',
        'Referer': 'http://192.168.1.1/wlbasic.asp?v=1673339477000',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/108.0.0.0 Safari/537.36',
    }
    body = {
        'username': 'admin',
        'password': 'admin'
    }
    try:
        res = requests.post(url=login_url, data=body, headers=headers)
        print(res.status_code, "登录成功")
        cookies = res.cookies.items()
        cookie = ''
        for name, value in cookies:
            cookie += '{0}={1}'.format(name, value)
        return cookie
    except Exception as e:
        print('获取cookie失败：\n{0}'.format(e))


# cookie = login()
# logout()
# print("-----------")
# headers1 = {
#     "cookie": cookie
# }
# res1 = requests.get("http://192.168.1.1/boaform/admin/formLogin", headers1)
# print(res1.status_code)


body = {
    'redirect:http': '//192.168.150.2:8000/workbench',
    'username': 'xiechen',
    'password': '123456'
}
headers = {
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

res = requests.post("http://192.168.150.2:8000/workbench", data=body, headers=headers)
print(res.cookies)



# 创建filecookiejar的实例
filename = 'cookie0111.txt'
cookie = cookiejar.MozillaCookieJar(filename)
# 生成cookie的管理器
cookie_handler = request.HTTPCookieProcessor(cookie)
# 创建http请求管理器
http_handler = request.HTTPHandler()
# 生成https管理器
https_handler = request.HTTPSHandler()
# 创建请求管理器
opener = request.build_opener(http_handler, https_handler, cookie_handler)


def login3():
    mf = requests.session()
    mf.cookies = cookiejar.LWPCookieJar(filename="mfcookies.txt")

    post_url = ""
    post_data = {
        "username": 'admin',
        "password": 'admin',
    }
    headers = {
        'Host': '192.168.1.1',
        'Origin': 'http://192.168.1.1',
        'Referer': 'http://192.168.1.1/wlbasic.asp?v=1673339477000',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/108.0.0.0 Safari/537.36',
    }
    res = mf.post('http://192.168.1.1/boaform/admin/formLogin', data=post_data, headers=headers)
    print(res.status_code)
    # 登录成功之后，将cookie保存在本地文件中
    mf.cookies.save()


def login4():
    mf = requests.session()
    mf.cookies = cookiejar.LWPCookieJar(filename="mfcookies.txt")
    body = {
        'email': 'xiechen_1115',
        'password': 'ssssslth123.',
    }
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/108.0.0.0 Safari/537.36',
    }
    res = mf.post('https://mail.163.com/', data=json.dumps(body), headers=json.dumps(headers))
    cookies = res.cookies.items()
    print(res.status_code)
    # 登录成功之后，将cookie保存在本地文件中
    mf.cookies.save()
