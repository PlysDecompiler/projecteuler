#https://projecteuler.net/problem=7

import math

def is_prime(i):
    return True if all(i%n for n in range(2,int(math.sqrt(i))+1)) else False

num = 5
primes = [2,3]
while len(primes)<=10001:
    if is_prime(num):
        primes.append(num)    
    num+=2

print primes[10000]
#solution = 104743
