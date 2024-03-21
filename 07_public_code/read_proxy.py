#!/usr/bin/env python
# -*- coding = utf-8 -*-
# @Time       : 2022/12/8 10:57
# @Author     : fany
# @Project    : PyCharm
# @File       : ip_proxies.py
# @description:
import random
data_list = []
file = open('../data/ip_proxies.txt', 'r')
file_data = file.readlines()
for ip in file_data:
    ip_list = ip.split(',')
    print(len(ip_list))
    data_list.append(ip_list)
proxies_dict = random.choice(data_list)
