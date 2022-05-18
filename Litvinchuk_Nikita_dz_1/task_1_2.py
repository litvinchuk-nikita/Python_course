# Задание 2.Создать список, состоящий из кубов нечётных чисел от 1 до 1000 (куб X - третья степень числа X):
# a. Вычислить сумму тех чисел из этого списка, сумма цифр которых делится нацело на 7.
# Например, число «19 ^ 3 = 6859» будем включать в сумму, так как 6 + 8 +5+9=28– делится нацело на 7.
# Внимание: использовать только арифметические операции!
# b.К каждому элементу списка добавить 17 и заново вычислить сумму тех чисел из этого списка,
# сумма цифр которых делится нацело на 7.
# c.* Решить задачу под пунктом b, не создавая новый список.
# Вариант а.
list_numbers = []
result = 0
for inx in range(1, 1001, 2):
    list_numbers.append(inx ** 3)
for number in list_numbers:
    sum_numbers = 0
    for index in str(number):
        sum_numbers += int(index)
    if sum_numbers % 7 == 0:
        result += number
print(result)
# Вариант b.
list_numbers = []
result = 0
for inx in range(1, 1001, 2):
    list_numbers.append(inx ** 3)
list_numbers_2 = []
for num in list_numbers:
    list_numbers_2.append(num + 17)
for number in list_numbers_2:
    sum_numbers = 0
    for index in str(number):
        sum_numbers += int(index)
    if sum_numbers % 7 == 0:
        result += number
print(result)
# Вариант c. (Вариант С взял из вашего решения).
list_numbers = []
result = 0
for inx in range(1, 1001, 2):
    list_numbers.append(inx ** 3)
for number in list_numbers:
    number += 17
    sum_numbers = 0
    for index in str(number):
        sum_numbers += int(index)
    if sum_numbers % 7 == 0:
        result += number
print(result)