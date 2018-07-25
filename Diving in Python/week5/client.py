import socket
import time


class ClientError(Exception):
    def __init__(self, text):
        ClientError.text = text


class Client:
    PUT = 'put'
    GET = 'get'
    OK_PUT = b'ok\n\n'
    GET_START = 'ok'
    GET_END = '\n\n'

    def __init__(self, host: str, port: int, timeout: int = None):
        self.__host = host
        self.__port = port
        self.__timeout = timeout

    def put(self, metric: str, value: float, timestamp=None):
        with socket.create_connection((self.__host, self.__port), self.__timeout) as sock:
            try:
                timestamp = timestamp or int(time.time())
                req = " ".join([self.PUT, metric.strip(), str(value), str(timestamp)]).strip()
                req += '\n'
                sock.sendall(req.encode('utf8'))
                if not sock.recv(1024) == self.OK_PUT:
                    raise ClientError(f"Error sending request {req}")
            except socket.timeout:
                raise ClientError("Timeout Error")
            except socket.error as exc:
                raise ClientError(f"Error in socket: {exc.args}")

    def get(self, req: str) -> dict():
        with socket.create_connection((self.__host, self.__port), self.__timeout) as sock:
            try:
                req = ' '.join([self.GET, req]).strip()
                req += '\n'
                sock.sendall(req.encode('utf8'))
                answer = sock.recv(1024).decode('utf8')
                metric_map = self.__recv_get(answer)
                return metric_map
            except ClientError:
                raise
            except socket.timeout:
                raise ClientError("Timeout Error")
            except socket.error as exc:
                raise ClientError(f"Error in socket: {exc.args}")

    def __recv_get(self, answer: str) -> dict:
        """Checking answer after get request"""
        metric_map = dict()
        if not answer.startswith(self.GET_START) and answer.endswith(self.GET_END):
            raise ClientError("Error in receiving request from server")
        answer_list = answer.splitlines()
        for ans in answer_list[1:len(answer_list)-1]:
            key, value, timestamp = list(ans.split())
            if key not in metric_map:
                metric_map[key] = [(int(timestamp), float(value))]
            else:
                metric_map[key].append((int(timestamp), float(value)))
        print(metric_map)
        return metric_map



if __name__ == '__main__':
    pass
    # try:
    #     client = Client(host='127.0.0.1', port=10000)
    #     # client.put("cpu", 16.5)
    #     client.get('')
    # except ClientError as err:
    #     print(err)
