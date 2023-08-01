#fibonacci series
num1=0
num2=1
for i in range(0,5):
    print(num1)
    num3=num1+num2
    num1=num2
    num2=num3

#remove no and replace with symbols
lst=[2,3,2,3]
n=int(input("no:"))
for i in range(len(lst)):
    if lst[i]==n:
        lst[i]='*'
print(lst)

#to check using not in and get fn
dic={"name":"shalu",
     "age":22}
if "name" not in dic:
    print("yes")
else:
    print("no")

if dic.get("name")==None:
    print("not present")

else:
    print("present")
