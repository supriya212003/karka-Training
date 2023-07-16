friends=[{"name":"vajeeha","age":22,"place":"thittuvilai"},
    {"name":"supriya","age":22,"place":"ganesapuram"},
    {"name":"valli","age":21,"place":"Krishnankovil"},
    {"name":"srivarthanan","age":20,"place":"swamithoppu"},
    {"name":"sreeram","age":20,"place":"thamarai kulam"},
    {"name":"subin","age":20,"place":"parvathipuram"},
    {"name":"robin","age":22,"place":"tirunelveli"}]
    
def details(friends):
    for friend in friends:
        name=friend["name"]
        age=friend["age"]
        place=friend["place"]
        print(f"I am {name},I'm {age} years old and I'm from {place}.")
# details(friends)


def age_21(friends):
    for friend in friends:
        name=friend["name"]
        age=friend["age"]
        place=friend["place"]
        if friend["age"]>21:
            print(f"I am {name},I'm {age} years old and I'm from {place}.")
# age_21(friends)



if details(friends):
    details(friends)
elif age_21(friends):
    age_21(friends)

