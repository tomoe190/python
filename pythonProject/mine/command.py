# -*- coding:UTF-8 -*-

# author:tomoe
# contact: test@test.com
# datetime:2023/1/11 11:31
# software: PyCharm

"""
文件说明：
    selenium操作页面
"""
import inspect
import os
import sys
import time

from selenium.webdriver.common.alert import Alert
from selenium.webdriver.remote import switch_to
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.chrome.options import Options
from mine import public_devices
from loggers import log

browser = None



def whichType(element_type):
    """
    返回输入类型对应的By.XXX
    :param element_type:元素类型，支持id、xpath、link_text、partial_link_text、name、tag_name、class_name、css_selector（传入时大写）
    :return: By.类型
    """
    by = None
    if element_type == 'XPATH':
        by = By.XPATH
    elif element_type == 'ID':
        by = By.ID
    elif element_type == 'NAME':
        by = By.NAME
    elif element_type == 'TAG_NAME':
        by = By.TAG_NAME
    elif element_type == 'CLASS_NAME':
        by = By.CLASS_NAME
    elif element_type == 'CSS_SELECTOR':
        by = By.CSS_SELECTOR
    elif element_type == 'LINK_TEXT':
        by = By.LINK_TEXT
    elif element_type == 'PARTIAL_LINK_TEXT':
        by = By.PARTIAL_LINK_TEXT
    return by



def exist(func):
    """
    装饰器，判断元素是否存在
    :param func:需要判断元素的函数
    :return:函数
    """
    global browser
    def wrapper(*args, **kwargs):
        keys = inspect.signature(func).parameters
        keys_str = str(keys)
        if keys_str.find('element_type') >= 0 and keys_str.find('element_value') >= 0:
            keys_lis = list(keys)
            index_type = keys_lis.index("element_type")
            index_value = keys_lis.index("element_value")
            element_type = whichType(args[index_type])
            element_value = args[index_value]
        try:
            WebDriverWait(browser, 5, 0.5).until(EC.presence_of_element_located((element_type, element_value)))
            return func(*args, **kwargs)
        except TimeoutException as e:
            log.error("timeout")
            raise ElementnotFoundException(element_type, element_value)
    return wrapper


def open_browser0(public_devices):
    """
    打开浏览器------无头模式
    :param public_devices:
    """
    global browser
    ch_options = Options()
    ch_options.add_argument("--headless")  # 为chrome设置无头模式 options=ch_options
    public_devices.driver = webdriver.Chrome()
    log.info("打开浏览器：%s" % public_devices.driver)
    browser = public_devices.driver
    browser.get("http://%s" % public_devices.path)
    log.info("get_url: %s" % public_devices.path)
    browser.maximize_window()
    time.sleep(2)


def open_browser1(ui=public_devices.ui_type):
    """
    打开浏览器
    :param host:
    :param ui:
    """
    logs_path = os.path.join(os.path.expanduser("~"), 'Desktop')
    chrome_path = get_resource_path('.\Chrome\Application\Chrome.exe')
    driver_path = get_resource_path('.\Scripts\chromedriver.exe')
    # log_path = get_resource_path('Log')
    host = public_devices.host
    global test_browser
    if ui == 'True':
        options = Options()
        options.binary_location = chrome_path
        test_browser = webdriver.Chrome(executable_path=driver_path,
                                        )
        test_browser.command_executor._commands["send_command"] = ("POST", '/session/$sessionId/chromium/send_command')
        params = {'cmd': 'Page.setDownloadBehavior',
                  'params': {'behavior': 'allow', 'downloadPath': logs_path}}
        test_browser.execute("send_command", params)
    else:
        options = Options()
        options.add_argument('--headless')
        options.add_argument('--disable-gpu')
        options.binary_location = chrome_path
        test_browser = webdriver.Chrome(executable_path=driver_path,
                                        chrome_options=options)
        test_browser.command_executor._commands["send_command"] = ("POST", '/session/$sessionId/chromium/send_command')
        params = {'cmd': 'Page.setDownloadBehavior',
                  'params': {'behavior': 'allow', 'downloadPath': logs_path}}
        test_browser.execute("send_command", params)
    test_browser.get("http://%s" % host)
    test_browser.maximize_window()
    time.sleep(3)


def get_resource_path(path):
    """
    获取资源路径
    :param path:
    :return:
    """
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, path)
    return os.path.join(os.path.abspath(".."), path)


def close_browser():
    """
    logout，并关闭浏览器
    """
    global browser
    browser.quit()
    log.info("关闭浏览器")

@exist
def logout(element_value, element_type):
    """
    退出登录
    """
    global browser
    alert_prencence()
    res = browser.switch_to.default_content()
    log.info("切换至默认frame")
    click_element_by(element_value, element_type)
    log.info("退出登录")


def execute(cmd):
    """
    执行命令
    :param cmd:
    """
    global browser
    log.info(browser.execute(cmd))


def refresh():
    """
    刷新页面
    """
    global browser
    browser.refresh()
    log.info("刷新页面")
    time.sleep(2)


@exist
def check_element(node_element):
    """
    判断用户是否可见该节点元素
    :param node_element:
    :return:
    """
    if node_element.is_displayed():
        return True
    else:
        return False


def switch_to_frame(frame_value):
    """
    切换fame
    :param frame_value:
    """
    global browser
    browser.switch_to.frame(frame_value)
    log.info("切换frame到：%s" % frame_value)


def switch_to_window(window_value, window_type):
    """
    切换浏览器窗口
    :param window_value:
    :param window_type:
    """
    global browser
    handles = browser.window_handles
    log.info(browser.switch_to.window(handles[window_value]))


@exist
def set_element_text(element_value, set_value, element_type):
    """
    输入框输入
    :param element_value:元素定位
    :param set_value:要设置的值
    :param element_type:元素类型，支持id、xpath、link_text、partial_link_text、name、tag_name、class_name、css_selector
    """
    global browser
    by = whichType(element_type)
    browser.find_element(by, element_value).send_keys(set_value)
    log.info("输入：%s", set_value)
    time.sleep(2)


@exist
def clear_element_text(element_value, element_type='XPATH'):
    """
    清空输入框
    :param element_value:元素定位
    :param element_type:元素类型，支持id、xpath、link_text、partial_link_text、name、tag_name、class_name、css_selector
    """
    global browser
    by = whichType(element_type)
    log.info(browser.find_element(by, element_value).clear())
    # elements = browser.find_elements(by, element_value)
    # element_res = []
    # for element in elements:
    #     element_res.append(element)
    # return element_res
    time.sleep(2)


@exist
def get_text(element_value, element_type):
    """
    获取元素，并打印
    :param element_value:元素定位
    :param element_type:元素类型，支持id、xpath、link_text、partial_link_text、name、tag_name、class_name、css_selector
    """
    global browser
    by = whichType(element_type)
    element = browser.find_elements(by, element_value)
    res = element.__getattribute__('text')
    log.info("获取元素", res)
    return res


@exist
def get_element_attribute(element_value, element_type):
    """
    获取元素属性并返回
    :param element_value:元素定位
    :param element_type:元素类型，支持id、xpath、link_text、partial_link_text、name、tag_name、class_name、css_selector
    :return:
    """
    global browser
    by = whichType(element_type)
    attribute = browser.find_element(by, element_value).get_attribute('value')
    log.info("获取元素属性：%s", attribute)
    return attribute


@exist
def click_element_by(element_value, element_type):
    """
    点击元素
    :param element_value:元素定位
    :param element_type:元素类型，支持id、xpath、link_text、partial_link_text、name、tag_name、class_name、css_selector
    """
    global browser
    by = whichType(element_type)
    log.info("点击元素 %s", element_value)
    browser.find_element(by, element_value).click()
    time.sleep(2)


def alert_prencence():
    result = EC.alert_is_present()(browser)
    if result:
        log.info(result.text)
        result.accept()
    else:
        log.info("未弹出！")


class ElementnotFoundException(Exception):
    """
    自定义异常
    :param
    :return:字符串
    """

    def __init__(self, element_type, element_value):
        self.element_type = element_type
        self.element_value = element_value

    def __str__(self):
        log.error("\n找不到元素: %s" % self.element_value)
        # return "\n找不到元素: %s" % self.element_value


public_devices.path = "192.168.1.1"
open_browser0(public_devices)
set_element_text('//*[@id="username"]', 'admin', 'XPATH')
set_element_text('password', 'admin', 'ID')
click_element_by('//*[@id="loginBtn"]', 'XPATH')
click_element_by('//*[@id="nav"]/li[4]/a', 'XPATH')
switch_to_frame('contentIframe')
click_element_by('/html/body/form/div[1]/table/tbody/tr[1]/th/select/option[3]', 'XPATH')
click_element_by('/html/body/form/div[1]/table/tbody/tr[6]/td/select/option[3]', 'XPATH')
click_element_by('/html/body/form/div[8]/input[3]', 'XPATH')
time.sleep(2)
logout()
close_browser()

