# Задание №1. Реализовать вывод информации о промежутке времени в зависимости от его продолжительности duration в секундах:
# a. до минуты: <s> сек;
# b. до часа: <m> мин <s> сек;
# c. до суток: <h> час <m> мин <s> сек;
# d. * в остальных случаях: <d> дн <h> час <m> мин <s> сек.
# Вариант решения a, b, c, d в одном коде.
duration = int(input('Введите целое положительное число: '))
if duration // 60 <= 0:
    print(f'{duration} сек')
elif duration // 60 < 36:
    minute = duration // 60
    second = duration % 60
    print(f'{minute} мин {second} сек')
elif 0 < duration // 3600 <= 24 and duration // 60 < 36:
    hour = duration // 3600
    minute = duration % 3600 // 60
    second = duration % 60
    print(f'{hour} час {minute} мин {second} сек')
else:
    day = duration // 86400
    hour = duration % 86400 // 3600
    minute = duration % 3600 // 60
    second = duration % 60
    print(f'{day} дн {hour} час {minute} мин {second} сек')
