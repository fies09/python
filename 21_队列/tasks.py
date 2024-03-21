#!/usr/bin/env python
# -*- coding = utf-8 -*-
# 启动: celery -A tasks worker --loglevel=info
from celery import Celery

app = Celery('tasks', broker='redis://localhost:6379/0')

@app.task
def long_running_task():
    for i in range(1, 11):
        progress = i * 10  # 进度
        print(f"Task progress: {progress}%")
