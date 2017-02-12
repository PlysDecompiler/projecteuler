#https://projecteuler.net/problem=50
import math
import bisect

primes = [2]

def prime(i):
    rt = math.sqrt(i)
    for p in primes:
        if p > rt:
            return True
        if i % p == 0:
            return False
    return True

for n in range(3, 1000000, 2):
    if prime(n):
        primes.append(n)

top = [p for p in primes if p>100000]
maxi = 0
maxprime = 0
t = top[0]
j = bisect.bisect(primes, t)

k = 1
while True:
    if k > j or j<2:
        break
    s = sum(primes[j-k:j])
    if s > top[-1]:
        j -= 1
        k = 1
        continue
    if s in primes:
        if k > maxi:
            maxi = k
            maxprime = s
            print j, k, maxi, maxprime
    k+=2

print maxi, maxprime

#solution: 997651
