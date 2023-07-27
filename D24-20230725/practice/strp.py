from datetime import datetime
from datetime import timedelta
date="21 May 03"
print(type(date))
s=datetime.strptime(date,"%d %B %y")
a=timedelta(days=5,seconds=27)
print(type(s))
print(s)
print(a)