import requests
import time
import re
from random import randint

BOOK_PATH = 'https://www.gutenberg.org/files/2638/2638-0.txt'


def benchmark(func):
    """
    Декоратор, выводящий время, которое заняло выполнение декорируемой функции
    """

    def wrapper(*args, **kwargs):
        t1 = time.time()
        # print('Начало работы')
        func(*args, **kwargs)
        t2 = time.time()
        # print('Окончание работы')
        print("Время исполнения - ", t2 - t1)
        return func(*args, **kwargs)

    return wrapper


def logging(func):
    """
    Декоратор, который выводит параметры с которыми была вызвана функция
    """

    def wrapper(*args, **kwargs):
        # func(*args, **kwargs)
        k = args
        t = kwargs
        print(f"Функция вызвана с параметрами: {k},{t}")
        return func(*args, **kwargs)

    return wrapper


def counter(func):
    """
    Декоратор, считающий и выводящий количество вызовов декорируемой функции
    """

    def wrapper(*args, **kwargs):
        global countl
        countl = countl + 1
        # func(*args, **kwargs)
        print("Функция вызвана ", countl, "раз")
        return func(*args, **kwargs)

    return wrapper


countl = 0


@counter
@logging
@benchmark
def word_count(word, url=BOOK_PATH):
    """
    Функция для посчета указанного слова на html-странице
    """

    # отправляем запрос в библиотеку Gutenberg и забираем текст
    raw = requests.get(url).text

    # заменяем в тексте все небуквенные символы на пробелы
    processed_book = re.sub('[\W]+', ' ', raw).lower()

    # считаем
    cnt = len(re.findall(word.lower(), processed_book))
    # my_str = "Cлово " + word + " встречается " + str(cnt) + " раз"
    # print(my_str)
    return f"Cлово {word} встречается {cnt} раз"


print(word_count('whole'))
