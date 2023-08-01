user_detail=[{"name":"agalya",
              "email_id":"agal03@gmail.com",
              "password":"agal03",
              "hobbies":["sketching","dancing"],
              "friends_list":["renu","ashika","rathi"]
              },
              {"name":"thanu",
              "email_id":"thanu02@gmail.com",
              "password":"thanu02",
              "hobbies":["singing","dancing"],
              "friends_list":["ashwathi","nizy","ruby"]
              },
              {"name":"meha",
              "email_id":"meha23@gmail.com",
              "password":"1234",
              "hobbies":["sketching","gardening"],
              "friends_list":["samyuktha","ramya","renisha","mathumitha"]
              }
              ]
# print(user_detail)
email_id=input("enter your email:")
password=input("enter the password:")
def user_list(lists):
    a=""
    for j in lists:
        separator=","
        a+=j+separator
    return a
for i in user_detail:
    
    if email_id==i["email_id"] and password==i["password"]:
        print("login successful!")
        i.update({"login":"true"})
        n=i["name"]
        print("welcome ",n)
        h=i["hobbies"]
        print("your hobbies are:",user_list(h))
        frnds=i["friends_list"]
        print("your friends are:",user_list(frnds))
                
    else:
        i.update({"login":"false"})







# print(user_detail)


        
