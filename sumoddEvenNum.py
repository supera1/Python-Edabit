def sum_odd_and_even(lst):
    a=[]
    b=[]
    for i in lst:
        if i%2 ==0 :
            a.append(i)
        else:
            b.append(i)
    return [sum(a),sum(b)]
     #   elif i%2 !=0:
     #       b.append(i)
     #   return b

print(sum_odd_and_even([1, 2, 3, 4, 5, 6]))

print(sum_odd_and_even([-1, -2, -3, -4, -5, -6]))

print(sum_odd_and_even([0, 0]))
print(sum_odd_and_even([]))
    

            