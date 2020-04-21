import random

file = open('names.txt', 'r', encoding='utf-8')     # читаем неформатированный файл с именами (дёрнул с сайта)
names = file.read()
file.close()

a = ord('а')                                            # создаем список русских букв для форматирования списка имён (можно
rus_letters = ''.join([chr(i) for i in range(a, a+32)])     # как то иначе сделать, но в голову первой пришла такая идея)
rus_letters = list(rus_letters + rus_letters.upper() + 'ё' + 'Ё')

def text_editor(text, alphabet):
    '''
    функция разбивает текст на входе на отдельные слова, затем выдаёт их список
    :param text: указывается переменная с текстом, который нужно преобразовать
    :param alphabet: указывается алфавит знаков, из которых состоят слова текста
    :return: возвращается список слов, из которых состоит текст
    '''
    text = text + ' '
    list_symbols = []
    for i in range(len(text)-1):
        if text[i] in alphabet:
            list_symbols.append(text[i])
            if text[i+1] not in alphabet:
                list_symbols.append(' ')

    text = ''.join(list_symbols)
    text = text.split(' ')
    del text[len(text)-1]
    words = list(map(lambda x: x.lower().title(), text)) # Делает первую букву каждого слова заглавной, а остальные - строчными
    return words

test_list = text_editor(names, rus_letters)

'''
Напишите функцию (F): на вход список имен и целое число N; на выходе список длины N случайных имен из первого списка
(могут повторяться, можно взять значения: количество имен 20, N = 100, рекомендуется использовать функцию random).
'''
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

rand_names = random_names(test_list, 50)
print('Список случайных имён:', rand_names, end='\n\n')

'''
Напишите функцию вывода самого частого имени из списка на выходе функции F;
'''
def popular_name(list_names):
    '''
    :param list_names: на вход подаётся список имён
    :return:    на выходе самое частое имя
    '''
    list_names = sorted(list_names)
    dictionary = {}
    # кусок из предыдущего урока (чего коду пропадать)
    for i in list_names:
        dictionary[i] = 1

    for i in range(len(list_names) - 1):
        if list_names[i] == list_names[i + 1]:
            dictionary[list_names[i]] += 1

    popular_words_list = sorted(list(dictionary.items()), key=lambda i: i[1], reverse=True)
    popular_words_list = popular_words_list[:1]

    if popular_words_list[0][1] == 1:
        print('Самого частого имени нет, все редкие')
    else:
        return popular_words_list[0][0] # выведет только имя
    #return popular_words_list[0]       # - выведет имя и число повторений

pop_name = popular_name(rand_names)

'''
 Напишите функцию вывода самой редкой буквы, с которого начинаются имена в списке на выходе функции F.
'''
def rare_letter(list_words):
    '''
    :param list: список слов
    :return:    самая редкая буква с которой начинаются эти слова
    '''
    letters_list = []
    dictionary = {}

    for i in list_words:
        letters_list.append(i[:1])

    letters_list = sorted(letters_list)
    # кусок из предыдущего урока (чего коду пропадать)
    for i in letters_list:
        dictionary[i] = 1

    for i in range(len(letters_list) - 1):
        if letters_list[i] == letters_list[i + 1]:
            dictionary[letters_list[i]] += 1

    letters_list = sorted(list(dictionary.items()), key=lambda i: i[1])

    return letters_list[0][0]

rare_let = rare_letter(rand_names)


print('Самое частое имя:', pop_name, end='\n\n')
print('Самая редкая буква с которой начинаются имена: ',rare_let, end='\n\n')

# Пункт 4. В файле с логами найти дату самого позднего лога (по метке времени)

file = open("log", "r", encoding='utf-8')
date_time = []
for line in file:
    dtime = line.split(',')
    dtime = dtime[0]
    date_time.append(dtime)

file.close()
sort_dates = sorted(date_time)
sort_dates.reverse()
latest_date = sort_dates[0]
print(latest_date)