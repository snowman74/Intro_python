import json, time, datetime as dt

start_time = dt.datetime.now()

file = 'weapon.txt'


def get_dict_data(file):  # возвращает словарь аргументов
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

    return dict_temp


temp_dict = get_dict_data(file)

dict_to_json = json.dumps(temp_dict)
with open('lesson7_json.txt', 'w', encoding='utf-8') as f:
    json.dump(temp_dict, f)

json_time = dt.datetime.now() - start_time

print('Файл создан, время затраченное на выполнение: ', json_time)

with open('lesson7_json.txt') as f:
    data = json.load(f)



data_1 = json.loads(dict_to_json)


