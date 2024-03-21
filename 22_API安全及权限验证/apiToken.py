#!/usr/bin/env python
# -*- coding = utf-8 -*-
# API密钥
from flask import Flask, request

app = Flask(__name__)
api_key = 'your_api_key_here'

@app.route('/')
def protected_route():
    if 'api_key' not in request.args or request.args['api_key'] != api_key:
        return "Invalid API key. Access denied.", 403
    return "This is a protected route!"

if __name__ == '__main__':
    app.run()
