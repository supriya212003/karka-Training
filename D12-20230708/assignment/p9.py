day=int(input())
def weekday(day):
    if day==1:
        d="Sunday"
        return d
    elif day==2:
        d="Monday"
        return d
    elif day==3:
        d="Tuesday"
        return d
    elif day==4:
        d="Wednesday"
        return d
    elif day==5:
        d="Thursday"
        return d
    elif day==6:
        d="Friday"
        return d
    elif day==7 or day==0:
        d="Saturday"
        return d
    else:
        d="error"
        return d
print(f"Weekday {day}:{weekday(day)}")
print("Today is a {}!".format(weekday(day)))