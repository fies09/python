'''
需要从两个不同的API获取数据并合并返回给前端。我们可以通过异步处理和合并数据来优化响应时间
'''
import asyncio
import aiohttp
from aiohttp import ClientSession


async def fetch_data(url):
    async with ClientSession() as session:
        async with session.get(url) as response:
            data = await response.json()
            return data

async def handle_request():
    url1 = 'https://api1.example.com/data'
    url2 = 'https://api2.example.com/data'

    tasks = [fetch_data(url1), fetch_data(url2)]
    results = await asyncio.gather(*tasks)

    # 合并来自两个api的数据
    merged_data = {
        'data_from_api1': results[0],
        'data_from_api2': results[1]
    }

    return merged_data


async def main():
    merged_data = await handle_request()
    return merged_data


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    result = loop.run_until_complete(main())
    print(result)
