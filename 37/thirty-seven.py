#https://projecteuler.net/problem=37
import math

def prime(i):
    return False if i==1 else (True if all(i%n for n in range(2,int(math.sqrt(i))+1)) else False)

truncatable = []
i=11
while len(truncatable)<11:
    n = str(i)
    if n[0] in '1468':
        i+= 10**(len(n)-1)
        continue
    if prime(i):
        if all(prime(int(n[j:])) and prime(int(n[:-j])) for j in range(1,len(n))):
            truncatable.append(i)
            print i
    i+=2
print sum(truncatable)
#solution: 748317
