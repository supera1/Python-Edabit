def caesarchip(text,a):
    cipher = ''
    if (a > 25) or (a < 1):
        return "enter value between 1-25"
    for char in text:
        if not char.isalpha():
            return "dont enter numnber"
        char = char.upper()
        code = ord(char) + a
        if code > ord('Z'):
            code = ord('A')
        cipher += chr(code)
    return cipher

print(caesarchip("agfkgfrjkhfd", 6))