#!/usr/bin/env python
# -*- coding = utf-8 -*-
# @Time       : 2023/2/12 21:23
# @Author     : fany
# @Project    : PyCharm
# @File       : python对excel的操作.py
# @description:
# # 创建excel
# import openpyxl
# # ====== 创建格式为xlsx的excel文件 ======
# # 创建一个工作簿,若表格已存在，则覆盖
# wb = openpyxl.Workbook()
#
# # 创建一个名为test的sheet
# wb.create_sheet('test')
#
# # 保存文件。注：创建表格会有两个sheet,按顺序名称分别为Sheet和test
# wb.save('test.xlsx')
#
# # 关闭工作薄
# wb.close()
#
# # 读取已有excel文件
# import openpyxl# ====== 打开已有的excel表格 ======
# # 打开一个工作簿
# wb = openpyxl.load_workbook('test.xlsx')
#
# # 选择一个sheet
# # sheet = wb["Sheet1"]     # 通过表名选择
# sheet = wb.worksheets[0]      # 通过索引选择
#
# # 关闭工作薄
# wb.close()
#
# # 对sheet进行读写
# # coding:utf-8
# import openpyxl
#
# # ====== 向sheet写入数据 ======
# # 打开一个工作簿
# wb = openpyxl.load_workbook('test.xlsx')
# # 选择一个sheet
# # sheet = wb["Sheet1"]     # 通过表名选择
# sheet = wb.worksheets[0]      # 通过索引选择
#
# # 获取行数
# row = sheet.max_row
# # 获取列数
# column = sheet.max_column
# print(row, column)
#
# # 写入数据
# sheet.append(["aaa", "bbb", "ccc"])     # 在最后一行写入一行数据，列表中每一个数据表示每列写入的数据
# sheet.append([1, 2, 3, 4])
#
# # 读取数据
# ce = sheet.cell(row=1, column=1)    # 读取第1行，第1列的数据
# print(ce.value)
#
# # 更新数据
# ce.value = "ddd"    # 更新第1行，第1列的数据为 ddd
# sheet.cell(3, 1, '')    # 更新第3行第1列的数据为 空串
#
# # 删除数据
# # 从第2行开始删除，删除1行
# sheet.delete_rows(2, amount=1)
# # 删除第3列
# sheet.delete_cols(3)
#
# # 保存文件
# wb.save('test.xlsx')
# # 关闭工作薄
# wb.close()

# # xlwt只能对xls文件进行写
# import xlwt
#
# # 打开一个工作薄
# filename = './test.xls'
# write_book = xlwt.Workbook(encoding="utf-8")
#
#
# # 新增个表格，若文件已存在，则覆盖
# sheet = write_book.add_sheet('test')
#
# # 写入数据(行号， 列号， 写入值)
# sheet.write(0, 0, 123.456)
# sheet.write(1, 0, 789)
# sheet.write(2, 0, 'hello')
#
# # 保存
# write_book.save(filename)

# xlwt没有直接修改已有 xls 文件的方法。通常的做法是，读取出文件，复制一份数据，对其进行修改，再保存。
import xlrd
from xlutils.copy import copy

# 打开文件
filename = './test.xls'
rb = xlrd.open_workbook(filename)

# 复制
wb = copy(rb)
# 选取表单
s = wb.get_sheet(0)
# 写入数据
s.write(0, 1, 'new data')
# 保存
wb.save(filename)