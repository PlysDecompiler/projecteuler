#https://projecteuler.net/problem=49
from itertools import permutations
import math

primes = [2]
def prime(i):
    return True if all(i%n for n in primes if n <= math.sqrt(i)) else False

for n in range(3, 10000, 2):
    if prime(n):
        primes.append(n)

primes = [p for p in primes if p > 1000]
found = 0

for p in primes:
    if found == 2:
        break
    perms = list(set([int(''.join(perm)) for perm in permutations(str(p))]))
    perms.remove(p)
    for perm in perms:
        if perm in primes:
            third = perm+(perm-p) 
            if third in perms and third in primes:
                print str(p)+str(perm)+str(third)
                found += 1
                break   

#solution: 296962999629
