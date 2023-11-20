l1=[[1,2,3],
    [4,5,6],
    [7,8,9]]

l2=[]

for i in range(len(l1[0])):
    row=[]
    for j in range(len(l1)):
        row.append(l1[j][i])
    l2.append(row)
    
print(l2)