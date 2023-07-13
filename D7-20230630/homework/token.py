item1=int(input("Enter the amount of item1="))
item2=int(input("Enter the amount of item2="))
item3=int(input("Enter the amount of item3="))
item4=int(input("Enter the amount of item4="))
sum=item1+item2+item3+item4
if 500<=sum<=1000:
    print("Congrats,You have owned a Silver Token!")
elif sum>1000:
    print("Congrats,You have owned a Golden Token!")
else:
    print("Thanks for purchasing!")
