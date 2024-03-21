#!/usr/bin/env python
# -*- coding = utf-8 -*-
# @Time       : 2023/6/24 22:59
# @Author     : fany
# @Project    : PyCharm
# @File       : 02_保存数据到json文件中.py
# @description:
import json
data = {}
with open('./startup/json/this_year.json', 'w') as f:
    json.dump(data, f)
# return send_from_directory('./startup/json', f"this_year.json", as_attachment=True)  # 生成的文件返回出去
# return jsonify({"statusCode": 200, "msg": "数据获取成功", "result": data})