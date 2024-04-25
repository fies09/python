#!/usr/bin/env python
# -*- coding = utf-8 -*-
# @Time       : 2023/6/24 23:53
# @Author     : fany
# @Project    : PyCharm
# @File       : 03_对python创建的目录进行授权.py
# @description:
import os, stat
file_path = '10.1/'
# 处理目录权限不足问题
# set the permission bits for read, write and execute for the owner, group and others
permission_bits = stat.S_IRUSR | stat.S_IWUSR | stat.S_IXUSR | stat.S_IRGRP | stat.S_IWGRP | stat.S_IXGRP | stat.S_IROTH
# set the permission bits for the directory
os.chmod(file_path, permission_bits)
