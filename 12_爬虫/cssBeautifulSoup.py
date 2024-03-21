#!/usr/bin/env python
# -*- coding = utf-8 -*-
# @Time       : 2023/10/13 15:13
# @Author     : fany
# @Project    : PyCharm
# @File       : cssBeautifulSoup.py
# @description: cssBeautifulSoup
html_content = '<html><body><p>Hello, <span>world!</span></p></body></html>'
soup = BeautifulSoup(html_content, 'html.parser')

span_text = soup.select_one('span').text
print('Span text:', span_text)
