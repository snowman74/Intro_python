# костыли дичайшие
import time, csv, datetime as dt

start_time = dt.datetime.now()
file = 'weapon.txt'


def get_list_data(file):

    data = [[] * i for i in range(2)]
    with open('weapon.txt', encoding='utf-8') as f:
        while True:
            line = f.readline()
            if not line:
                break
            data[0].append(line.split(' - ')[0])
            data[1].append(line.split(' - ')[1].strip())

    return data


with open('lesson7.csv', 'w', encoding='utf-8') as f:
    writer = csv.writer(f, delimiter = ';')
    writer.writerow(get_list_data(file))


def get_dict_data(file): # возвращает словарь аргументов
    data = []
    with open(file, encoding='utf-8') as f:
        for line in f:
            data.append(line)

    list_temp = []
    for i in data:
        list_temp.append(i.split(' - '))

    dict_temp = {}
    for i in list_temp:
        i[1] = i[1][:-1]
        dict_temp[i[0]] = i[1]
    dict_temp = [dict_temp]
    return dict_temp


list_csv = get_list_data(file)
dict_csv = get_dict_data(file)

fieldnames = []
for i in range(len(list_csv[0])):
    fieldnames.append(list_csv[0][i])

with open('lesson7_1.csv', 'w', encoding='utf-8') as f:
    writer = csv.DictWriter(f, delimiter = ';', fieldnames = fieldnames)
    writer.writeheader()
    for i in range(len(dict_csv)):
        writer.writerow(dict_csv[i])

csv_time = dt.datetime.now() - start_time

print('Файл создан, время затраченное на выполнение: ', csv_time)
