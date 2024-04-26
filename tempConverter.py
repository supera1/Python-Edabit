def converter(a,b):
    if a[0]=='fahrenheit' and b=='kelvin':
        return round((a[1] + 459.67) * 5/9,1)
    elif a[0]=='fahrenheit' and b=='celsius':
        return round((a[1]-32) / 1.8,1)
    elif a[0]=='celsius' and b=='fahrenheit':
        return round((a[1] * 1.8) + 32 ,1)
    elif a[0]=="celsius" and b=="kelvin":
        return round(a[1] + 273.15 ,1)
    elif a[0]=="kelvin" and b=="fahrenheit":
        return round((a[1] * 9/5) - 459.67 ,1)
    elif a[0]=="kelvin" and b=="celsius":
        return round(a[1] - 273.15 ,1)


print(converter(["kelvin", -10], "celsius"))        