#https://projecteuler.net/problem=47
import math
import time
primes = [2]
num = 3
start = time.time()

def prime(i):
    return True if all(i%n for n in primes if n <= math.sqrt(i)) else False

consec = []

while True:
    if prime(num):
        primes.append(num)
        num+=1
        consec = []
        continue
    if sum([1 if num%p==0 else 0 for p in primes]) == 4:
        consec.append(num)
        if len(consec) == 4:
            print consec[0]
            break
    else:
        consec = []

    num+=1

print time.time()-start
#solution: 134043
