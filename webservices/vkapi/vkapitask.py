import requests
import config


class Error(Exception):
    pass


class VkError(Error):

    def __init__(self, code, msg) -> None:
        self.code = code
        self.msg = msg


class ReqError(Error):

    def __init__(self, code) -> None:
        self.response_code = code


class VkApi:

    def __init__(self, user_id: int) -> None:
        with config.ConfigReader() as reader:
            self.__key = reader.get('VKAPI', 'servicekey')
            self.user_id = user_id

    def user_get(self, fields: list):
        params = {'user_id': self.user_id,
                  'fields': fields}
        try:
            response = self.__get('users.get', params=params)
        except VkError:
            raise
        except ReqError:
            raise
        return response['response'][0]

    def friends_get(self, fields: list):
        params = {'user_id': self.user_id,
                  'fields': ','.join(fields)}
        try:
            response = self.__get('friends.get', params=params)
        except VkError:
            raise
        except ReqError:
            raise
        return response['response']

    def __get(self, method: str, params: dict):
        url = 'https://api.vk.com/method/{}?v=5.80'.format(method)
        params['access_token'] = self.__key
        r = requests.get(url, params=params)
        if not r.status_code == requests.codes.ok:
            raise ReqError(r.status_code)
        j = r.json()
        if 'error' in j:
            raise VkError(j['error']['error_code'], j['error']['error_msg'])
        return j


def CountBdates(id: int):
    import operator
    from collections import Counter
    ages = list()
    vk = VkApi(id)
    js = vk.friends_get(['bdate'])
    for person in js['items']:
        if 'bdate' in person:
            try:
                d, m, y = str(person['bdate']).split(sep='.')
            except ValueError:
                continue
            if y is not None:
                ages.append(2018 - int(y))
    return Counter(ages).most_common()


if __name__ == '__main__':
    d = CountBdates(3496508)  # 105353423
    print(d)
    vk = VkApi(3496508)
    js = vk.user_get(['sex', 'bdate', 'city', 'photo_max_orig'])
    print(js)
    # js = vk.friends_get(['city', 'bdate', 'photo_max_orig'])
    # for person in js['items']:
    #     print(person)
    # # print(js)
