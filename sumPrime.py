a = [67,24,58,28,71,73,99]
print(min(a))
b = [x for x in range(min(a), max(a)+1) if all(x % y != 0 for y in range(2, x))]
d=[]
for i in range()
for i in b:
if a==i:
        d.append(i)
print(d)
# c= 0
# for i in b:
#     c += i
# print(c)