year=input("Enter the year:")
year=int(year)
if (year%4==0 and year%100!=4) or year%400==0:
    print(year,"is a leap year")
else:
    print(year,"is not a leap year")