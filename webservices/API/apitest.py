import requests
from bs4 import BeautifulSoup


def main():
    resp = requests.get('http://www.cbr.ru/scripts/XML_daily.asp')
    soup = BeautifulSoup(resp.content, 'xml')
    # print(soup.prettify())
    print(soup.find('CharCode', text='EUR').find_next_sibling('Value').string)
    # much easier
    print(soup.find(ID='R01239').Value.string)


if __name__ == '__main__':
    main()
