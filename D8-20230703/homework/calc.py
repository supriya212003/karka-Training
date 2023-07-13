num1=int(input("Enter the first number:"))
operator=(input("Enter the operator"))
num2=int(input("Enter the second number:"))
def calc(num1,operator,num2):
    if operator=="+":
        return(num1+num2)
    elif operator=="-":
        return(num1-num2)
    elif operator=="*":
        return(num1*num2)
    elif operator=="%":
        return(num1%num2)
    else:
        return 0
result=calc(num1,operator,num2)
print(result)
    