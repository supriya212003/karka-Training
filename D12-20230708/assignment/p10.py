name=input("Hey,what's your name?(Sorry,I keep forgetting.)")
age=int(input(f"ok,{name},how old are you?"))
if age<16:
    print("You can't drive")
elif age==16 or age==17:
    print("You can drive but don't vote")
elif age>=18 and age<=24:
    print("You can vote but not rent a car")
else:
    print("You can do pretty much anything")