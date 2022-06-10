# Написать скрипт, который выводит статистику для заданной папки в виде словаря,
# в котором ключи — верхняя граница размера файла (пусть будет кратна 10),
# а значения — общее количество файлов (в том числе и в подпапках),
# размер которых не превышает этой границы, но больше предыдущей (начинаем с 0),
# например:
# {
# 100: 15,
# 1000: 3,
# 10000: 7,
# 100000: 2
# }
# Тут 15 файлов размером не более 100 байт; 3 файла больше 100 и не больше 1000 байт...
# Подсказка: размер файла можно получить из атрибута .st_size объекта os.stat.
import os
my_path = os.getcwd()
my_dict = {}
for key in [100, 1000, 10000, 100000]:
    my_dict[key] = 0
for root, dirs, files in os.walk(my_path):
    for file in files:
        if os.stat(os.path.realpath(os.path.join(root, file))).st_size <= 100:
            my_dict[100] += 1
        elif 100 < os.stat(os.path.realpath(os.path.join(root, file))).st_size <= 1000:
            my_dict[1000] += 1
        elif 1000 < os.stat(os.path.realpath(os.path.join(root, file))).st_size <= 10000:
            my_dict[10000] += 1
        elif 10000 < os.stat(os.path.realpath(os.path.join(root, file))).st_size <= 100000:
            my_dict[100000] += 1
print(my_dict)
