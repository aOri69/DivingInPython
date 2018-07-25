import time


class Test:
    def __init__(self):
        self.transport = None
        self._database = {}

    def process_data(self, data: str) -> str:
        resp = 'ok\n'
        try:
            operation, key, value, timestamp = data.split()
        except ValueError:
            operation, key = data.split()
        if operation == 'put':
            self.__put(key, value, timestamp)
            return 'ok\n\n'
        elif operation == 'get':
            resp_dict = self.__get(key)
            print(resp_dict)
            for key,values in resp_dict.items():
                val = str(' ').join(values)
                resp.join(f' {key} {val}')

    def __put(self, key, value, timestamp):
        if key not in self._database:
            self._database[key] = [(int(timestamp), float(value))]
        else:
            self._database[key].append((int(timestamp), float(value)))

    def __get(self, key):
        if key == '*':
            return self._database
        return {key: self._database[key]}


if __name__ == '__main__':
    test = Test()
    test.process_data(f'put cpu 12.0 {int(time.time())}')
    test.process_data(f'put cpu 13.0 {int(time.time())}')
    test.process_data(f'put cpu 10.6 {int(time.time())}')
    test.process_data(f'put cpu 9.0 {int(time.time())}')
    test.process_data(f'put cpu 90.0 {int(time.time())}')
    test.process_data(f'put ram 12.0 {int(time.time())}')
    test.process_data(f'put ram 13.0 {int(time.time())}')
    test.process_data(f'put ram 10.6 {int(time.time())}')

    test.process_data(f'get cpu')
    test.process_data(f'get *')
