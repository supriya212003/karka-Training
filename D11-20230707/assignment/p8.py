name=input("Hey,what's your name?")
age=int(input("ok,{}.How old are you?".format(name)))
if age<16:
    print("You can't drive",name,"\nYou can't vote,",name,"\nYou can't rent a car,",name)
elif age<18:
    print("You can't vote,{}\nYou can't rent a car,{}".format(name,name))
elif age<25:
    print("You can't rent a car,",name)
else:
    print("You can do anything that's legal,",name)