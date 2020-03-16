l=[1,5,2,1,8,7,2,5,3,7,8,1]
l2=[]
for i in  l:
    if i not in l2:   # checking i is not in list.
        l2.append(i)

print(l2) # output.