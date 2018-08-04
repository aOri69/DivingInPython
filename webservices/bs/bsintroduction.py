import requests
import re
from bs4 import BeautifulSoup


def req(htm: str):
    groups = re.findall(r'<a [^>]*other-project-link[^>]*href="([^"]*)', htm)
    print(groups)


def bs(htm: str):
    soup = BeautifulSoup(htm, 'lxml')
    print([tag['href'] for tag in soup('a', 'other-project-link')])


if __name__ == '__main__':
    resp = requests.get('https://wikipedia.org/')
    html = resp.text
    req(html)
    bs(html)
