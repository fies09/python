#!/usr/bin/env python
# -*- coding = utf-8 -*-
# @Time       : 2023/8/8 13:50
# @Author     : fany
# @Project    : PyCharm
# @File       : python的mqtt应用.py
# @description:
'''
paho-mqtt是Eclipse Paho项目的Python实现，提供了MQTT客户端库，可以用于连接MQTT代理、发布消息和订阅主题。
mqtt的使用说明
实时数据传输：由于MQTT的低延迟和高效性，它适用于实时数据传输场景，如实时监控、实时控制等。
消息推送：MQTT可以用于向多个订阅者推送消息，如即时通讯应用、新闻订阅等。
'''
import paho.mqtt.client as mqtt

# 定义回调函数，处理连接成功的情况
def on_connect(client, userdata, flags, rc):
    print("Connected with result code " + str(rc))
    client.subscribe("topic/test")  # 订阅主题

# 定义回调函数，处理接收到的消息
def on_message(client, userdata, msg):
    print(msg.topic + " " + str(msg.payload))

# 创建MQTT客户端实例
client = mqtt.Client()

# 设置回调函数
client.on_connect = on_connect
client.on_message = on_message

# 连接MQTT代理
client.connect("broker.example.com", 1883, 60)

# 启动消息循环
client.loop_start()

# 发布消息
client.publish("topic/test", "Hello, MQTT!")

# 等待接收消息，这里使用while循环模拟一个持续运行的应用
while True:
    pass
