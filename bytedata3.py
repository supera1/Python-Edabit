import sys
from os import strerror


try:
    bf = open('file3.bin', 'rb')
    data = bytearray(bf.read())
    bf.close()

    for b in data:
        print(hex(b), end=' ')

except IOError as e:
    print("I/O error occurred:", sys.stderr.write("File tidak ditemukan"))

