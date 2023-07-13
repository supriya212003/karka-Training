height=float(input("Your height in m:"))
weight=float(input("Your weight in kg:"))
def bmi_calc(height,weight):
    return weight/height**2
# bmi_calc=weight/(height*height)
print("Your BMI is",bmi_calc(height,weight))