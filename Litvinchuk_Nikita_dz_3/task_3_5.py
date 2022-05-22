# Реализовать функцию get_jokes(), возвращающую n шуток, сформированных из трех случайных слов,
# взятых из трёх списков (по одному из каждого):
# nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
# adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
# adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]
# Например:
#  >>> get_jokes(2)
# ["лес завтра зеленый", "город вчера веселый"]
# Документировать код функции.
# Сможете ли вы добавить еще один аргумент — флаг, разрешающий или запрещающий повторы слов в шутках
# (когда каждое слово можно использовать только в одной шутке)?
# Сможете ли вы сделать аргументы именованными?
import random


def get_jokes(number_of_jokes, repete_words=False):
    """
    Function for creating jokes
    :param number_of_jokes: int (from 1 to n).
    :param repete_words: If you don't want words to be repeated in jokes, select True
    :return: list of jokes
    """
    nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
    adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
    adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]
    list_jokes = []
    inx = 0
    if repete_words:
        try:
            word_1 = random.sample(nouns, k=number_of_jokes)
            word_2 = random.sample(adverbs, k=number_of_jokes)
            word_3 = random.sample(adjectives, k=number_of_jokes)
            while inx < number_of_jokes:
                jok = f'{word_1[inx]} {word_2[inx]} {word_3[inx]}'
                list_jokes.append(jok)
                inx += 1
        except ValueError:
            return f' Max number_of_jokes = {len(nouns)}'
    else:
        while inx < number_of_jokes:
            jok = f'{random.choice(nouns)} {random.choice(adverbs)} {random.choice(adjectives)}'
            list_jokes.append(jok)
            inx += 1
    return list_jokes
