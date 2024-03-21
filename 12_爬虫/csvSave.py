#!/usr/bin/env python
# -*- coding = utf-8 -*-
# @Time       : 2023/10/13 15:13
# @Author     : fany
# @Project    : PyCharm
# @File       : csvSave.py
# @description: csvSave
import csv

data = [{'name': 'Alice', 'age': 30}, {'name': 'Bob', 'age': 25}]

filename = 'data.csv'
fieldnames = ['name', 'age']

with open(filename, 'w', newline='') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()
    for item in data:
        writer.writerow(item)

print('Data saved to', filename)
