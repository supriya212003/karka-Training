from datetime import datetime
now=datetime.now()
print(now)
yr=now.strftime("%Y")  #Y->year 2023
print(yr)
year=now.strftime("%y") #y->year 23
print(year)
day=now.strftime("%d") #d->day 21
print(day)
dy=now.strftime("%D") #D->date 05/21/2003
print(dy)
mon=now.strftime("%m") #m->month
print(mon)
m=now.strftime("%M") #M->minute
print(m)
sec=now.strftime("%S") #S->seconds
print(sec)
hr=now.strftime("%H") #H->hour
print(hr)
month=now.strftime("%h") #h->month in short jul
print(month)
s=now.strftime("%s") #
print(s)