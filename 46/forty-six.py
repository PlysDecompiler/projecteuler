#https://projecteuler.net/problem=46
import math

primes = [2]
num = 3

def prime(i):
    return True if all(i%n for n in primes if n <= math.sqrt(i)) else False

#run over the odd numbers and add them either to prime or check through subtracting double squares that the substracted composite ones are not in prime
while True:
    p = prime(num)
    if p:
        primes.append(num)
    else:
        a = 1
        while num-2*a**2 > 2:
            s = num-2*a**2
            if s in primes:
                break
            a+=1
        else:
            print num
            break
    num+=2

#solution: 5777
