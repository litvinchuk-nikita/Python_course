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

