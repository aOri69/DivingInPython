import asyncio


# def run_server(host, port):
#     loop = asyncio.get_event_loop()
#     coro = loop.create_server(ClientServerProtocol, host, port)
#     server = loop.run_until_complete(coro)
#     try:
#         loop.run_forever()
#     except KeyboardInterrupt:
#         pass
#
#     server.close()
#     loop.run_until_complete(server.wait_closed())
#     loop.close()
#
#
# class ClientServerProtocol(asyncio.Protocol):
#
#     def __init__(self):
#         self.transport = None
#         self._database = {}
#
#     def data_received(self, data):
#         # super().data_received(data)
#         resp = self.__process_data(data.decode())
#         self.transport.write(resp.encode())
#
#     def connection_made(self, transport):
#         # super().connection_made(transport)
#         self.transport = transport
#
#     def __process_data(self, data: str) -> str:
#         resp = ''
#         try:
#             operation, key, value, timestamp = data.split()
#         except ValueError:
#             operation, key = data.split()
#             value, timestamp = None, None
#
#         if operation == 'put':
#             self.__put(key, value, timestamp)
#             return 'ok\n\n'
#         elif operation == 'get':
#             resp_dict = self.__get(key)
#             print(resp_dict)
#             for key,values in resp_dict.items():
#                 resp.join()
#
#     def __put(self, key, value, timestamp):
#         if key not in self._database:
#             self._database[key] = [(int(timestamp), float(value))]
#         else:
#             self._database[key].append((int(timestamp), float(value)))
#
#     def __get(self, key):
#         if key == '*':
#             return self._database
#         return {key: self._database[key]}
from collections import defaultdict


def run_server(host, port):
    loop = asyncio.get_event_loop()
    coro = loop.create_server(
        ClientServerProtocol,
        host, port)

    server = loop.run_until_complete(coro)

    try:
        loop.run_forever()
    except KeyboardInterrupt:
        pass

    server.close()
    loop.run_until_complete(server.wait_closed())
    loop.close()


class ClientServerProtocol(asyncio.Protocol):
    storage = defaultdict(list)

    def __init__(self):
        super().__init__()

    def connection_made(self, transport):
        self.transport = transport

    def data_received(self, data):
        resp = self.process_data(data.decode())
        self.transport.write(resp.encode())

    def process_data(self, data):
        data_splitted = data.split()
        command = data_splitted[0]
        ret = ''
        if command not in ('get', 'put'):
            ret = 'error\nwrong command\n\n'
        else:
            ret = 'ok\n'

        if command == 'get':
            if len(data_splitted) > 1:
                key = data_splitted[1]
                ret += self.get(key)
        elif command == 'put':
            metric = data_splitted[1:]
            self.put(metric)
            ret += '\n'

        return ret

    def get(self, key):
        ret = ''
        if key == '*':
            for k, values in ClientServerProtocol.storage.items():
                for v1, v2 in values:
                    ret += '{} {} {}\n'.format(k, v1, v2)
            ret += '\n'

        else:
            retl = [' '.join([key, v1, v2]) + '\n' for (v1, v2) in ClientServerProtocol.storage[key]]
            ret = ''.join(retl) + '\n'
        return ret

    def put(self, metric):
        k, v1, v2 = metric
        ClientServerProtocol.storage[k].append((v1, v2))


if __name__ == '__main__':
    run_server('127.0.0.1', 8181)
