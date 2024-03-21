#!/usr/bin/env python
# -*- coding = utf-8 -*-
# @Time       : 2023/10/13 15:16
# @Author     : fany
# @Project    : PyCharm
# @File       : jsHeadless.py
# @description: jsHeadless
from selenium import webdriver

url = 'https://example.com'
driver = webdriver.Chrome()  # You need to have Chrome driver installed

driver.get(url)

# Wait for the page to load completely (you can change the time)
driver.implicitly_wait(10)

# Get the page source
page_source = driver.page_source
print('Page Source:', page_source)

driver.quit()
