#!/usr/bin/env python
# -*- coding = utf-8 -*-
# @Time       : 2023/10/13 15:17
# @Author     : fany
# @Project    : PyCharm
# @File       : jsSelenium.py
# @description: 解析动态生成的内容
from selenium import webdriver
from bs4 import BeautifulSoup

url = 'https://example.com'
driver = webdriver.Chrome()  # You need to have Chrome driver installed

driver.get(url)

# Wait for the page to load completely (you can change the time)
driver.implicitly_wait(10)

# Get the page source and parse with BeautifulSoup
page_source = driver.page_source
soup = BeautifulSoup(page_source, 'html.parser')

# Use BeautifulSoup to navigate and extract data from the webpage
# For example, soup.find() to find specific elements
print('Title:', soup.title.text)

driver.quit()

