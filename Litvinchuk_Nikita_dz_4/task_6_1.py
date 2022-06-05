# Задание №1. Не используя библиотеки для парсинга, распарсить (получить определённые данные) файл логов web-сервера
# nginx_logs.txt (https://github.com/elastic/examples/raw/master/Common%20Data%20Formats/nginx_logs/nginx_logs)
# — получить список кортежей вида: (<remote_addr>, <request_type>, <requested_resource>).
# Например:
# [
# ...
# ('141.138.90.60', 'GET', '/downloads/product_2'),
# ('141.138.90.60', 'GET', '/downloads/product_2'),
# ('173.255.199.22', 'GET', '/downloads/product_2'), ...
# ]
# Вариант №1.
my_list = []
with open('nginx_logs.txt', encoding='utf-8') as f:
    for line in f:
        line = line.split(' ')
        my_list.append((line[0], line[5].replace('"', ''), line[6]))
print(my_list)

# Вариант №2.
with open('nginx_logs.txt', encoding='utf-8') as f:
    my_gen = (line.split(' ') for line in f)
    my_list = [(line[0], line[5].replace('"', ''), line[6]) for line in my_gen]
print(my_list)
