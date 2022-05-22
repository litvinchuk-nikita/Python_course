# Задание №1. Написать функцию num_translate(), переводящую числительные от 0 до 10 c английского на русский язык.
# Например:
# >>> num_translate("one") "один"
# >>> num_translate("eight") "восемь"
# Если перевод сделать невозможно, вернуть None.
# Подумайте, как и где лучше хранить информацию, необходимую для перевода: какой тип данных выбрать, в теле функции или снаружи.


def num_translate(english_number):
    num_translate_dict = {'zero': 'ноль', 'one': 'один', 'two': 'два', 'three': 'три', 'four': 'четыре', 'five': 'пять',
                          'six': 'шесть', 'seven': 'семь', 'eight': 'восемь', 'nine': 'девять', 'ten': 'десять'}
    return num_translate_dict.get(english_number)


# Задание №2. *(вместо задачи 1) Доработать предыдущую функцию в num_translate_adv():
# реализовать корректную работу с числительными, начинающимися с заглавной буквы — результат тоже должен быть с заглавной.
# Например:
# >>> num_translate_adv("One") "Один"
# >>> num_translate_adv("two") "два"


def num_translate_adv(english_number):
    num_translate_dict = {'zero': 'ноль', 'one': 'один', 'two': 'два', 'three': 'три', 'four': 'четыре', 'five': 'пять',
                          'six': 'шесть', 'seven': 'семь', 'eight': 'восемь', 'nine': 'девять', 'ten': 'десять'}
    if str(english_number).istitle():
        try:
            return num_translate_dict.get(str(english_number).lower()).capitalize()
        except AttributeError:
            return None
    else:
        return num_translate_dict.get(english_number)
