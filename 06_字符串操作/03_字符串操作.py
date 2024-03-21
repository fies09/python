#!/usr/bin/env python
# -*- coding = utf-8 -*-
# @Time       : 2023/2/13 00:51
# @Author     : fany
# @Project    : PyCharm
# @File       : 03_字符串操作.py
# @description:
# split分割
# join 拼接
_list = ["a", "b", "c"]

# 以"."拼接列表所有值
_str1 = ".".join(_list)

# 以"/"拼接列表所有值
_str2 = "/".join(_list)
print(_str1, _str2)


# 列表转字典(长度相同)
a = ["a", "b", "c"]
b = [1, 2, 3]

tup = zip(a, b)
print(tup)
d = dict(tup)
print(d)

# json字符串与python类型相互转化
# json.loads将json字符串转换为python类型（反序列化）
# 将json的object类型转换为python的dict类型
import json

# 定义json字符串，注意键值均用双引号，否则在转换成是会报错
json_string = '{"name": "张三", "age": 18}'

# 将json字符串转换为dict
ts_dict = json.loads(json_string)
print(type(json_string), type(ts_dict), ts_dict)

# 需要注意的是，转换的字符串需要符合json字符的规范，比如，键值需用双引号，否则在转换时会抛 Expecting property name 的错误。
# 我们可以使用eval内置函数进行转换
# 定义json字符串，注意键值均用双引号，否则在转换成是会报错
json_string = "{'name': '张三', 'age': 18}"

# 将json字符串转换为dict
ts_dict = eval(json_string)
print(type(json_string), type(ts_dict), ts_dict)

#  json.dumps将dict转换成json字符串（序列化）
import json

# 定义dict类型数据
_dict = {"name": "张三", "age": 18}

# 将dict转换成json。ensure_ascii：不将中文以ascii转换
ts_string = json.dumps(_dict, ensure_ascii=False)
print(type(_dict), type(ts_string), ts_string)