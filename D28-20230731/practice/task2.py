d=[1,5,3,7,9,13]
for i in range(len(d)):
    for j in range(i+1,len(d)):
        if d[i]+d[j]==10:
            print([i,j])