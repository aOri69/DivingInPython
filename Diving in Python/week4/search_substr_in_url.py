import re
import requests


def main(url, substring):
    code = get_site_code(url)
    matching_substrings = get_matching_substrings(code, substring)
    print(f'{substring} found {len(matching_substrings)} times in {url}')


def get_site_code(url: str):
    if not url.startswith('http'):
        url = 'http://' + url
    return requests.get(url).text


def get_matching_substrings(code, substring):
    return re.findall(substring, code)


if __name__ == '__main__':
    inp = str(input("Enter Url, and substring to find---->  "))
    splited = inp.split()
    main(splited[0], splited[1])
