num1 = 0
num2 = 0
i = 1
while i < 1000000:
    n = i
    t = 1
    while 1:
        if n % 2 == 0:
            n = n / 2
        else:
            n = n * 3 + 1
        t += 1
        if n == 1:
            break
    if t > num2:
        num2 = t
        num1 = i
    i+=1
print (num1)
