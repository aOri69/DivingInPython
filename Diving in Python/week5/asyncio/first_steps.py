# asyncio Hello World
import asyncio


@asyncio.coroutine
def hello_world():
    """Старый синтаксис"""
    while True:
        print("Hello World")
        yield from asyncio.sleep(1.0)


async def hello_new():
    """Новый синтаксис PEP492 Python3.5"""
    while True:
        print("Hello World!!!")
        await asyncio.sleep(1.0)


def main():
    loop = asyncio.get_event_loop()
    try:
        loop.run_until_complete(hello_new())
    except KeyboardInterrupt:  # Ctrl+C
        pass
    loop.close()


if __name__ == '__main__':
    main()
