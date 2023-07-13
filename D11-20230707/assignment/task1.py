# # numbers=[34,6,9,7,2]
# # print(len(numbers))
# # sum=0
# # for values in numbers:
# #     sum=sum+values
# # print(sum)
# # average=sum/len(numbers)
# # print(average)
numbers=[1,43,8]
num=0
# for number in numbers:
#     print("before",num)
#     num=num+number
#     print("after",num)
enum_numbers=enumerate(numbers)
print(type(enum_numbers))
for i,number in enum_numbers:
    print("entering the process of item1:"+str(1))
    print("before sum",number)
    num=num+number
    print("after numbers",number)
    print("existing the process of item1:"+str(1))
    print("\n")