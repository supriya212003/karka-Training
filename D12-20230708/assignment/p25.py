month_number=int(input("number:"))
def month_name(month_number):
    if month_number==1:
        j=f"number{month_number}:January"
        return j
    elif month_number==2:
        f=f"number{month_number}:February"
        return f
    elif month_number==3:
        m=f"number{month_number}:March"
        return m
    elif month_number==4:
        a=f"number{month_number}:April"
        return a
    elif month_number==5:
        z=f"number{month_number}:May"
        return z
    elif month_number==6:
        x=f"number{month_number}:June"
        return x
    elif month_number==7:
        b=f"number{month_number}:July"
        return b
    elif month_number==8:
        a=f"number{month_number}:August"
        return a
    elif month_number==9:
        s=f"number{month_number}:September"
        return s
    elif month_number==10:
        o=f"number{month_number}:October"
        return o
    elif month_number==11:
        n=f"number{month_number}:November"
        return n
    elif month_number==12:
        d=f"number{month_number}:December"
        return d
    else:
        return 0
print(month_name(month_number))
# result=month_name(month_number)
# print(result)

     