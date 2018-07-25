import asyncio


async def handle_echo(reader, writer):
    """Корутина по получению данных от клиента"""
    data = await reader.read(1024)
    message = data.decode("utf8")
    addr = writer.get_extra_info("peername")
    print("recieved %r from %r" % (message, addr))
    writer.close()


def main():
    loop = asyncio.get_event_loop()
    coro = asyncio.start_server(handle_echo, "127.0.0.1", 10001, loop=loop)
    server = loop.run_until_complete(coro)
    try:
        loop.run_forever()
    except KeyboardInterrupt:
        pass
    server.close()
    loop.run_until_complete(server.wait_closed())
    loop.close()


if __name__ == '__main__':
    main()
