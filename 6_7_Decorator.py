'''
Создайте декоратор memo для реализации механизма мемоизации. Для проверки используйте функции из предыдущей задачи.

Пример работы:

>>> @memo
@perf
def fib(n):
    ...

>>> fib(27)
196418
>>> PERF
{'fact': 10, 'fib': 28}
'''
PERF = dict()


def make_perf(pd):
    def perf_(func):
        def inner(*args):
            pd.setdefault(func.__name__, 0)
            pd[func.__name__] += 1
            return func(*args)
        return inner
    return perf_


MEM = dict()


def make_mem(pb):
    def memo(func):
        def inner(arg):
            if arg in pb.keys():
                return pb[arg]
            pb[arg] = func(arg)
            return pb[arg]
        return inner
    return memo


perf = make_perf(PERF)
memo = make_mem(MEM)


@make_perf(PERF)
def fact(n):
    if n <= 1:
        return 1
    return n * fact(n - 1)


@memo
@perf
def fib(n):
    if n < 2:
        return 1
    return fib(n-1) + fib(n - 2)


print(fib(26))
print(PERF)
