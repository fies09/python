#!/usr/bin/env python
# -*- coding = utf-8 -*-
# @Time       : 2023/2/12 21:16
# @Author     : fany
# @Project    : PyCharm
# @File       : 01_文件被多次读取.py
# @description:
import time
class Demo:
    def __init__(self):
        self.excel_info = self.mock_read_excel()
        print("实例化完成")

    def mock_read_excel(self):
        print("读取文件")
        time.sleep(5)
        return "excel数据"

    def mock_use_1(self):
        a = self.excel_info
        return "指标1"

    def mock_use_2(self):
        b = self.excel_info
        return "指标2"

    def mock_use_3(self):
        c = self.excel_info
        return "指标3"


if __name__ == '__main__':
    start_time = time.time()
    demo = Demo()
    demo.mock_use_1()
    demo.mock_use_2()
    demo.mock_use_3()
    print("耗时", time.time() - start_time)