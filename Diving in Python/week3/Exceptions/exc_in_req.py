"""
Работа с собственными исключениями библиотеки requests
"""
import requests
import sys


def main():
    try:
        url = sys.argv[1]
        response = requests.get(url, timeout=30)
        response.raise_for_status()
    except requests.Timeout:
        print("время ожидания истекло ", url)
    except requests.HTTPError as err:
        code = err.response.status_code
        print("ошибка url: {0}, {1}".format(url, code))
    except requests.RequestException:
        print("ошибка скачивания url:", url)
    else:
        print(response.content)


if __name__ == '__main__':
    main()
