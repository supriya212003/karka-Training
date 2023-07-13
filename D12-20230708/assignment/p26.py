print("ye olde keychain shop")
a="1.Add keychains to order"
b="2.Remove keychains to order"
c="3.View current order"
d="4.Checkout"
print(a,"\n",b,"\n",c,"\n",d)

def add_keychain():
    print("ADD KEYCHAINS")
    print(a,"\n",b,"\n",c,"\n",d)
    
    
    
    
def remove_keychain():
    print("REMOVE KEYCHAINS")
    print(a,"\n",b,"\n",c,"\n",d)
    
    
    
def view_order():
    print("VIEW ORDER")
    print(a,"\n",b,"\n",c,"\n",d)    
    
def checkout():
    print("CHECKOUT")
    print(a,"\n",b,"\n",c,"\n",d)
    
    
    

# for i in range(15):
#     print(i)
#     choice=input("Please enter your choice:")
#     if choice=='1':
#         add_keychain()
#     if choice=='2':
#         remove_keychain()
#     if choice=='3':
#         view_order()
#     elif choice=='4':
#         checkout()
#         break
choice=input("Please enter your choice:")
while choice<'4':
    choice=input("Please enter your choice:")

    print(choice)
    if choice=='1':
        add_keychain()
    if choice=='2':
        remove_keychain()
    if choice=='3':
        view_order()
    elif choice=='4':
        checkout()
        break