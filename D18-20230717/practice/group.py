group=[
        {   "name":"vajeeha",
            "age":22,
            "place":"thittuvilai",
            "mark_10":{"tamil":78,"english":89,"maths":67,"science":78,"social":90}
        },
        ]
for person in group:
    # print(group)
    mark=(person["mark_10"])
    m1=mark["tamil"]
    m2=mark["english"]
    m3=mark["maths"]
    m4=mark["science"]
    m5=mark["social"]
    total=m1+m2+m3+m4+m5
    leb = len(person["mark_10"].values())
    print("leb",leb)
    percentage=(total/(leb*100))*100
    print(percentage)
    math=person["mark_10"]["maths"]
    

    if percentage>90 or (percentage>75 and math>98):
        print("Eligible for maths biology!")
    elif percentage>80 or (percentage>70 and math>98):
        print("Eligible for computer science!")
    else:
        print("not eligible for maths biology or computer science!")  

    