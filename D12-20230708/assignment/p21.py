height=float(input("Your height in m:"))
weight=float(input("Your weight in kg:"))
def bmi_calc(height,weight):
    return weight/height**2
#bmi_calc=weight/(height*height)
print("Your BMI is",bmi_calc(height,weight))
if bmi_calc(height,weight)<18.5:
    print("BMI category=under weight")
if bmi_calc(height,weight)>18.5 and bmi_calc(height,weight)<24.9:
    print("BMI category=normal weight")
if bmi_calc(height,weight)<25.0 and bmi_calc(height,weight<29.9):
    print("BMI category=over weight")
if bmi_calc(height,weight)>30:
    print("BMI category=obese")