def caesarchip(a):
    text = input("Enter a number = ")
    cipher = ''
    while not ((a > 25) or (a < 1)):
        print("enter value between 1-25")
        text = input("Enter a number = ")
    for char in text:
        while not (char.isalpha()):
            print("dont enter numnber")
            text = input("Enter a number = ")
        char = char.upper()
        code = ord(char) + a
        if code > ord('Z'):
            code = ord('A')
        cipher += chr(code)
    return cipher

print(caesarchip(6))