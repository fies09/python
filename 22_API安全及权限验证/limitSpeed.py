#!/usr/bin/env python
# -*- coding = utf-8 -*-
# 限制访问速率
from flask import Flask, request, jsonify
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address

app = Flask(__name__)
limiter = Limiter(app, key_func=get_remote_address)

# 设置限制：每分钟最多允许10个请求
limiter.limit("10 per minute")(app)

@app.route('/')
def protected_route():
    return "This is a protected route!"

if __name__ == '__main__':
    app.run()
