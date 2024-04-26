def ganjil(angka):
    for a in range(angka):
        if (a % 2 !=0):
            yield a

def ganjil2(angka):
    b=[]
    for a in range(angka):
        if (a % 2 !=0):
            b.append(a)
    return b

bil_ganjil = ganjil(20)

# print(type(bil_ganjil))
# for i in bil_ganjil:
#     print(i)

print(ganjil2(20))

# print([i for i in bil_ganjil])