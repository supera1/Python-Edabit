class nomor:
    def __iter__(self):
        self.a = 1
        return self

    def __next__(self):
        if self.a <= 30:
            x = self.a
            self.a += 1
            return x
        else:
            raise StopIteration

kelas1 = nomor()
myiter = iter(kelas1)

# print(next(myiter))
# print(next(myiter))
# print(next(myiter))

for i in myiter:
    print(i)

for j in range(30):
    print(j+1)
