file=open("/home/supriya/Documents/karka.txt","a")
# print(file)
# for line in file:
#     print(line)
# data =file.read()
# print(data)
file.write("vajeeha from thittuvilai\n she like berry")
file.close()
file=open("/home/supriya/Documents/karka.txt","r")


# data=file.read()
# print(data)
for line in file:
    print(line.split())