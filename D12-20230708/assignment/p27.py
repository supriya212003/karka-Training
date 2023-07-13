current=0
price=10
# print=input(" old keychain shop\n1.Add keychains to order\n2.Remove keychains to order\n3.View current order\n4.Checkout")

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
    return f"You have {current} keychains.\nKeychain cost ${price} per each.\nTotal cost is {current*price}"
    # total=current*price
    # return total
def checkout():
    global current
    name=input("What is your name?:")
    return f"you have {current} keychains.\nKeychain cost ${price} each.\nTotal cost is ${price*current}"
    view_order(current,price)
    print("Thank you",name,"for ordering!")
    print("checkout")

for i in range(7):
    print=input(" old keychain shop\n1.Add keychains to order\n2.Remove keychains to order\n3.View current order\n4.Checkout")
    choice=input("Please enter your choice:")
# while choice<'4':
    # print("1.Add keychains to order")
    # print("2.Remove keychains to order")
    # print("3.View current order")
    # print("4.Checkout")
    # choice=input("Please enter your choice:")
    
    if choice=='1':
        add_keychain()
    elif choice=='2':
        remove_keychain()
    elif choice=='3':
        view_order()
    elif choice=='4':
        checkout()
        break