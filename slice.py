# a = 'aaabbbccc'

# print(a[::-1])

def palindrome(a):
    return a == a[::-1]

print(palindrome('malam malam'))