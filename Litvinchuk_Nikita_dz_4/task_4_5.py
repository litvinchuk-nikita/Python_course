# Задание №5. *(вместо 4) Доработать скрипт из предыдущего задания: теперь он должен работать и из консоли.
# Например:
#  > python task_4_5.py USD
#  75.18, 2020-09-05
from utils import currency_rates
import sys

try:
    command = sys.argv[1]
except IndexError:
    print('Введите наименование валюты')
else:
    print(currency_rates(str(command)))
