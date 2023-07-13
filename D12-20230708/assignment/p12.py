ready=input("Are you ready for a quiz?")
print("Okay,here it comes!")
n=0
q1=int(input("What is the capital of alaska?\n\t1)Melbourne\n\t2)Anchorage\n\t3)Juneau\n>"))
if q1==3:
    print("That's right!")
    n=n+1
else:
    print("Sorry,that's Incorrect")
q2=int(input("Can you store the value cat in a variable of type int?\n\t1)Yes\n\t2)No\n>"))
if q2==2:
    print("That's right!")
    n=n+1
else:
    print("Sorry,cat is a string.It's can only store numbers.")
q3=int(input("What is the result of 9+6/3\n\t1)5\n\t2)11\n\t3)15/3\n>"))
if q3==2:
    print("That's right!")
    n=n+1
else:
    print("Sorry,that's Incorrect")
print(n)
print("Overall,you got",n,"out of 3 correct.\nThanks for playing!")

