#!/usr/bin/env python
# -*- coding = utf-8 -*-
# @Time       : 2022/11/30 16:08
# @Author     : fany
# @Project    : PyCharm
# @File       : 01_代理ip.py
# @description:
from config import headers
# 导入数据请求模块
import requests
# 导入数据解析模块
import parsel
import json
proxies_list = []
anonymity_list = []
agent_list = []
type_list = []
# 发送请求, 根据浏览器对于分析得到的url地址发送请求
# 请求url地址
for i in range(0, 20):
    # choice = input('是否获取下一页(y/n):')
    # print('开始获取第{}页数据...'.format(i+1))
    # if choice.lower() == 'y':
    url = f'https://www.kuaidaili.com/free/inha/{i+1}/'
    # 发送请求 Response 200 响应对象, 请求成功
    print(url)
    response = requests.get(url, headers=headers)
    print(response.status_code)
    '''
       解析数据, 提取我们想要的数据内容
           解析方法: 
            re正则: 对于字符串数据进行提取
            css: 根据标签属性内容提取
            xpath: 根据标签节点提取
       '''
    # 转换数据类型 response.text<字符串数据类型>
    selector = parsel.Selector(response.text)
    '''
      ip代理结构
      proxies_dict = {
          "http": "http://" + ip:端口,
          "https": "http://" + ip:端口,
      }
      '''
    # 获取ip, 端口号,匿名度和类型
    trs = selector.css('#list > table > tbody > tr')
    trs1 = selector.xpath('//*[@id="list"]/table/tbody/tr[1]')
    # print(trs)
    # for循环一个一个提取tr标签
    for tr in trs:
        # 提取ip号, td:nth-child(1)::text 获取第一个td标签里面文件数据
        ip_num = tr.css('td:nth-child(1)::text').get()
        # ip_num_1 = tr.xpath('td[1]/text()').get()
        # print(ip_num)
        # 提取端口号
        ip_port = tr.css('td:nth-child(2)::text').get()
        # 提取匿名度
        anonymity = tr.css('td:nth-child(3)::text').get()
        # 类型
        agent_type = tr.css('td:nth-child(4)::text').get()
        agent_ip = ip_num + ':' + ip_port
        anonymity_list.append(anonymity)
        agent_list.append(agent_ip)
        type_list.append(agent_type)
    res1 = list(zip(agent_list, anonymity_list, type_list))
    # proxies_dict = {}
    for i in res1:
        if list(i)[1] == '高匿名':
            # if list(i)[-1] == 'HTTP':
            #     proxies_dict['http'] = "http://" + list(i)[0]
            # else:
            #     proxies_dict['https'] = "https://" + list(i)[0]
            proxies_dict = {
                'http': 'http://' + list(i)[0],
                'https': 'https://' + list(i)[0]
            }
            print(proxies_dict)
            # 检测代理是否可以, 用代理请求下网站
            try:
                print(proxies_dict)
                response1 = requests.get(url='https://www.baidu.com/', headers = headers, proxies = proxies_dict, timeout = 1)
                print(response1.status_code)
                if response1.status_code == 200:
                    proxies_list.append(proxies_dict)
                    print('代理可以使用', proxies_dict)
                    # 保存代理到文本
                    with open('../data/代理.txt', mode='a', encoding='utf-8') as f:
                        f.write(json.dumps(proxies_dict))
                        f.write(',')
            except:
                print("当前代理:", proxies_dict, "请求超时,检测不合格")
# else:
#     print('已取消下载')
#     break

print('=' * 50)
print("获取到一共:", len(agent_list))
print('可以使用的代理:', len(proxies_list))
print(proxies_list)

