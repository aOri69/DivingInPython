from bs4 import BeautifulSoup
import requests
import json


def get_html(url: str):
    return requests.get(url).text


def get_article(url: str) -> str:
    article_soup = BeautifulSoup(get_html(url), 'lxml')
    tags = article_soup.find_all('div', 'article__item article__item_alignment_left article__item_html')
    tags_p = [p.text for p in [tag for tag in tags]]
    # for tag in tags:
    # for p in tag.children:
    #     ret_str += p.text
    ret_str = ''.join(tags_p)
    return ret_str


if __name__ == '__main__':
    soup = BeautifulSoup(get_html('https://news.mail.ru'), 'lxml')
    # Дебильный способ
    sections = soup.find_all('span', 'hdr__inner')
    for section in sections:
        news = section.find_parents()[4].find_all('span', 'link__text')
        for new in news:
            link = new.find_parent()['href']
    # Питон путь
    articles_list = [
        (section.string,
         [
             {
                 'header': link.string,
                 'link': 'https://news.mail.ru{}'.format(link.find_parent()['href']),
                 'text': get_article('https://news.mail.ru{}'.format(link.find_parent()['href']))
             }
             for link in section.find_parents()[4].find_all('span', 'link__text')
         ]
         ) for section in soup.find_all('span', 'hdr__inner')
    ]
    with open('news.json', 'w', encoding='utf-8') as f:
        json.dump(articles_list, f, sort_keys=False, indent=4, ensure_ascii=False, separators=(',', ': '))
    # print(articles_list)
