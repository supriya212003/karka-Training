from datetime import datetime,date
from datetime import timedelta
n=int(input("enter the number of days:"))
d=input("enter the day:")
e=datetime.strptime(d,"%d %B %y")
f=e+timedelta(n)
print(f)