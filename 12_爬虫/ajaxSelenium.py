#!/usr/bin/env python
# -*- coding = utf-8 -*-
# @Time       : 2023/10/13 15:13
# @Author     : fany
# @Project    : PyCharm
# @File       : ajaxSelenium.py
# @description: ajaxSelenium
from selenium import webdriver

url = 'https://example.com'
driver = webdriver.Chrome()  # You need to have Chrome driver installed

driver.get(url)

# You can now interact with the page using Selenium functions
# For example, you can wait for some elements to load, click buttons, etc.

driver.quit()
