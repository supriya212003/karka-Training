venus=0.78
mars=0.39
jupiter=2.65
saturn=1.17
uranus=1.05
neptune=1.23
weight=float(input("Please enter your current earth weight:"))
print("I have information about the following planets")
print("\t 1.venus  \t 2.Mars  \t 3.Jupiter")
print("\t 4.saturn  \t 5.uranus  \t 6.neptune")
planet=int(input("Which planet are you visiting?"))
if planet==1:
    gravity1=weight*venus
    print("Your weight would be",gravity1,"pounds on that planet")
elif planet==2:
    gravity2=weight*mars
    print("Your weight would be",gravity2,"pounds on that planet")
elif planet==3:
    gravity3=weight*jupiter
    print("Your weight would be",gravity3,"pounds on that planet")
elif planet==4:
    gravity4=weight*saturn
    print("Your weight would be",gravity4,"pounds on that planet")
elif planet==5:
    gravity5=weight*uranus
    print("Your weight would be",gravity5,"pounds on that planet")
elif planet==6:
    gravity6=weight*neptune
    print("Your weight would be",gravity6,"pounds on that planet")