#!/usr/bin/env python
# -*- coding = utf-8 -*-
# @Time       : 2023/8/29 23:26
# @Author     : fany
# @Project    : PyCharm
# @File       : get_chatgptToken.py
# @description: get_chatgptToken
import openai

openai.api_key = "YOUR_API_KEY"

response = openai.Completion.create(
  engine="text-davinci-003",
  prompt="Once upon a time",
  max_tokens=50  # 设置生成回复的最大 token 数量
)

print(response.choices[0].text)
