# Есть два файла: в одном хранятся ФИО пользователей сайта, а в другом — данные об их хобби.
# Известно, что при хранении данных используется принцип:
# одна строка — один пользователь, разделитель между значениями — запятая.
# Написать код, загружающий данные из обоих файлов и формирующий из них словарь:
# ключи — ФИО, значения — данные о хобби. Сохранить словарь в файл.
# Проверить сохранённые данные.
# Если в файле, хранящем данные о хобби, меньше записей, чем в файле с ФИО, задаём в словаре значение None.
# Если наоборот — выходим из скрипта с кодом «1».
# При решении задачи считать, что объём данных в файлах во много раз меньше объема ОЗУ.
# Фрагмент файла с данными о пользователях (users.csv):
# Иванов,Иван,Иванович
# Петров,Петр,Петрович
# Фрагмент файла с данными о хобби (hobby.csv):
# скалолазание,охота
# горные лыжи
import json
from itertools import zip_longest
with open('users.csv', encoding='utf-8') as f:
    user_list = [line.strip() for line in f]
with open('hobby.csv', encoding='utf-8') as f:
    hobby_list = [line.strip() for line in f]
if len(user_list) >= len(hobby_list):
    my_dict = dict(zip_longest(user_list, hobby_list))
else:
    my_dict = dict(zip(user_list, hobby_list))
with open('result_task_6_3.json', 'w', encoding='utf-8') as f:
    result = json.dumps(my_dict)
    f.write(result)
with open('result_task_6_3.json', encoding='utf-8') as f:
    result = f.read()
    my_dict = json.loads(result)
    print(my_dict)

