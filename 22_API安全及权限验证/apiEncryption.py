#!/usr/bin/env python
# -*- coding = utf-8 -*-
# API加密, 使用HTTPS来保护API通信
from flask import Flask

app = Flask(__name__)

# 使用HTTPS保护API
@app.route('/')
def protected_route():
    return "This is a protected route over HTTPS!"

if __name__ == '__main__':
    # 配置SSL证书路径和密钥路径
    ssl_context = ('path/to/your_certificate.crt', 'path/to/your_private_key.key')
    app.run(ssl_context=ssl_context)
