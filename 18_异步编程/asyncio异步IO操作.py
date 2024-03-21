#!/usr/bin/env python
# -*- coding = utf-8 -*-
'''
在这个示例中，fetch_data() 函数模拟了异步IO操作，通过使用await asyncio.sleep() 来模拟IO阻塞。main() 函数创建了一个异步任务列表，每个任务调用 fetch_data() 函数。最后，通过 await asyncio.gather() 等待所有任务完成。
运行这段代码，你会看到它并发执行了多个异步任务，每个任务在等待时间后完成。
'''
import asyncio
async def fetch_data(url):
    print(f"Fetching data from {url}")
    # 模拟延迟(eg:IO绑定操作)
    await asyncio.sleep(2)
    print(f"Data fetched from {url}")
    return f"Data from {url}"

async def main():
    # 要获取的url列表
    urls = ['url1', 'url2', 'url3']

    # 创建一个异步运行的任务列表
    tasks = [asyncio.create_task(fetch_data(url)) for url in urls]

    # 等待所有任务完成
    await asyncio.gather(*tasks)


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())