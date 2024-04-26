import math

# n=5
# a=1
# for i in range(1,n+1):
#     a *= math.factorial(int(i))
# print(a)
def fact_of_fact(n):
    a=1
    for i in range(1,n+1):
        a *= math.factorial(int(i))
    return a        
   

print(fact_of_fact(5))