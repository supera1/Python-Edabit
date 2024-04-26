def adds_n(n):
    return lambda x: n + x
    

a = adds_n(1)
b = adds_n(-5)
print(b(10))
# def make_incrementor(n):
#     return lambda x: x + n

# f = make_incrementor(42)
# print(f(3))

# def adds_n(n):
# 	return lambda x: x + n