'''
Light:
1. Выберете дз, к функциям которого будете писать тесты (например, вебинар 5);
2. Создайте дополнительную ветку в репозитории GitHub с тестами;
3. Напишите не менее 5ти тестов к функциям выбранного урока;
4. В качестве ответа на дз пришлите ссылку на ветку с тестами или ссылку на PullRequest ветки с тестами с веткой master.
Pro:
light +
5. Придумайте 2 теста к грязной функции. Примером грязной функции является функция F из задания 4;
Пришлите ответ по инструкции 4.
Немного про грязные функции:
https://ru.wikipedia.org/wiki/%D0%A7%D0%B8%D1%81%D1%82%D0%BE%D1%82%D0%B0_%D1%84%D1%83%D0%BD%D0%BA%D1%86%D0%B8%D0%B8
'''
#1
def simple_number(x):
    answer = 'Необходимо ввести целое положительное число.'
    '''

    :param x: На вход получает целое положительное число из диапазона 1 - 1000
    :return:  Возвращает True если число простое, иначе - возвращает False
    '''
    if type(x) != int or x <= 0:
        pass
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
    '''

    :param x: на вход подаётся целое положительное число до 1000
    :return: возвращается список всех делителей этого числа
    '''
    if type(x) != int or x <= 0:
        answer = 'Необходимо ввести целое положительное число.'
    elif x == 1:
        answer = 1
    elif 2 <= x <= 1000 and type(x) is int:
        answer = []
        for i in range(1, x+1):
            if x % i == 0:
                answer.append(i)
    return answer

# 3
def top_simple_devisor(x):
    '''

    :param x: на вход подаётся целое положительное число до 1000
    :return: возвращается наибольший простой делитель этого числа
    '''
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
    return p

# 5
def top_devisor(x):
    '''
    :param x: на вход подаётся целое положительное число до 1000
    :return: возвращается наибольший делитель этого числа
    '''
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

# 6
import random

def random_names(list_names, number_names):
    '''
    :param list_names: список имён, из которых будет производится выборка
    :param number_names: число имён, которое будет выведено
    :return: список случайных имен, количество элементов которого равно number_names
    '''
    final_list = []
    i = 0
    while i != number_names:
        final_list.append(list_names[random.randint(0, len(list_names)-1)])
        i += 1
    return final_list

# 1
def test_1_simple_number():
    assert simple_number('as') == 'Необходимо ввести целое положительное число.'
# 2
def test_2_simple_number():
    assert simple_number(7) == True
# 3
def test_top_devisor():
    assert top_devisor(505) == 101
# 4
def test_devisors_list():
    assert devisors_list(10) == [1,2,5,10]
# 5
def test_top_simple_devisor():
    assert top_simple_devisor(998) == 499
# 6
def test_canon_factorization():
    assert canon_factorization(45) == [3, 3, 5]
# 7
def test_1_random_names():
    names = ['Галина', 'Ксения', 'Валерия', 'Кирилл', 'Вячеслав']
    assert len(random_names(names, 10)) == 10
# 8
def test_2_random_names():
    names = ['Галина', 'Ксения', 'Валерия', 'Кирилл', 'Вячеслав'] # Хотел показать, что если количество элементов
    el = 'Ксения'                                                 # входного списка много меньше выходного, то
    assert (el in random_names(names, 15)) == True                # с высокой вероятностью выходной список будет содержать
                                                                  # все элементы входного. Тест иногда не выполняется,
                                                                  # потому что он "не очень" =(
                                                                  # ну и потому что зависит от функции random.randint()