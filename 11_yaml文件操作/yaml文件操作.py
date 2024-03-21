#!/usr/bin/env python
# -*- coding = utf-8 -*-
# @Time       : 2023/2/12 23:48
# @Author     : fany
# @Project    : PyCharm
# @File       : yaml文件操作.py
# @description:
import yaml

# 将yaml格式数据转换成dict格式, 使用 safe_load 方法转换成dict格式数据
with open("./test.yml") as f:
    msg = f.read()

obj = yaml.safe_load(msg)
print(obj)

# 将dict格式数据转换成yaml格式
import yaml

msg = [{'test': {'id': 'login', 'request': {'url': 'XXX', 'method': 'POST'}}},
       {'test': {'id': 'get_user_info', 'request': {'url': 'XXX', 'method': 'GET'}, 'validate': [{'eq': [['code', 0], ['mail', '33@qq.com']]}]}}]

yaml_msg = yaml.safe_dump(msg)
print(yaml_msg)

# 3个“-”  用于将一个yaml文件分成多段，这样可以将多个文档写在一个文件中。读取多段yaml格式用 safe_load_all()方法，返回值是可迭代对象。
import yaml

with open("./test.yml", encoding="utf-8") as f:
    msg = f.read()

objs = yaml.safe_load_all(msg)
print(objs)
for obj in objs:
    print(obj)
