data = bytearray(257)
print(type(data))
print(len(data))
for i in range(len(data)):
    data[i] = 257 - i

for b in data:
    print(hex(b))