#https://projecteuler.net/problem=58
import math

def is_prime(i):
    for j in range(2,int(math.sqrt(i))):
        if i%j == 0:
            return False
    return True

def topleft(n): return 4*n**2-8*n+5;
def topright(n): return 4*n**2-10*n+7;
def bottomleft(n): return 4*n**2-6*n+3;

it = 5
prime = 8
every = 13.

while True:
    if is_prime(topleft(it)):
        prime+=1
    if is_prime(bottomleft(it)):
        prime+=1
    if is_prime(topright(it)):
        prime+=1
    every+=4.
    if prime/every < 0.1:
        print 2*it-1
        break
    
    it+=1

#solution: 26241
