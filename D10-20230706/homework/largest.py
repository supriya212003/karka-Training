numbers=[1,100,300,4]
largest=0
def great(numbers,largest):
    for number in numbers:
        if number>largest:
            largest=number 
    return largest

print(great(numbers,largest))

