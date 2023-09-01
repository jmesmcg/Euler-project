import math
isPrime = True
n = int(input(""))
if(n%2 == 0):
    isPrime = False
for r in range(1,n):
    if(math.factorial(n)/(math.factorial(r)*math.factorial(n-r)))% n != 0.0:
        isPrime = False
    break

print(isPrime)

