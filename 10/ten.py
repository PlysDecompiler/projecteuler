#https://projecteuler.net/problem=10
import math

primes = [2,3]
def is_prime(i):
    return True if all(i%n for n in range(2,int(math.sqrt(i))+1)) else False
num = 5
while num < 2000000:
    if is_prime(num):
        primes.append(num)    
    num+=2

print sum(primes)
#solution: 142913828922
