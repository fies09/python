#!/usr/bin/env python
# -*- coding = utf-8 -*-
# @Time       : 2023/6/14 09:34
# @Author     : fany
# @Project    : PyCharm
# @File       : 获取图片的尺寸.py
# @description:
from PIL import Image
import os
# 打开图片
image = Image.open("./pic/input/fan(1).jpg")

# 获取图片大小（文件大小）
file_size = os.path.getsize("./pic/input/fan(1).jpg") // 1024
print("文件大小：", file_size, "字节")

# 获取图片宽度和高度
width, height = image.size
print("宽度：", width, "像素")
print("高度：", height, "像素")

# 获取图片尺寸（宽度和高度的元组）
size = image.size
print("尺寸：", size)