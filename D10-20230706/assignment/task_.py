
numbers=[1,43,8]
num=0
enum_numbers=enumerate(numbers)
print(type(enum_numbers))
for i,number in enum_numbers:
    print("entering the process of item1:"+str(1))
    print("before sum",number)
    num=num+number
    print("after numbers",number)
    print("existing the process of item1:"+str(1))
    print("\n")