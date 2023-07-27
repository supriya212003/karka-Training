from datetime import datetime,date
from datetime import timedelta
a=datetime.now()
n=int(input("enter the days:"))
f=a+timedelta(n)
print(f)