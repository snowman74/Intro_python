'''
LIGHT:

Необходимо реализовать модуль divisor_master. Все функции модуля принимают на вход натуральные числа от 1 до 1000.
Модуль содержит функции:

1) проверка числа на простоту (простые числа - это те числа у которых делители единица и они сами);
2) выводит список всех делителей числа;
3) выводит самый большой простой делитель числа.

PRO:
LIGHT +
4) функция выводит каноническое разложение числа
(https://zaochnik.com/spravochnik/matematika/delimost/razlozhenie-chisel-na-prostye-mnozhiteli/) на простые множители;
5) функция выводит самый большой делитель (не обязательно простой) числа.
'''

#1
def simple_number(x):
    '''

    :param x: На вход получает целое положительное число из диапазона 1 - 1000
    :return:  Возвращает True если число простое, иначе - возвращает False
    '''
    if type(x) != int or x <= 0:
        answer = 'Необходимо ввести целое положительное число.'
    elif x == 1:
        answer = '''К началу XX века математики стали приходить к консенсусу о том,
    что 1 не является простым числом, а скорее формирует свою специальную категорию — «единицу» (© Wikipedia)'''
    elif 2 <= x <= 1000 and type(x) is int:
        n = []
        for i in range(2, x):
            if x % i == 0:
                n.append(i)
        if n == []: answer = True
        else: answer = False
    return answer

#2
def devisors_list(x):
    if type(x) != int or x <= 0:
        answer = 'Необходимо ввести целое положительное число.'
    elif x == 1:
        answer = 1
    elif 2 <= x <= 1000 and type(x) is int:
        answer = []
        for i in range(2, x):
            if x % i == 0:
                answer.append(i)
    return answer

# 3
def top_simple_devisor(x):
    m = []
    n = devisors_list(x)
    for i in n:
        if simple_number(i) == True:
            m.append(i)
    return m[-1]

# 4
def canon_factorization(x):
    '''
    :param x: на вход подаётся целое положительное число до 1000
    :return: возвращается каноническое разложение, например 900 = 2^2 * 3^2 * 5^2
    '''
    a = x
    p = []
    n = [k for k in range(2, x) if simple_number(k)]
    dic = {}
    i = 0
    while not simple_number(a):
        if a % n[i] == 0:
            p.append(n[i])
            a //= n[i]
        else:
            i += 1
    p.append(a)
    for i in p:
        dic[i] = 1
    for i in range(len(p) - 1):
        if p[i] == p[i + 1]:
            dic[p[i]] += 1
    answer = ''
    for key, value in dic.items():
        answer += (f' {key}^{value} *')
    answer = f'{x} =' + answer[:-1]
    return answer

# 5
def top_devisor(x):
    if type(x) != int or x <= 0:
        answer = 'Необходимо ввести целое положительное число.'
    elif x == 1:
        answer = 1
    elif 2 <= x <= 1000 and type(x) is int:
        n = []
        for i in range(2, x):
            if x % i == 0:
                n.append(i)
        answer = n[-1]
    return answer
