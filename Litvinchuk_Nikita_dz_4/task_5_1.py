# Задание №1. Написать генератор нечётных чисел от 1 до n (включительно), используя ключевое слово yield, например:
# >>> odd_to_15 = odd_nums(15)
# >>> next(odd_to_15) 1
# >>> next(odd_to_15)
# 3
# ...
# >>> next(odd_to_15) 15
# >>> next(odd_to_15) ...StopIteration...


def odd_nums(n):
    for num in range(1, n + 1, 2):
        yield num


odd_to_15 = odd_nums(15)
print(next(odd_to_15))  # 1
print(next(odd_to_15))  # 3
print(next(odd_to_15))  # 5
print(next(odd_to_15))  # 7
print(next(odd_to_15))  # 9
print(next(odd_to_15))  # 11
print(next(odd_to_15))  # 13
print(next(odd_to_15))  # 15
print(next(odd_to_15))  # ...StopIteration...
