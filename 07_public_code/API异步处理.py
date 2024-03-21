#!/usr/bin/env python
# -*- coding = utf-8 -*-
'''
在上述示例中，long_running_task函数模拟了一个长时间运行的任务，每秒更新一次进度。start_task接口触发了异步任务的执行。
前端可以通过轮询或长连接等方式获取任务的进度信息并更新UI。根据具体情况，可以选择合适的方法来实现异步处理和进度反馈。
'''
import time
import threading
from flask import Flask, jsonify

app = Flask(__name__)

# 模拟长时间运行的任务
def long_running_task():
    for i in range(1, 11):
        time.sleep(1)  # 模拟任务执行1秒
        progress = i * 10  # 进度
        print(f"Task progress: {progress}%")

# API接口，触发异步任务并反馈进度
@app.route('/start_task', methods=['GET'])
def start_task():
    # 使用线程执行长时间任务
    threading.Thread(target=long_running_task).start()
    return jsonify({'message': 'Task started!'})

if __name__ == '__main__':
    app.run()
