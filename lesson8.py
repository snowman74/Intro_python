import time, os, psutil, sys

def decor_time(f):

    def timer(*args, **kwargs):
        start = time.perf_counter()
        # f(*args, **kwargs)
        f_result = f(*args, **kwargs)
        """думал дополнительно выводить результат выполнения, но на
        этапе с генератором списка до 1000000 - 
        комп начал чихать и кашлять"""
        stop = time.perf_counter()
        return f'Время выполнения функции равно {stop - start}', f_result

    return timer


def decor_ram(f):

    def rammeter(*args, **kwargs):
        proc = psutil.Process(os.getpid())
        init_state = proc.memory_info().rss/1000000
        res = f(*args, **kwargs)
        final_state = proc.memory_info().rss/1000000
        return f'Память, занимаемая выполнением функции равна {final_state-init_state}', res

    return rammeter

# Ради интереса хотел импортировать весь свой модуль из 5 урока, не вышло, при добавлении пути к
# модулю выдал следующую ошибку -
# File "C:/Users/Max/PycharmProjects/Intro_python/lesson8.py", line 21
#     paths.append('C:\Users\Max\PycharmProjects\Intro_python\lesson5\divisor_master.py')
#                 ^
# SyntaxError: (unicode error) 'unicodeescape' codec can't decode bytes in position 2-3: truncated \UXXXXXXXX escape


@decor_ram
@decor_time
def devisors_list(x):
    """

    :param x: на вход подаётся целое положительное число до 1000
    :return: возвращается список всех делителей этого числа
    """
    if type(x) != int or x <= 0:
        answer = 'Необходимо ввести целое положительное число.'
    elif x == 1:
        answer = 1
    elif 2 <= x <= 1000:
        answer = []
        for i in range(1, x+1):
            if x % i == 0:
                answer.append(i)
    return answer


@decor_ram
@decor_time
def list_maker(n):
    L = [i for i in range(n)]
    return L

print(list_maker(100))


@decor_ram
@decor_time
def generator(n):
    for i in range(n):
        yield i

print(generator(100000000000))