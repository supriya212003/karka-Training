passed_out_yr=input("which year passed out from college")
print(passed_out_yr)
#type_of_passed_out_yr=type(passed_out_yr)
#print(type_of_passed_out_yr)
passed_out_yr=int(passed_out_yr)
cgpa=input("cgpa:")
is_eligible=passed_out_yr==2022 or passed_out_yr==2023
if is_eligible:
    print("come to session")
else:
    print("do not come to session")
is_eligible=passed_out_yr==2022 and cgpa==7
if is_eligible:
    print("eligible for pay after placement")
else:
    print("not eligible")