# Задание №2. *(вместо 1) Решить задачу генерации нечётных чисел от 1 до n (включительно),
# не используя ключевое слово yield.
n = 15
odd_num = (num for num in range(1, n + 1, 2))
print(next(odd_num))  # 1
print(next(odd_num))  # 3
print(next(odd_num))  # 5
print(next(odd_num))  # 7
print(next(odd_num))  # 9
print(next(odd_num))  # 11
print(next(odd_num))  # 13
print(next(odd_num))  # 15
print(next(odd_num))  # StopIteration
