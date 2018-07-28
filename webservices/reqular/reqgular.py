import re

"""
БZ1,! - Обозначают сами себя
\d - от 0 до 9
\D - что угодно, кроме цифр
. - любой символ, кроме перевода строки
+ - 1 и более раз
* - 0 и более раз
? - 0 или 1 раз
() - группировка
"""
if __name__ == '__main__':
    html = "Курс евро на сегодня 68,7514, курс евро на завтра 67,8901"
    match = re.search(r'Евро\D+(\d+,\d+)', html, re.IGNORECASE)
    rate = match.group(1)
    print(rate)

    match = re.search(r'Евро\D+(\d+,\d+)', html)  # Без IGNORECASE не работает
    print(match is None)

    print(re.search(r'Евро.*(\d+,\d+)', html, re.IGNORECASE).group(1))
    print(re.search(r'Евро.*?(\d+,\d+)', html, re.IGNORECASE).group(1))
    print(re.findall(r'Евро\D+(\d+,\d+)', html, re.IGNORECASE))
    print(re.findall(r'Евро\D+(\d+),(\d+)', html, re.IGNORECASE))
    print(re.findall(r'Евро\D+((\d+),(\d+))', html, re.IGNORECASE))

    html = """Курс евро на сегодня (15 января) 
    68,7514
    курс евро на завтра 67,8901
    """
    print(re.search(r'Евро.*?(\d+,\d+)', html, re.IGNORECASE | re.DOTALL).group(1))
