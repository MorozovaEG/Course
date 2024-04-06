def logging(func):
    """
    Декоратор, который выводит параметры с которыми была вызвана функция
    """

    def wrapper(*args, **kwargs):
      print(f"Функция вызвана с параметрами: {*args}, {**kwargs}")
    return wrapper