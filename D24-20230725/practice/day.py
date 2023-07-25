from datetime import datetime
from pytz import timezone
dt=datetime(2023,7,25,12,32,46)
print(dt)
# seoul=pytz.timezone()

c=datetime.now(timezone("UTC"))
print("c",c)
f=c.strftime("%Y")
print(f)
# d=date(2023,7,25)
# print(d)
# day=date.today().day
# print(day)
# t=time(12,19,43)
# print(t)