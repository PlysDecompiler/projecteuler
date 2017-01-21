#https://projecteuler.net/problem=27
import math

def is_prime(i):
    return True if all(i%n for n in range(2,int(math.sqrt(i))+1)) else False

consecs = {}

for a in range(-1000,1001):
    for b in range(-1000,1001):
        n=0        
        while True:
            eq = n**2+a*n+b
            if eq > 1:
                if is_prime(eq):
                    n+=1
                else:
                    if n>5:
                        consecs[(a,b)] = n
                    break
            else:
                break

maxlist = sorted(consecs.keys(), key=lambda k: consecs[k])
print maxlist[-1], consecs[maxlist[-1]]
print maxlist[-1][0]*maxlist[-1][1]

#solution: -59231
