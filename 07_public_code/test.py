#!/usr/bin/env python
# -*- coding = utf-8 -*-
import socket

def check_ip(ip):
    try:
        sock = socket.create_connection((ip, 80), timeout=5)
        print("IP地址可用")
        sock.close()
    except socket.error as e:
        print("无法连接到IP地址:", str(e))

# 要检查的IP地址
ip = "154.12.81.139"

# 调用函数检查IP地址
check_ip(ip)