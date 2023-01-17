# -*- coding:UTF-8 -*-

# author:tomoe
# contact: test@test.com
# datetime:2023/1/11 11:31
# software: PyCharm

"""
文件说明：
    通过requests操作页面
"""
import json
import os
import time
from http import cookiejar
from urllib import request
import pickle as pk
import requests
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from loggers import log


def logout():
    """
    退出登录
    :return:
    """
    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,'
                  'application/signed-exchange;v=b3;q=0.9',
        'Accept-Encoding': 'gzip,deflate',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Connection': 'keep-alive',
        'Host': '192.168.1.1',
        'Referer': 'http://192.168.1.1/boaform/admin/formLogout',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/108.0.0.0 Safari/537.36 '
    }
    url_logout = 'http://192.168.1.1/boaform/admin/formLogout'
    res_logout = requests.get(url=url_logout, headers=headers)
    if res_logout.status_code == 200:
        log.info("logout成功！")
    return res_logout


def login_pon():
    """
    登陆设备web页面
    :return:
    """
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
    res = requests.post(url=login_url, data=body, headers=headers)
    if res.status_code == 200:
        log.info("登录成功！")
    return res


login_pon()

mf = requests.session()
mf.cookies = cookiejar.LWPCookieJar(filename="mfcookies.txt")


def get_cookie():
    """
    获取cookie
    :return:
    """
    headers = {
        'Host': 'accounts.douban.com',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
        'Accept-Encoding': 'gzip, deflate, br',
        'Connection': 'keep-alive'
    }
    res = mf.get("https://accounts.douban.com/passport/login", headers=headers)
    cookie1111 = res.cookies.get_dict()  # 格式化 字典形式输出
    # cookie2222 = requests.utils.dict_from_cookiejar(res.cookies)  # 格式化 字典形式输出
    for cookie in res.cookies:
        print(cookie.name + "\t" + cookie.value)
    print("响应状态码：", res.status_code)
    # print("响应cookies：", res.cookies)
    # print("格式化cookie1111 :", cookie1111)
    # print("格式化cookie2222 :", cookie2222)
    mf.cookies.save()
    return mf.cookies
    # 使用


# def cookie_login_pingtai():
#     mf = requests.session()
#     mf.cookies = cookiejar.LWPCookieJar(filename="mfcookies.txt")
#     headers = {
#         'Host': 'accounts.douban.com',
#         'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36',
#         'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
#         'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
#         'Accept-Encoding': 'gzip, deflate, br',
#         'Connection': 'keep-alive'
#     }
#     try:
#         res = mf.get("https://accounts.douban.com/passport/login")
#         if res.status_code == 200:
#             print("登录成功！")
#         print(res.cookies)
#         cookies = res.cookies.items()
#         cookie = ''
#         for name, value in cookies:
#             cookie += '{0}={1}'.format(name, value)
#         mf.cookies.save()
#         print(res.status_code)
#         return res
#     except Exception as e:
#         print('获取cookie失败：\n{0}'.format(e))


def ssid_change(ssid):
    """
    修改WiFi参数
    """
    body = {
        'band': '2',
        'mode': '0',
        'ssid': ssid,
        'chanwid': '3',
        'chan': '4',
        'txpower': '4',
        'wl_limitstanum': '0',
        'wl_stanum': '',
        'regdomain_demo': '1',
        'submit-url': '/admin/wlbasic.asp',
        'save': 'Apply Changes',
        'basicrates': '15',
        'operrates': '4095',
        'wlan_idx': '0',
        'Band2G5GSupport': '1',
        'wlanBand2G5GSelect': '',
        'dfs_enable': '0'
    }
    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,'
                  'application/signed-exchange;v=b3;q=0.9',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Cache-Control': 'max-age=0',
        'Connection': 'keep-alive',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Host': '192.168.1.1',
        'Origin': 'http://192.168.1.1',
        'Referer': 'http://192.168.1.1/wlbasic.asp?v=1673339477000',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/108.0.0.0 Safari/537.36',
    }
    url_change_mode = 'http://192.168.1.1/boaform/formWlanSetup'
    return requests.post(url=url_change_mode, headers=headers, data=body)


def Security_change():
    """
    修改WiFi密码
    """
    body = {
        'wlanDisabled': 'OFF',
        'isNmode': '0',
        'wpaSSID': '0',
        'security_method': '6',
        'auth_type': 'both',
        'wepEnabled': 'ON',
        'length0': '1',
        'format0': '1',
        'key0': '',
        'wpaAuth': 'psk',
        'dotIEEE80211W': '0',
        'sha256': '0',
        'ciphersuite_a': '1',
        'wpa2ciphersuite_a': '1',
        'gk_rekey': '86400',
        'pskFormat': '0',
        'pskValue': 'asdf1234',
        'wapiPskFormat': '0',
        'wapiPskValue': '',
        'wepKeyLen': 'wep64',
        'radiusIP': '0.0.0.0',
        'radiusPort': '1812',
        'radiusPass': ' ',
        'radius2IP': '0.0.0.0',
        'radius2Port': '1812',
        'radius2Pass': ' ',
        'wapiASIP': '0.0.0.0',
        'wlan_idx': '0',
        'submit-url': ' /admin/wlwpa.asp',
        'encodekey0': ' ',
        'encoderadiusPass': ' ',
        'encoderadius2Pass': ' ',
        'save': 'Apply Changes',
    }
    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Cache-Control': 'max-age=0',
        'Connection': 'keep-alive',
        'Content-Length': '547',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Host': '192.168.1.1',
        'Origin': 'http://192.168.1.1',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36'
    }
    url_change_mode = 'http://192.168.1.1/boaform/admin/formWlEncrypt'
    res = requests.post(url=url_change_mode, headers=headers, data=body)
    print(res.status_code)
    return res


# Security_change()
# def import_file(srvUrl, file):
#     try:
#         headers = {
#             'Accept': '*/*',
#             'Accept-Encoding': 'gzip, deflate',
#             'Accept-Language': 'zh-CN,zh;q = 0.9',
#             'Connection': 'keep-alive',
#             'Content-Type': 'multipart/form-data;',
#             'Host': '192.168.150.2:8000',
#             'Origin': 'http://192.168.150.2:8000',
#             'Referer': 'http://192.168.150.2:8000/workbench',
#             'User-Agent': 'Mozilla / 5.0(WindowsNT10.0;Win64;x64) AppleWebKit / 537.36(KHTML, likeGecko) Chrome/108.0.0.0Safari/537.36',
#             'X-Requested-With': 'XMLHttpRequest'
#         }
#         resp = requests.post(url=srvUrl, headers=headers)
#         print(resp)
#         if resp.status_code != requests.codes.ok:
#             return  # error!
#
#         name = os.path.basename(file)
#         with open(file, "rb") as conf:
#             upFile = {
#                 'file': (name, conf)
#             }
#             resp = requests.post(url=srvUrl, files=upFile)
#             print(resp.status_code)
#     except Exception as ex:
#         print(ex)

def import_file(srvUrl, file):
    """
    上传文件
    :param srvUrl: http://192.168.150.2:8000/api/v1.0/tickets/126（126为对应工单ID）
    :param file: 要上传的文件名
    :return:
    """
    try:
        header = {
            'Accept': '*/*',
            'Accept-Encoding': 'gzip, deflate',
            'Accept-Language': 'zh-CN,zh;q=0.9',
            'Connection': 'keep-alive',
            'Content-Type': 'multipart/form-data; boundary=----WebKitFormBoundarynX9ZcZCeJ4MKpx88',
            'Cookie': 'autologin = fe1e222f97cc6e5ac85f0a3c7aa95dea336f0350;sessionid = uknhuh96x1j3yrei6f448cba4b8121vl;csrftoken = mwkXE0fp20xbHFCYSThRZNqvAo4aialXMZfYPLwnA1u3wyjBXV8oRtGSmg06UDq0;jwt = eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE2NzM2MDM2MjAsImlhdCI6MTY3MzUxNzIyMCwiZGF0YSI6eyJpZCI6MzksImxhc3RfbG9naW4iOiIyMDIzLTAxLTEyIDA5OjUyOjIwIiwidXNlcm5hbWUiOiJ4aWVjaGVuIiwiYWxpYXMiOiJcdThjMjJcdTY2NjgiLCJlbWFpbCI6IjgiLCJwaG9uZSI6IjgiLCJpc19hY3RpdmUiOnRydWUsInR5cGVfaWQiOjAsImNyZWF0b3JfaW5mbyI6eyJjcmVhdG9yX2lkIjoxLCJjcmVhdG9yX2FsaWFzIjoiYWRtaW4iLCJjcmVhdG9yX3VzZXJuYW1lIjoiYWRtaW4ifSwiZ210X2NyZWF0ZWQiOiIyMDIyLTEyLTA3IDExOjM2OjI2IiwiZ210X21vZGlmaWVkIjoiMjAyMi0xMi0wNyAxMzo1NjowOCIsImlzX2RlbGV0ZWQiOmZhbHNlfX0.Z2wxwaNB74Do6nkHLd7iZ2QcvOGVB1Qh6FtBvhPfpW0',
            'Host': '192.168.150.2:8000',
            'Origin': 'http://192.168.150.2:8000',
            'Referer': 'http://192.168.150.2:8000/workbench',
            'User-Agent': 'Mozilla / 5.0(WindowsNT10.0;Win64;x64) AppleWebKit / 537.36(KHTML, likeGecko) Chrome/108.0.0.0Safari/537.36',
            'X-Requested-With': 'XMLHttpRequest'
        }
        body = {
            'ModuleFeatureDecomposition': "[{\"url\":\"/media/ticket_file/111/US_HG6V1.0re_v1.1.0_en_TDE01_xpon.tar\",\"file_name\":\"img.tar\"}]",
            'SoftwareOverview': "[{\"url\":\"/media/ticket_file/111/HG6V1.0-TDE01 SVT8测试策略.xlsx\",\"file_name\":\"HG6V1.0-TDE01 SVT8测试策略.xlsx\"}]",
            'transition_id': '4'
        }
        resp = requests.patch(url=srvUrl, headers=header, data=json.dumps(body))
        print(resp.status_code)
        if resp.status_code != requests.codes.ok:
            return "error!"

        name = os.path.basename(file)
        with open(file, "rb") as conf:  # rb mode，读取二进制
            upFile = {
                'file': (name, conf)
            }
            resp = requests.patch(url=srvUrl, files=upFile)
        print(resp.status_code)
    except Exception as ex:
        print(ex)


# sevUrl = 'http://192.168.150.2:8000/api/v1.0/tickets/126'
# file1 = 'HG6V1.0-TDE01 SVT8测试策略.xlsx'
# file2 = 'US_HG6V1.0re_v1.1.0_en_TDE01_xpon.tar'
# import_file(sevUrl, file1)
# import_file(sevUrl, file2)


def export_file(srvUrl, file):
    """
    下载平台文件
    :param srvUrl: http://192.168.150.2:8000/api/v1.0/tickets/126（126为对应工单ID）
    :param file:文件名称。文件与运行脚本目录一致，则直接使用文件名；与脚本目录不一致需要加文件存放路径，可以是一个绝对路径，也可以是运行脚本的相对路径。
    :return:
    """
    try:
        header = {"Content-Type": "application/json;charset=UTF-8"}
        resp = requests.post(url=srvUrl, headers=header)
        print(resp.status_code)
        if resp.status_code != requests.codes.ok:
            return "error!"
        header = resp.headers
        name = header.get("Content-Disposition")  # 假设头中携带文件信息，可获取用于写文件
        print(name)
        with open(file, "wb") as conf:  # wb mode，写入二进制
            conf.write(resp.content)
    except Exception as ex:
        print(ex)

# sevUrl = 'http://192.168.150.2:8000/api/v1.0/tickets/126'
# file = 'HG3V1.1产品开发项目用户场景分析.pptx'
# export_file(sevUrl, file)

import requests

response = requests.get("https://www.csdn.net")
print(response.text)