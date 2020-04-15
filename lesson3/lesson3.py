# Считываем текст из файла и импортируем модули
import pymorphy2
morph = pymorphy2.MorphAnalyzer()
file = open('text.txt', 'r', encoding='utf-8')
text = file.read()
file.close()

# Пункт 1. Вариант 1. Очистить от знаков препинания
'''
marks = [',', '.', '!', '?', '-', ':', ';', '"', '«', '»', '—', '(', ')']
list_text = list(text)
for i in text:
    if i in marks:
        list_text.remove(i)
text = ''.join(list_text)
text = text.replace('\n', ' ')
print(text)
'''
# Пункт 1. Вариант 2

marks = [',', '.', '!', '?', ' -', ':', ';', '"', '«', '»', '—', '(', ')']
for i in marks:
    text = text.replace(i, '')
text = text.replace('\n', ' ')  # Заменяем знаки абзаца на пробел
text = text.replace('  ', ' ')  # Заменяем два пробела подряд на один
text = ''.join(text)
print(text, end='\n\n')

# Пункт 2. Формируем список со словами

words_list = text.split()

# Пункт 3. Приводим все слова к нижнему регистру

lower_words = list(map(lambda x: x.lower(), words_list))
print(lower_words, end='\n\n')

# ВОПРОС. Чем хуже следующий код?
'''
text = text.lower()
words_list = text.split()
print(words_list)
'''


# Пункт 5 (лемматизация)

lower_words.sort()
words = lower_words.copy()

lem_words = []

for i in words:
    i = morph.parse(i)[0]
    lem_words.append(i.normal_form)

lem_words.sort()
print(len(lem_words))


# Пункт 3.1. Получить из list пункта 3 dict, ключами которого являются слова, а значениями их количество появлений в тексте

dictionary = {}


for i in words:                         # для лемматизированного списка заменить words на lem_words 
    dictionary[i] = 1                   #Видна разница:
                                        #Самые популярнае слова до Лемматизации:
                                        #[('и', 36), ('он', 29), ('в', 29), ('не', 19), ('с', 17)]
                                        # Самые популярнае слова после Лемматизации:
                                        #[('и', 36), ('в', 28), ('не', 19), ('он', 18), ('с', 15)]
for i in range(len(words)-1):           #
    if words[i] == words[i+1]:          #
        dictionary[words[i]] += 1       #
'''
for i in lem_words:
    dictionary[i] = 1

for i in range(len(lem_words)-1):
    if lem_words[i] == lem_words[i+1]:
        dictionary[lem_words[i]] += 1
'''
print(dictionary, end='\n\n')

# Пункт 4. Вывести 5 наиболее часто встречающихся слов (sort), вывести количество разных слов в тексте (set).

popular_words_list= list(dictionary.items())
popular_words_list.sort(key= lambda i: i[1])
popular_words_list.reverse()
popular_words_list = popular_words_list [:5]

print('Самые популярные слова', popular_words_list, end='\n\n')

for i in range(len(popular_words_list)):
    print('Слово ', popular_words_list[i][0], 'встречается в тексте ', popular_words_list[i][1], 'раз.', end='\n\n')

print('Количество разных слов в тексте:', len(set(words)), end='\n\n')

