def fun(n):
    for i in range(n):
       yield i

for i in fun(5):
    print(i)   
print([i for i in fun(5)])
print(type(fun(5)))