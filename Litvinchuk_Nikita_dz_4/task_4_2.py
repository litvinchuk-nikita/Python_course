# Задание №2. Написать функцию currency_rates(), принимающую в качестве аргумента код валюты (например, USD, EUR, GBP, ...)
# и возвращающую курс этой валюты по отношению к рублю.
# Использовать библиотеку requests.
# В качестве API можно использовать http://www.cbr.ru/scripts/XML_daily.asp.
# Рекомендация: выполнить предварительно запрос к API в обычном браузере, посмотреть содержимое ответа.
# Можно ли, используя только методы класса str, решить поставленную задачу?
# Функция должна возвращать результат числового типа, например float.
# Подумайте: есть ли смысл для работы с денежными величинами использовать вместо float тип Decimal?
# Сильно ли усложняется код функции при этом?
# Если в качестве аргумента передали код валюты, которого нет в ответе, вернуть None.
# Можно ли сделать работу функции не зависящей от того, в каком регистре был передан аргумент?
# В качестве примера выведите курсы доллара и евро.
import requests
from bs4 import BeautifulSoup
from decimal import Decimal


def currency_rates(code_volute):
    resp = requests.get('http://www.cbr.ru/scripts/XML_daily.asp')
    resp_text = resp.text
    soup = BeautifulSoup(resp_text, features="xml")
    my_dict = {}
    char_code_list = []
    value_list = []
    inx = 0
    for tag in soup.find_all('CharCode'):
        char_code_list.append(tag.text)
    for tag in soup.find_all('Value'):
        tag = str(tag.text).split(',')
        value_list.append('.'.join(tag))
    while inx < len(value_list):
        my_dict[char_code_list[inx]] = value_list[inx]
        inx += 1
    return Decimal(my_dict.get(str(code_volute).upper()))


if __name__ == '__main__':
    print(currency_rates('eur'))
    print(currency_rates('usd'))
    print(currency_rates('eur') - currency_rates('usd'))
    print(type(currency_rates('eur')))

# Задание №3. *(вместо 2) Доработать функцию currency_rates(): теперь она должна возвращать кроме курса дату,
# которая передаётся в ответе сервера.
# Дата должна быть в виде объекта date.
# Подумайте, как извлечь дату из ответа, какой тип данных лучше использовать в ответе функции?
from datetime import date


def currency_rates_1(code_volute):
    resp = requests.get('http://www.cbr.ru/scripts/XML_daily.asp')
    resp_text = resp.text
    soup = BeautifulSoup(resp_text, features="xml")
    my_dict = {}
    char_code_list = []
    value_list = []
    inx = 0
    date_value = soup.find('ValCurs')
    date_value = (str(date_value)[15:25]).split('.')
    date_value = date(day=int(date_value[0]), month=int(date_value[1]), year=int(date_value[2]))
    for tag in soup.find_all('CharCode'):
        char_code_list.append(tag.text)
    for tag in soup.find_all('Value'):
        tag = str(tag.text).split(',')
        value_list.append('.'.join(tag))
    for tag in soup.find_all('CharCode'):
        char_code_list.append(tag.text)
    while inx < len(value_list):
        my_dict[char_code_list[inx]] = value_list[inx]
        inx += 1
    print(Decimal(my_dict.get(str(code_volute).upper())), ',', date_value)


if __name__ == '__main__':
    currency_rates_1('eur')
    currency_rates_1('usd')
