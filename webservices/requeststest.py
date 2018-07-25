import requests
import json

URLLIB = 'http://httpbin.org/'

if __name__ == '__main__':
    r = requests.get(URLLIB + 'get')
    print(r.text)
    r = requests.post(URLLIB + 'post')
    print(r.text)
    #     Passing parameters
    payload = {'key1': 'value1', 'key2': 'value2'}
    r = requests.get(URLLIB + 'get', params=payload)
    print(r.text)

    r = requests.put(URLLIB + 'put', data={'key': 'value'})
    print(r.text)

    r = requests.post(URLLIB + 'post', data=json.dumps({'key': 'value'}))
    print(r.text)
    r = requests.post(URLLIB + 'post', json={'key': 'value'})
    print(r.text)

    # Post a multipart encoded file
    files = {'file':
                 ('test.txt',
                  open('testfile.txt', 'rb'))}
    r = requests.post(URLLIB + 'post', files=files)
    print(r.text)
    #     Passing headers
    headers = {'uesr-agent': 'my-app/0.0.1'}
    r = requests.get(URLLIB + 'get', headers=headers)
    print(r.text)
    #     Response content
    r = requests.get(URLLIB + 'get')
    print(type(r.text), r.text)
    print(type(r.content), r.content)
    print(type(r.json()), r.json())

    print(r.status_code)
    print(r.status_code == requests.codes.ok)
    print(r.headers)

    #     Cookies
    url = 'http://httpbin.org/cookies'
    cookies = dict(cookies_are='working')
    r = requests.get(url, cookies=cookies)
    print(r.text)

    #     Sessions
    s = requests.Session()
    s.get('http://httpbin.org/cookies/set/sessioncookie/123456789')
    r = s.get('http://httpbin.org/cookies')
    print(s.cookies)
    print(r.text)

    #     Headers
    s = requests.Session()
    s.headers.update({'x-test': 'true'})
    r = s.get('http://httpbin.org/headers', headers={'x-test2': 'false'})
    print(r.text)
