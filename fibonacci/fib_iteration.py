a = 0
b = 1
n = raw_input("enter Nth : ")
for i in range(1,int(n)+1):
	i = b
	print i
	c = a + b
	a, b = b, c
