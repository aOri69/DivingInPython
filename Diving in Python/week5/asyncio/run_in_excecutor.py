"""Запуск синхронной функции в потоке с asyncio"""
import asyncio
from urllib.request import urlopen


# A syncronious function
def sync_get_url(url):
    return urlopen(url).read()


async def load_url(url, loop=None):
    future = loop.run_in_executor(None, sync_get_url, url)
    response = await future
    print(len(response))


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(load_url("https://google.com", loop=loop))
