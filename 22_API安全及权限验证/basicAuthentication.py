#!/usr/bin/env python
# -*- coding = utf-8 -*-
# 基本身份验证
from flask import Flask, request
from functools import wraps
import base64

app = Flask(__name__)

def check_auth(username, password):
    # 检查用户名和密码是否正确，可以根据实际情况实现验证逻辑
    return username == 'user' and password == 'password'

def authenticate():
    message = {'message': "Authentication required."}
    return (message, 401, {'WWW-Authenticate': 'Basic realm="Login Required"'})

def requires_auth(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        auth = request.authorization
        if not auth or not check_auth(auth.username, auth.password):
            return authenticate()
        return f(*args, **kwargs)
    return decorated

@app.route('/')
@requires_auth
def protected_route():
    return "This is a protected route!"

if __name__ == '__main__':
    app.run()
