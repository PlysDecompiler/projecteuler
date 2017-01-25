#https://projecteuler.net/problem=32
import math

unusual = set()
digits = '123456789'

def isunusual(s):
    return all(d in s for d in digits)

for i in range(1000,100000):
    for j in range(1,int(math.sqrt(i))+1):
        if not i%j:
            k = i/j
            s = ''.join([str(n) for n in [i,j,k]])
            if len(s) == 9:
                if isunusual(s):
                    unusual.add(i)

print len(unusual), sum(unusual) 
#45228
