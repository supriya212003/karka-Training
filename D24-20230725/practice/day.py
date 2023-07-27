from datetime import datetime
import pytz

dt=datetime(2023,7,25,12,32,46)
print(dt)
dt1=datetime.now()
print(dt1)
dt2=datetime.now(pytz.utc)
print(dt2)
c=datetime.now(pytz.timezone("Europe/Vienna"))
print(c)
f=c.strftime("%Y")
print(f)
print(type(f))
