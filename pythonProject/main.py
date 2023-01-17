import time

from selenium import webdriver

from mine import command, public_devices

if __name__ == '__main__':

    public_devices.path = "192.168.1.1"
    browser = command.open_browser0(public_devices)
    command.set_element_text('//*[@id="username"]', 'admin', 'XPATH')
    command.set_element_text('password', 'admin', 'ID')
    command.click_element_by('//*[@id="loginBtn"]', 'XPATH')
    time.sleep(2)
    # command.click_element_by('/html/body/div[2]/div[1]/div[2]/ul/li[2]', 'XPATH')
    # command.click_element_by('//*[@id="nav"]/li[2]', 'XPATH')
    # command.click_element_by('//*[@value="0"]', 'XPATH')
    # command.click_element_by('//*[@name="tcpip"]/div[2]/table/tbody/tr/td/input[0]/text()', 'XPATH')  #
    # command.click_element_by('/html/body/form/div[2]/table/tbody/tr/td/input[1]', 'XPATH')  # 点不到
    # command.click_element_by('//*[@id="header"]/div[2]/ul/li[5]', 'XPATH')
    # command.set_element_text('//*[@name="ltime"]', '86411', 'XPATH')
    # //*[@id="displayDhcpSvr"]/div[1]/table/tbody/tr[5]/td/input





    # /html/body/form/div[2]/table/tbody/tr/th
    # /html/body/form/div[2]/table/tbody/tr/td/input[1]
    # //div[@id="MenuContent"]/a[2]/text()'   获取文本
    # $x('//a[text()="Sign In"]/@href')   获取属性


    # command.click_element_by('//*[@id="nav"]/li[2]/a', 'XPATH')
    # command.get_element_attribute('/html/body/form/div[2]/table/tbody/tr/td/input[1]', 'XPATH')
    # time.sleep(2)
    # command.click_element_by('//*[@id="nav"]/li[3]/a', 'XPATH')
    # command.refresh()
    command.close_browser()

    # clear_element_text('//*[@id="toolbar-search-input"]', 'XPATH')
    # click_element_by('//*[@id="toolbar-search-button"]', 'XPATH')
    # click_element_by('toolbar-search-button', 'ID')
    # switch_to_window(-1)
    # get_text('s-nav', 'CLASS_NAME')
    # click_element_by('//*[@id="csdn-toolbar"]/div/div/div[3]/div/div[1]/a', 'XPATH')
    # switch_to_frame(0)
    # click_element_by('/html/body/div[1]/div/div/div[2]/div[1]/div[1]/div[1]/span[4]', 'XPATH')



