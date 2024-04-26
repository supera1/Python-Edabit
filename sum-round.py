def sum_round(num):
	d = len(str(num))
	e=[]
	for i in range(d):
		b = num%10
		num = int(num/10)
		e.append(b)
	f=[]
	for x,y in enumerate(e):
		f.append(y*(10**x))
	fin=[]
	for value in f:
		if (value !=0) :
			fin.append(value)
	return " ".join(str(t) for t in fin)

print(sum_round(123456))