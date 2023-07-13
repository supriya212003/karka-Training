gender=input("What is your gender(M or F):")
fir_name=input("First name:")
last_name=input("Last name:")
age=int(input("Age:"))
if age>20 and gender=="F":
    marry=input("Are you married,{}(yes or no)?".format(fir_name))
    if marry=="yes":
        print("Then I should call you Mrs.",fir_name)
    else:
        print("Then I should call you Ms.",fir_name)
elif age<20 and gender=="F":
    print("Then I should call you",fir_name+last_name)
elif age>20 and gender=="M":
    print("Then I should call you Mr.",fir_name)
else:
    print("Then I should call you",fir_name+last_name)

