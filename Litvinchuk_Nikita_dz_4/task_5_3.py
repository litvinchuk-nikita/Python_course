# Задание №3. Есть два списка:
# tutors = [
# 'Иван', 'Анастасия', 'Петр', 'Сергей', 'Дмитрий', 'Борис', 'Елена'
# ]
# klasses = [
# '9А', '7В', '9Б', '9В', '8Б', '10А', '10Б', '9А' ]
# Необходимо реализовать генератор, возвращающий кортежи вида (<tutor>, <klass>), например:
# Количество генерируемых кортежей не должно быть больше длины списка tutors.
# Если в списке klasses меньше элементов, чем в списке tutors,
# необходимо вывести последние кортежи в виде: (<tutor>, None), например:
# ('Станислав', None)
# Доказать, что вы создали именно генератор. Проверить его работу вплоть до истощения.
# Подумать, в каких ситуациях генератор даст эффект.
from itertools import zip_longest

tutors = ['Иван', 'Анастасия', 'Петр', 'Сергей', 'Дмитрий', 'Борис', 'Елена']
klasses = ['9А', '7В', '9Б', '9В', '8Б', '10А']


def gen_tuple():
    if len(tutors) <= len(klasses):
        for result in zip(tutors, klasses):
            yield tuple(result)
    else:
        for result in zip_longest(tutors, klasses):
            yield tuple(result)


result = gen_tuple()
print(type(result))  # <class 'generator'>
print(next(result))  # ('Иван', '9А')
print(next(result))  # ('Анастасия', '7В')
print(next(result))  # ('Петр', '9Б')
print(next(result))  # ('Сергей', '9В')
print(next(result))  # ('Дмитрий', '8Б')
print(next(result))  # ('Борис', '10А')
print(next(result))  # ('Елена', None)
print(next(result))  # StopIteration
