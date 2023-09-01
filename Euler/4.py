def pal(string):
	isCorrect=True
	i=0
	while i<=int(len(string)/2) and isCorrect==True:
		if string[i]!=string[-(i+1)]:
			isCorrect=False
		i+=1
	return isCorrect


ans=0
for k in range(101,1000):
    for j in range(101,1000):
        if pal(str(j*k)) and j*k>ans:
                    ans=j*k


print (ans)
