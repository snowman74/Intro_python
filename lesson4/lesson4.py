


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