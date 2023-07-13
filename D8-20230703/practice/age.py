age=int(input("Enter your age"))
def eligible(age):
    if age>=18:
        return "you are eligible"
    else:
        return "you are not eligible"
result=eligible(age)
print(result)