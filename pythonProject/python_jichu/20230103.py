from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.remote import switch_to

# driver = webdriver.Chrome()
# url = 'https://www.csdn.net/'
# driver.get(url)
# driver.maximize_window()
# time.sleep(5)
# driver.quit()

browser = webdriver.Chrome()
browser.get('https://www.csdn.net/')
browser.maximize_window()

browser.find_element(By.ID, "toolbar-search-input").send_keys("python")
browser.find_element(By.ID, "toolbar-search-button").click()
browser.find_element(By.NAME, "tj_trnews")
browser.find_element(By.CSS_SELECTOR, "btn-del-query")

browser.find_element(By.XPATH, '//*[@id="csdn-toolbar"]/div/div/div[3]/div/div[3]/a').click()

# 在所有
# time.sleep(3)
# browser.find_element(By.XPATH, '//*[@id="toolbar-search-input"]').send_keys("人工智能")
# time.sleep(1)
# browser.find_element(By.XPATH, '//*[@id="toolbar-search-input"]').clear()
# browser.find_element(By.XPATH, '//*[@id="toolbar-search-input"]').send_keys("数据结构")
# time.sleep(1)
# browser.find_element(By.XPATH, '//*[@id="toolbar-search-button"]').click()
# time.sleep(3)
# browser.find_element(By.CLASS_NAME, 'toolbar-main').click()
# browser.quit()

# def open_browser(host=public_devices.host, ui=public_devices.ui_type):
#     browser.get(host)

browser = webdriver.Chrome()
time.sleep(2)
browser.get("http://www.csdn.net")
browser.maximize_window()
browser.find_element(By.XPATH, '//*[@id="toolbar-search-input"]').send_keys('数据结构')
browser.find_element(By.XPATH, '//*[@id="toolbar-search-button"]').click()
# browser.find_element(By.CSS_SELECTOR, '#toolbar-search-button').click()
time.sleep(3)

#
# now_handle = browser.current_window_handle
# handles = browser.window_handles
# print(handles)
# for handle in handles:
#     if handle != browser.current_window_handle:
#         print('switch to second window', handle)
#         browser.switch_to.window(handle)
# browser.switch_to.window(now_handle)
handles = browser.window_handles
browser.switch_to.window(handles[1])

browser.find_element(By.XPATH, '//*[@id="keyword"]').clear()
time.sleep(1)
browser.find_element(By.XPATH, '//*[@id="keyword"]').send_keys('python')
browser.find_element(By.XPATH, '//*[@id="search"]').click()
# browser.find_element_by_xpath('//*[@id="search"]').click()

# text = browser.find_element(By.XPATH, '//*[@id="toolbar-search-input"]').text
# print(text)
# text = browser.find_element(By.XPATH, '#toolbar-search-button').get_attribute("type")
time.sleep(5)
browser.quit()


# def isElementExit(element_type, element_value):
#     flag = True
#     by = whichType(element_type)
#     try:
#         browser.find_element(by, element_value)
#         return flag
#     except:
#         flag = False
#         return flag




# def exist(func):
#     def wrapper(*args, **kwargs):
#         # WebDriverWait(browser, 30)
#         # if browser.find_element(By.XPATH, element_value).is_displayed():
#         # element.type = func.element_type
#         # element.value = func.element_value
#         keys = inspect.signature(func).parameters
#         element_value = list(keys)[0]
#         # print(args)
#         # print(args[0])
#         # print(element_value)
#         # flag = isElementExit(element_type, element_value)
#         # for x in alltype:
#         #     if element_type == 'ID':
#         print(args[0])
#         print(element_value)
#         try:
#             WebDriverWait(browser, 10, 0.5).until(EC.presence_of_element_located(element_value))
#             return func(*args, **kwargs)
#         except NoSuchElementException as e:
#             print("{}".format(e))
#         # return func(*args, **kwargs)
#
#     return wrapper
