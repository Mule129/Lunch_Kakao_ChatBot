import datetime as dt

date = str(dt.date.today()).split("-")[:2]
print(*date)
d = date[0]+date[1]
print(d)