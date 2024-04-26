a = [4,6]
b=[]
print(a[1])
for i in range(len(a)):
    for j in range(i):
    #print(i)
        b.append(a[i])
print(b)