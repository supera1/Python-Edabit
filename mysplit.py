def mysplit(sentence):
    split_value = []
    tmp = ''
    for c in sentence:
        if c == ' ':
            split_value.append(tmp)
            tmp = ''
        else:
            tmp += c
    if tmp:
        split_value.append(tmp)
    return split_value

print(mysplit('Python Programming tutorial'))