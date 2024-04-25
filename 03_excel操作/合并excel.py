#!/usr/bin/env python
# -*- coding = utf-8 -*-
# @Time       : 2024/4/12 10:50
# @Author     : fany
# @Project    : PyCharm
# @File       : 合并excel.py
import pandas as pd

# 读取要合并的Excel表格
excel1 = pd.read_excel('file1.xlsx')
excel2 = pd.read_excel('file2.xlsx')

# 合并表格
merged_excel = pd.concat([excel1, excel2], ignore_index=True)

# 将合并后的表格保存到新的Excel文件
merged_excel.to_excel('merged_file.xlsx', index=False)