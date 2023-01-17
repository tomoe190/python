#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import sys
import time
from selenium import webdriver
from selenium.common.exceptions import TimeoutException, UnexpectedTagNameException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from Devices.devices_info import public_devices, log

test_browser = None


def get_resource_path(path):
    """

    :param path:
    :return:
    """
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, path)
    return os.path.join(os.path.abspath(".."), path)


def open_browser(ui=public_devices.ui_type):
    """
    打开浏览器
    :param host:
    :param ui:
    """
    logs_path = os.path.join(os.path.expanduser("~"), 'Desktop')
    chrome_path = get_resource_path('./Chrome/Chrome/App/Chrome.exe')
    driver_path = get_resource_path('./Scripts/chromedriver.exe')
    # log_path = get_resource_path('Log')
    host = public_devices.host
    global test_browser
    if ui == 'True':
        # 创建一个参数对象，用来控制chrome以无界面模式打开

        options = Options()
        options.binary_location = chrome_path
        test_browser = webdriver.Chrome(executable_path=driver_path,
                                        chrome_options=options)
        test_browser.command_executor._commands["send_command"] = ("POST", '/session/$sessionId/chromium/send_command')
        params = {'cmd': 'Page.setDownloadBehavior',
                  'params': {'behavior': 'allow', 'downloadPath': logs_path}}
        test_browser.execute("send_command", params)
    else:
        # 创建一个参数对象，用来控制chrome以无界面模式打开
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


def execute_script(cmd):
    global test_browser
    result = test_browser.execute_script(cmd)
    return result


def check_element(node_element):
    global test_browser
    try:
        if test_browser.find_element_by_xpath(node_element):
            return True
    except:
        return False
    time.sleep(1)


def click_element_by_xpath(xpath):
    global test_browser
    try:
        element = WebDriverWait(test_browser, 10, 0.5).until(
            EC.presence_of_element_located((By.XPATH, xpath))
        )
        try:
            result = get_text(xpath)
        except:
            pass
        log.info('点击元素 %s ' % result)
        element.click()
    except TimeoutException:
        log.error('没有找到指定的元素！')
        raise Exception('没有找到指定的元素！')
    time.sleep(1)


def click_element_by_id(resource_id):
    global test_browser
    try:
        element = WebDriverWait(test_browser, 10, 0.5).until(
            EC.presence_of_element_located((By.ID, resource_id))
        )
        log.info('点击元素 %s ' % resource_id)
        element.click()
    except TimeoutException:
        log.error('没有找到指定的元素！')
        raise Exception('没有找到指定的元素！')
    time.sleep(1)


def click_element_by_tag_name(tag_name):
    global test_browser
    try:
        element = WebDriverWait(test_browser, 10, 0.5).until(
            EC.presence_of_element_located((By.TAG_NAME, tag_name))
        )
        log.info('点击元素 %s ' % tag_name)
        element.click()
    except TimeoutException:
        log.error('没有找到指定的元素！')
        raise Exception('没有找到指定的元素！')
    time.sleep(1)


def click_element_by_class_name(class_name):
    global test_browser
    try:
        element = WebDriverWait(test_browser, 10, 0.5).until(
            EC.presence_of_element_located((By.CLASS_NAME, class_name))
        )
        log.info('点击元素 %s ' % class_name)
        element.click()
    except TimeoutException:
        log.error('没有找到指定的元素！')
        raise Exception('没有找到指定的元素！')
    time.sleep(1)


def click_element_by_name(name):
    global test_browser
    try:
        element = WebDriverWait(test_browser, 10, 0.5).until(
            EC.presence_of_element_located((By.NAME, name))
        )
        log.info('点击元素 %s ' % name)
        element.click()
    except TimeoutException:
        log.error('没有找到指定的元素！')
        raise Exception('没有找到指定的元素！')
    time.sleep(1)


def click_element_by_css_selector(css_selector):
    global test_browser
    try:
        element = WebDriverWait(test_browser, 10, 0.5).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, css_selector))
        )
        log.info('点击元素 %s ' % css_selector)
        element.click()
    except TimeoutException:
        log.error('没有找到指定的元素！')
        raise Exception('没有找到指定的元素！')
    time.sleep(1)


def click_element_by_link_text(link_text):
    global test_browser
    try:
        element = WebDriverWait(test_browser, 10, 0.5).until(
            EC.presence_of_element_located((By.LINK_TEXT, link_text))
        )
        log.info('点击元素 %s ' % link_text)
        element.click()
    except TimeoutException:
        log.error('没有找到指定的元素！')
        raise Exception('没有找到指定的元素！')
    time.sleep(1)


def click_element_by_partial_link_text(partial_link_text):
    global test_browser
    try:
        element = WebDriverWait(test_browser, 10, 0.5).until(
            EC.presence_of_element_located((By.PARTIAL_LINK_TEXT, partial_link_text))
        )
        log.info('点击元素 %s ' % partial_link_text)
        element.click()
    except TimeoutException:
        log.error('没有找到指定的元素！')
        raise Exception('没有找到指定的元素！')
    time.sleep(1)


def get_element_attribute(element_value, element_type='xpath'):
    """
    :param element_value: 元素
    :param element_type: 元素类型，支持id、xpath、link_text、partial_link_text、name、tag_name、class_name、css_selector
    :param test_browser: 指定浏览器
    :return: 返回元素所有属性
    """
    global test_browser
    if element_type.find('_') > 0:
        test_type = element_type.replace('_', ' ')
    else:
        test_type = element_type
    try:
        element = WebDriverWait(test_browser, 10, 0.5).until(
            EC.presence_of_element_located((test_type, element_value))
        )
        attribute = test_browser.execute_script(
            'var items = {}; for (index = 0; index < arguments[0].attributes.length; ++index) { items[arguments['
            '0].attributes[index]. name] = arguments[0].attributes[index].value }; return items;',
            element)
        return attribute
    except TimeoutException:
        log.error('没有找到指定的元素！')
        raise Exception('没有找到指定的元素！')
    time.sleep(1)


def get_attribute(element_value, element_type='xpath'):
    """
    :param element_value: 元素
    :param element_type: 元素类型，支持id、xpath、link_text、partial_link_text、name、tag_name、class_name、css_selector
    :param test_browser: 指定浏览器
    :return: 返回元素值
    """
    global test_browser
    if element_type.find('_') > 0:
        test_type = element_type.replace('_', ' ')
    else:
        test_type = element_type
    try:
        element = WebDriverWait(test_browser, 10, 0.5).until(
            EC.presence_of_element_located((test_type, element_value))
        )
        attribute = test_browser.find_element_by_xpath(element_value).get_attribute('value')
        log.info('获取到值为:%s' % str(attribute))
        return attribute
    except TimeoutException:
        log.error('没有找到指定的元素！')
        raise Exception('没有找到指定的元素！')
    time.sleep(1)


def get_text(element_value, element_type='xpath'):
    """
    :param element_value: 元素
    :param element_type: 元素类型，支持id、xpath、link_text、partial_link_text、name、tag_name、class_name、css_selector
    :param test_browser: 指定浏览器
    :return: 返回text
    """
    global test_browser
    if element_type.find('_') > 0:
        test_type = element_type.replace('_', ' ')
    else:
        test_type = element_type
    try:
        element = WebDriverWait(test_browser, 10, 0.5).until(
            EC.presence_of_element_located((test_type, element_value))
        )
        attribute = test_browser.find_element_by_xpath(element_value).get_attribute('innerText')
        # log.info('获取到值为:%s' % str(attribute))
        return attribute
    except TimeoutException:
        log.error('没有找到指定的元素！')
        raise Exception('没有找到指定的元素！')
    time.sleep(1)


def refresh():
    """
    :param test_browser: 指定浏览器
    :return:刷新浏览器
    """
    global test_browser
    test_browser.refresh()


def clear_element_text(element_value, element_type='xpath'):
    """
    :param element_value: 元素
    :param element_type: 元素类型，支持id、xpath、link_text、partial_link_text、name、tag_name、class_name、css_selector
    :param test_browser: 指定浏览器
    :return: True or False
    """
    global test_browser
    if element_type.find('_') > 0:
        test_type = element_type.replace('_', ' ')
    else:
        test_type = element_type
    try:
        element = WebDriverWait(test_browser, 10, 0.5).until(
            EC.presence_of_element_located((test_type, element_value))
        )
        element.clear()
        log.info("清除指定元素成功！")
        return True
    except TimeoutException:
        log.error('没有找到指定的元素！')
        raise Exception('没有找到指定的元素！')
    time.sleep(1)


def get_element_select_value(element_value, element_type='xpath'):
    """
    :param element_value: 元素
    :param element_type: 元素类型，支持id、xpath、link_text、partial_link_text、name、tag_name、class_name、css_selector
    :param test_browser: 指定浏览器
    :return: select_value
    """
    global test_browser
    select_value = []
    if element_type.find('_') > 0:
        test_type = element_type.replace('_', ' ')
    else:
        test_type = element_type
    try:
        element = WebDriverWait(test_browser, 10, 0.5).until(
            EC.presence_of_element_located((test_type, element_value))
        )
        try:
            select_element = Select(element)
            for select in select_element.options:
                select_value.append(select.text.encode('utf8', 'ignore'))
        except UnexpectedTagNameException:
            element.click()
            time.sleep(1)
            try:
                # '/html/body/ul'暂时只发现这个xpath代替了下拉列表值
                list_value = test_browser.find_element_by_xpath('/html/body/ul')
                all_value = list_value.find_elements_by_xpath('./*')
                for i in range(len(all_value) - 1):
                    value = all_value[i]
                    val = test_browser.execute_script(
                        'var items = {}; for (index = 0; index < arguments[0].attributes.length; ++index) { items[''arguments[ ''0].attributes[index]. name] = arguments[0].attributes[index].value }; return items;',
                        value)
                    select_value.append(val['value'])
            except:
                log.error('没有找到指定的元素！')
                raise Exception('没有找到指定的元素！')
            element.click()
        return select_value
    except TimeoutException:
        log.error('没有找到指定的元素！')
        raise Exception('没有找到指定的元素！')
    time.sleep(1)


def set_element_select_value(element_value, set_value, element_type='xpath'):
    """
    :param element_value: 元素
    :param set_value: 设置值
    :param element_type: 元素类型，支持id、xpath、link_text、partial_link_text、name、tag_name、class_name、css_selector
    :param test_browser: 指定浏览器
    :return: True or False
    """
    global test_browser
    if element_type.find('_') > 0:
        test_type = element_type.replace('_', ' ')
    else:
        test_type = element_type
    try:
        element = WebDriverWait(test_browser, 10, 0.5).until(
            EC.presence_of_element_located((test_type, element_value))
        )
        try:
            select_element = Select(element)
            select_element.select_by_visible_text(set_value)
            log.info('设置 %s 值为 %s 成功！' % (str(element_value), str(set_value)))
            return True
        except UnexpectedTagNameException:
            element.click()
            time.sleep(1)
            try:
                # '/html/body/ul'暂时只发现这个xpath代替了下拉列表值
                list_value = test_browser.find_element_by_xpath('/html/body/ul')
                all_value = list_value.find_elements_by_xpath('./*')
                for i in range(len(all_value) - 1):
                    value = all_value[i]
                    val = test_browser.execute_script(
                        'var items = {}; for (index = 0; index < arguments[0].attributes.length; ++index) { items[''arguments[ ''0].attributes[index]. name] = arguments[0].attributes[index].value }; return items;',
                        value)
                    if val['value'] == str(set_value):
                        click_element = value
                        click_element.click()
                        log.info('设置 %s 值为 %s 成功！' % (str(element_value), str(set_value)))
                        return True
                    elif i == len(all_value) - 2:
                        log.error('设置值错误，可以先获取控件可以设置的值！！')
                        raise Exception('设置值错误，可以先获取控件可以设置的值！')
            except:
                log.error('没有找到指定的元素！')
                raise Exception('没有找到指定的元素！')
    except TimeoutException:
        log.error('没有找到指定的元素！')
        raise Exception('没有找到指定的元素！')
    time.sleep(1)


def set_element_text(element_value, set_value, element_type='xpath'):
    """
    :param element_value: 元素
    :param set_value: 设置值
    :param element_type: 元素类型，支持id、xpath、link_text、partial_link_text、name、tag_name、class_name、css_selector
    :param test_browser: 指定浏览器
    :return: True or False
    """
    global test_browser
    if element_type.find('_') > 0:
        test_type = element_type.replace('_', ' ')
    else:
        test_type = element_type
    try:
        element = WebDriverWait(test_browser, 10, 0.5).until(
            EC.presence_of_element_located((test_type, element_value))
        )
        element.send_keys(set_value)
        log.info('输入密码成功！')
        return True
    except TimeoutException:
        log.error('没有找到指定的元素！')
        raise Exception('没有找到指定的元素！')
    time.sleep(1)


def switch_to_frame(frame_value, frame_type='xpath'):
    """
    :param frame_value: 元素
    :param frame_type: 元素类型，支持id、xpath、link_text、partial_link_text、name、tag_name、class_name、css_selector
    :param test_browser: 指定浏览器
    :return: True or False
    """
    global test_browser
    if frame_type.find('_') > 0:
        test_type = frame_type.replace('_', ' ')
    else:
        test_type = frame_type
    try:
        element = WebDriverWait(test_browser, 10, 0.5).until(
            EC.presence_of_element_located((test_type, frame_value))
        )
        test_browser.switch_to.frame(element)
        return True
    except TimeoutException:
        log.error('没有找到指定的元素！')
        raise Exception('没有找到指定的元素！')
    time.sleep(1)


def get_switch_status(element_value, element_type='xpath'):
    """
    :param element_value: 元素
    :param element_type: 元素类型，支持id、xpath、link_text、partial_link_text、name、tag_name、class_name、css_selector
    :param test_browser: 指定浏览器
    :return: checked or unchecked
    通过class属性判断，只适合路由产品
    """
    global test_browser
    attribute = get_element_attribute(element_value, element_type)
    switch_status = attribute['class']
    if switch_status == 'switch-item':
        return 'unchecked'
    else:
        return 'checked'
    time.sleep(1)


def browser_close():
    global test_browser
    test_browser.close()
    time.sleep(1)


def browser_screenshot(filename, full_path):
    global test_browser
    if not os.path.exists(full_path):
        os.makedirs(full_path)
    test_browser.save_screenshot(os.path.join(full_path, filename))


def clear_browser():
    global test_browser
    host = public_devices.host
    open_browser()
    test_browser.get('chrome://settings/clearBrowserData')
    time.sleep(1)
    test_browser.find_element_by_xpath('//settings-ui').send_keys(Keys.ENTER)
    time.sleep(20)
    test_browser.get("http://%s" % host)
    time.sleep(2)


def goform_telnet():
    host = public_devices.host
    global test_browser
    url = 'http://%s/goform/telnet' % host
    test_browser.get(url)
    time.sleep(0.5)
    page = test_browser.page_source
    if page.find('load telnetd success') > 0:
        return True
    else:
        return False
