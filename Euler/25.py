a,b,c = 0,1,1
while True:
	a,b,c=b,a+b,c+1
	if b >= 10**999:
		print (c)
		break
