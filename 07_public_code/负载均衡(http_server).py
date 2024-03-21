#!/usr/bin/env python
# -*- coding = utf-8 -*-
'''
这个示例中，我们使用Python内置的http.server模块创建了一个简单的HTTP负载均衡器。它随机选择一个后端服务器，并将请求转发给后端服务器。
你可以根据自己的需求修改这个示例来实现更复杂的负载均衡逻辑。
'''
import http.server
import socketserver
import random
import socket
# 后端服务器列表
backend_servers = [('localhost', 8001), ('localhost', 8002)]

# 自定义请求处理类
class CustomRequestHandler(http.server.SimpleHTTPRequestHandler):
    def choose_backend(self):
        return random.choice(backend_servers)

    def do_GET(self):
        # 随机选择一个后端服务器
        backend_server = self.choose_backend()

        # 转发请求到后端服务器
        self.proxy_to(backend_server)

    def proxy_to(self, backend_server):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

        with socketserver.TCPServer(('localhost', 0), http.server.SimpleHTTPRequestHandler) as httpd:
            httpd.wfile.write(f"Proxying request to {backend_server[0]}:{backend_server[1]}".encode())
            httpd.wfile.write(b'\n')

            # 将请求转发到后端服务器
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as backend_socket:
                backend_socket.connect(backend_server)
                backend_socket.sendall(self.raw_requestline + self.headers)

                # 读取后端服务器的响应并返回给客户端
                while True:
                    data = backend_socket.recv(4096)
                    if not data:
                        break
                    httpd.wfile.write(data)

# 启动负载均衡器
with socketserver.TCPServer(('localhost', 8000), CustomRequestHandler) as httpd:
    print('Load balancer started on port 8000')
    httpd.serve_forever()
