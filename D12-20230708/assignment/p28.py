current=0
price=10
sales_tax=8.25
cost_per_order=5
per_keychain_cost=1


def add_keychain():
    global current
    add=int(input(f"You have {current} keychains.How many to add?:"))
    current+=add
    return f"You now have {current} keychains."
def remove_keychain():
    global current
    remove=int(input(f"You have {current} keychains.How many to to remove?:"))
    current-=remove
    return f"you now have {current} keychains."
def view_order():
    global current
    global price
    
    return f"You have {current} keychains.\nKeychain cost ${price} per each.\nTotal cost is {(current*price)+((per_keychain_cost*current)+cost_per_order)+((current*price)*(sales_tax/100))}"

    # total=current*price
    # return total
def checkout():
    global current
    global price
    name=input("What is your name?:")
    print(f"Thank you {name} for ordering!")
    return f"you have {current} keychains.\nKeychain cost ${price} each.\nTotal cost is ${(current*price)+((per_keychain_cost*current)+cost_per_order)+((current*price)*(sales_tax/100))}"

    
    # print(f"Thank you {name} for ordering!")
    print("checkout")

for i in range(7):
    print(" old keychain shop\n1.Add keychains to order\n2.Remove keychains to order\n3.View current order\n4.Checkout")
    choice=input("Please enter your choice:")-
    
    
    if choice=='1':
        print(add_keychain())
    elif choice=='2':
        print(remove_keychain())
    elif choice=='3':
        print(view_order())
    elif choice=='4':
        print(checkout())
        break