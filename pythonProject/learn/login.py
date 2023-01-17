# -*- coding:utf-8 -*-
#!/usr/sbin/python
import requests
from http import cookiejar
import sys
# log_path = 'D:\\pythonProject\\tenda.txt'

UserAgent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36"
header = {
    "Host": "192.168.1.1",
    "Origin": "http://192.168.1.1",
    "Referer": "http://192.168.1.1/admin/login.asp",
    "User-Agent": UserAgent
}
acl_header = {
    "Host": "192.168.1.1",
    "Origin": "http://192.168.1.1",
    "Referer": "http://192.168.1.1/admin/acl.asp",
    "User-Agent": UserAgent
}
login_session = requests.session()
# login_session.cookies = cookielib.LWPCookieJar(filename="tenda_cpe.txt")

# class Logger(object):
#     def __init__(self, filename=log_path, stream=sys.stdout):
#         self.terminal = stream
#         self.log = open(filename, 'a')
#
#     def write(self, message):
#         self.terminal.write(message)
#         self.log.write(message)
# sys.stdout = Logger(stream=sys.stdout)

def login_cpe(name, pwd):
    postUrl = "http://192.168.1.1/boaform/admin/formLogin"
    postData = {
        "username": name,
        "password": pwd,
        "save": "Login",
        "submit-url": "/admin/login.asp",
    }
    responseRes = login_session.post(postUrl, data=postData, headers=header)
    # print "statusCode %s" % responseRes.status_code
    get_result  = responseRes.text.encode('utf-8','ignore')
    if get_result.decode('utf-8','ignore').find("BroadBand Device Webserver") >= 0:
        print("UI登录成功！")
    # login_session.cookies.save()

def setting_5G_channel(test_channel):
    settingUrl = "http://192.168.1.1/boaform/formWlanSetup"
    postData = {
        "band": "75",
        "mode": "0",
        # "ssid": "Tenda-888888",
        "chanwid": "0",
        "chan": test_channel,
        "txpower": "0",
        "wl_limitstanum": "0",
        "wl_stanum":"",
        "regdomain_demo": "1",
        "submit-url": "/admin/wlbasic.asp",
        "save": "Apply Changes",
        "basicrates": "15",
        "operrates": "4095",
        "wlan_idx": "0",
        "Band2G5GSupport": "2",
        "wlanBand2G5GSelect": "0",
        "dfs_enable": "0"
    }
    responseRes = login_session.post(settingUrl, data=postData, headers=header)
    # print "text %s" % responseRes.text
    get_result  = responseRes.text.encode('utf-8','ignore')
    # print(get_result)
    if get_result.find("  OK  ") >= 0:
        print("5G %s 信道设置成功！" % test_channel)

def setting_2G4_channel(test_channel):
    settingUrl = "http://192.168.1.1/boaform/formWlanSetup"
    postData = {
        "band": "10",
        "mode": "0",
        "ssid": "Tenda-999999",
        "chanwid": "0",
        "chan": test_channel,
        "txpower": "0",
        "wl_limitstanum": "0",
        "wl_stanum":"",
        "regdomain_demo": "1",
        "submit-url": "/admin/wlbasic.asp",
        "save": "Apply Changes",
        "basicrates": "15",
        "operrates": "4095",
        "wlan_idx": "1",
        "Band2G5GSupport": "1",
        "wlanBand2G5GSelect": "0",
        "dfs_enable": "0"
    }
    responseRes = login_session.post(settingUrl, data=postData, headers=header)
    # print "text %s" % responseRes.text
    get_result  = responseRes.text.encode('utf-8','ignore')
    if get_result.decode('utf-8','ignore').find("  OK  ") >= 0:
        print("2.4G %s 信道设置成功！" % test_channel)

def logout_cpe():
    logoutUrl = "http://192.168.1.1/boaform/admin/formLogout"
    postData = {
        "save": "Logout",
        "submit-url": "/login.asp",
    }
    responseRes = login_session.post(logoutUrl, data=postData, headers=header)
    get_result = responseRes.text.encode('utf-8', 'ignore')
    if get_result.decode('utf-8','ignore').find("Login") < 0:
        print("退出登录成功！")
def open_telnet():
    telnet_url = "http://192.168.1.1/boaform/admin/formACL"
    postData = {
        "lan_ip": "192.168.1.1",
        "lan_mask": "255.255.255.0",
        "aclcap": "0",
        "enable": "1",
        "interface": "0",
        "aclstartIP": "192.168.1.2",
        "aclendIP": "192.168.1.254",
        "l_telnet": "1",
        "addIP": "Add",
        "submit-url": "/admin/acl.asp"
    }
    responseRes = login_session.post(telnet_url, data=postData, headers=acl_header)
    get_result = responseRes.text.encode('utf-8', 'ignore')
    if get_result.find("192.168") >= 0:
        print("Telnet开启成功！")


if __name__ == "__main__":
#
    # pass
    login_cpe("admin", "admin")
    # open_telnet()
    # setting_5G_channel("36")
    setting_2G4_channel("6")
    logout_cpe()
