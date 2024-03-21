#!/usr/bin/env python
# -*- coding = utf-8 -*-
'''
在这个示例中，long_running_task 是一个Celery任务，负责模拟一个长时间运行的任务。在Flask应用中，通过delay() 方法调用Celery任务，
将任务放入Celery任务队列中异步执行。
确保你已经配置好消息队列，这里使用Redis作为消息队列（broker='redis://localhost:6379/0'）。
这样，Flask应用可以通过Celery异步执行任务，任务会被放入任务队列中，Celery worker会负责处理这些任务，从而实现了任务队列的功能。
'''
from flask import Flask, render_template
from tasks import long_running_task

app = Flask(__name__)

# 调用Celery任务
@app.route('/start_task')
def start_task():
    long_running_task.delay()
    return 'Task started!'

if __name__ == '__main__':
    app.run()
