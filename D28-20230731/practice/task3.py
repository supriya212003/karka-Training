d=[1,0,3,0,9,13]
for i in d:
    if i==0:
        d.remove(0)
        d+=[0]
        
print(d)