#Задачи на циклы и оператор условия------
#----------------------------------------

'''
Задача 1
Вывести на экран циклом пять строк из нулей, причем каждая строка должна быть пронумерована.
'''

# for i in range(5):
#     print('Строка №', i + 1, '-', i * 0)

'''
Задача 2
Пользователь в цикле вводит 10 цифр. Найти количество введеных пользователем цифр 5.
'''

# print('Цифры и числа - это разные вещи... (© Конфуций)')
# i = 0
# five_amount = 0
# while i < 10:
#     user_input = input('Введите цифру ') # Обработка пользовательского ввода
#     try:
#         user_input = int(user_input)
#     except ValueError:
#         print('Неверно, цифрами являются - 0, 1, 2, 3, 4, 5, 6, 7, 8, 9')
#     else: # Алгоритм подсчёта цифр 5
#         if 0 <= user_input < 10:
#             i += 1
#             if user_input == 5:
#                 five_amount += 1
#         else:
#             print('Неверно, цифрами являются - 0, 1, 2, 3, 4, 5, 6, 7, 8, 9')
# print('Количество введеных цифр 5 =', five_amount)

'''
Задача 3
Найти сумму ряда чисел от 1 до 100. Полученный результат вывести на экран.
'''

# sum = 0
#
# for i in range(1,101):
#     sum += i
# print(sum)

'''
Задача 4
Найти произведение ряда чисел от 1 до 10. Полученный результат вывести на экран.
'''

# multiply = 1
#
# for i in range(1,11):
#     multiply *= i
# print(multiply)

'''
Задача 5
Вывести цифры числа на каждой строчке.
'''

# integer_number = 2129
#
# #print(integer_number % 10, integer_number // 10)
#
# while integer_number > 0:
#     print(integer_number % 10)
#     integer_number = integer_number // 10

'''
Задача 6
Найти сумму цифр числа.
'''

## Пользовательский ввод и его обработка

# integer_number = input('Введите целое число ')
# while type(integer_number) != int:
#     try:
#         integer_number = int(integer_number)
#     except ValueError:
#         print('Неверно, необходимо ввести целое число')
#         integer_number = input('Введите целое число ')
#     else:
#         integer_number = abs(integer_number)

## Алгоритм нахождения суммы цифр числа

# sum_numeral = 0
# while integer_number > 0:
#     sum_numeral += integer_number % 10
#     integer_number = integer_number // 10
# print(sum_numeral)

'''
Задача 7
Найти произведение цифр числа.
'''

## Пользовательский ввод и его обработка

# integer_number = input('Введите целое число ')
# while type(integer_number) != int:
#     try:
#         integer_number = int(integer_number)
#     except ValueError:
#         print('Неверно, необходимо ввести целое число')
#         integer_number = input('Введите целое число ')
#     else:
#         integer_number = abs(integer_number)

## Алгоритм умножения цифр числа

# multiply_numeral = 1
# while integer_number > 0:
#     multiply_numeral *= integer_number % 10
#     integer_number = integer_number // 10
# print(multiply_numeral)

'''
Задача 8
Дать ответ на вопрос: есть ли среди цифр числа 5?
'''
# integer_number = 213413
# while integer_number > 0:
#     if integer_number % 10 == 5:
#         print('Yes')
#         break
#     integer_number = integer_number // 10
# else:
#     print('No')

'''
Задача 9
Найти максимальную цифру в числе
'''
## Обработка пользовательского ввода

# integer_number = input('Введите целое число ')
# while type(integer_number) != int:
#     try:
#         integer_number = int(integer_number)
#     except ValueError:
#         print('Неверно, необходимо ввести целое число')
#         integer_number = input('Введите целое число ')
#     else:
#         integer_number = abs(integer_number)

# # Алгоритм поиска наибольшей цифры в числе

# max_numeral = 0
# while integer_number > 0:
#     if integer_number % 10 > max_numeral:
#         max_numeral = integer_number % 10
#     integer_number = integer_number // 10
# print(max_numeral)

'''
Задача 10
Найти количество цифр 5 в числе
'''
## И снова обработка ввода

# integer_number = input('Введите целое число ')
# while type(integer_number) != int:
#     try:
#         integer_number = int(integer_number)
#     except ValueError:
#         print('Неверно, необходимо ввести целое число')
#         integer_number = input('Введите целое число ')
#     else:
#         integer_number = abs(integer_number)

# # И снова алгоритм подсчета пятерок
# five_numeral = 0
# while integer_number > 0:
#     if integer_number % 10 == 5:
#         five_numeral += 1
#     integer_number = integer_number // 10
# print(five_numeral)