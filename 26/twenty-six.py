#https://projecteuler.net/problem=26
import math
from decimal import * 
getcontext().prec = 2000
d = 999

def recurring(s):   
    i = 1
    while i < 0.5*(len(s)+1):             
        if all([s[0:i]==s[j*i:(j+1)*i] for j in range(1,len(s)/i)]):
            return i
        i+=1
    return False    

def is_prime(i):
    return True if all(i%n for n in range(2,int(math.sqrt(i))+1)) else False

while d>1:
    if is_prime(d):
        s = str(Decimal(1)/Decimal(d))[2:] 
        r = recurring(s) 
        if r:
            print d,r
            if recurring(s) == d-1:
                print d, len(s), recurring(s)
                break
    d-=1

#(primes tend to have a recurring series length of just 1 below their amount. I test through the prime numbers from above, so it is the maximum. no)
#solution: 983
