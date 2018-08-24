from bs4 import BeautifulSoup
import re
import os


class Exists(Exception):
    pass


class Finder:

    def __init__(self, start, end, path) -> None:
        self.start = start
        self.bridge = []
        self.end = end
        self.path = path
        self.files = dict.fromkeys(os.listdir(path))
        self.link_re = re.compile(r"(?<=/wiki/)[\w()]+")
        self.__parsed_pages = set()

    def find_path(self, start) -> list:
        if self.end in self.bridge:
            return self.bridge
        children = self._get_links(start)
        self.bridge.append(start)
        if len(children) == 0:  # and self.end not in self.bridge:
            self.bridge.pop(len(self.bridge) - 1)
            return []
        for child in children:
            self.find_path(child)
        return []

    def _get_links(self, filename) -> list:
        if filename in self.__parsed_pages:
            return []
        with open(f'{self.path}{filename}', encoding='UTF-8') as f:
            children = []
            page = str(BeautifulSoup(f.read(), 'lxml').find('div', {'id': 'bodyContent'}))
            links = self.link_re.findall(page)
            del page
            self.__parsed_pages.add(filename)
            for link in links:
                if link in self.files:
                    if not self.files.get(link) and link != filename:
                        children.append(link)
        return children

    # def get_children(path: str, filename: str, files: dict) -> dict:
    #     with open(f'{path}{filename}', encoding='UTF-8') as f:
    #         link_re = re.compile(r"(?<=/wiki/)[\w()]+")  # Искать ссылки можно как угодно, не обязательно через re
    #         children = {}
    #         page = str(BeautifulSoup(f.read(), 'lxml').find('div', {'id': 'bodyContent'}))
    #         links = link_re.findall(page)
    #         del page
    #         for link in links:
    #             if link in files:
    #                 if not files.get(link) and link != filename:
    #                     children[link] = filename  # Setting parent
    #     return children


# Вспомогательная функция, её наличие не обязательно и не будет проверяться
def build_tree(start, end, path):
    # link_re = re.compile(r"(?<=/wiki/)[\w()]+")  # Искать ссылки можно как угодно, не обязательно через re
    files = dict.fromkeys(os.listdir(path))  # Словарь вида {"filename1": None, "filename2": None, ...}
    # # TODO Проставить всем ключам в files правильного родителя в значение, начиная от start
    # children = get_children(path, start, files)
    # files.update(children)
    # for child in children:
    #     pass
    finder = Finder(start, end, path)
    brid = finder.find_path(start)
    return files


# Вспомогательная функция, её наличие не обязательно и не будет проверяться
def build_bridge(start, end, path):
    files = build_tree(start, end, path)
    bridge = []
    # TODO Добавить нужные страницы в bridge
    return bridge


def parse(start, end, path):
    bridge = build_bridge(start, end, path)  # Искать список страниц можно как угодно, даже так: bridge = [end, start]

    # Когда есть список страниц, из них нужно вытащить данные и вернуть их
    out = {}
    for file in bridge:
        with open("{}{}".format(path, file)) as data:
            soup = BeautifulSoup(data, "lxml")

        body = soup.find(id="bodyContent")

        # TODO посчитать реальные значения
        imgs = 5  # Количество картинок (img) с шириной (width) не меньше 200
        headers = 10  # Количество заголовков, первая буква текста внутри которого: E, T или C
        linkslen = 15  # Длина максимальной последовательности ссылок, между которыми нет других тегов
        lists = 20  # Количество списков, не вложенных в другие списки

        out[file] = [imgs, headers, linkslen, lists]

    return out
