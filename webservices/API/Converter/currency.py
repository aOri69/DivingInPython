from bs4 import BeautifulSoup, Tag
from decimal import Decimal, getcontext, localcontext


def convert(amount, cur_from, cur_to, date, requests):
    url = 'http://www.cbr.ru/scripts/XML_daily.asp?'
    if date is not None:
        url += 'date_req='
    response = requests.get(f'{url}{date}')  # Использовать переданный requests
    soup = BeautifulSoup(response.content, 'xml')
    tag_to = soup.find('CharCode', text=cur_to)
    nominal = int(tag_to.find_next_sibling('Nominal').string)
    value = Decimal(tag_to.find_next_sibling('Value').string.replace(',', '.', 1)) / nominal
    result = Decimal(Decimal(amount) / value).quantize(Decimal('.0001'))
    return result  # не забыть про округление до 4х знаков после запятой
