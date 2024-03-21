#!/usr/bin/env python
# -*- coding = utf-8 -*-
# @Time       : 2023/2/13 00:54
# @Author     : fany
# @Project    : PyCharm
# @File       : 01_selenium截屏.py
# @description:
'''
selenium截图有两种方式

截取全屏
get_screenshot_as_file(filename)：将截图转化成文件保存到本地，filename为保存的文件路径
get_screenshot_as_base64()：将截图转化成base64
get_screenshot_as_png()：将截图转化成png
截取指定元素
screenshot(filename)：将截图转化成文件保存到本地，filename为保存的文件路径
screenshot_as_base64：将截图转化成base64
screenshot_as_png：将截图转化成png
'''
import time
from selenium import webdriver

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("http://www.baidu.com")
time.sleep(1)

# 截取全屏
driver.get_screenshot_as_file("./test.png")
print(driver.get_screenshot_as_base64())
print(driver.get_screenshot_as_png())

print(' ')

# 截图指定元素
el = driver.find_element_by_id("su")
el.screenshot("./btn.png")
print(el.screenshot_as_base64)
print(el.screenshot_as_png)

driver.quit()