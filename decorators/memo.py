import time
def memo(func):
  """
  Декоратор, запоминающий результаты исполнения функции func, чьи аргументы args должны быть хешируемыми
  """
  cache = {}

  def fmemo(*args):
    if args not in cache:
        cache[args] = func(*args)
    return cache[args]

  fmemo.cache = cache
  return fmemo

def fib(n):
    if n < 2:
        return n
    return fib(n-2) + fib(n-1)

# измеряем время выполнения
t1=time.time()
s=fib(30)
t2=time.time()
print(s,t2-t1)


@memo
def fib(n):
    if n < 2:
        return n
    return fib(n-2) + fib(n-1)

# измеряем время выполнения
t1=time.time()
s=fib(30)
t2=time.time()
print(s,t2-t1)