#https://projecteuler.net/problem=39
import math

start = 1
maxsize = 0
maxp = start

for p in range(start,1001):
    sides = set()
    a = 1
    while a<p/3:
        b = a 
        while True:            
            c = math.sqrt(a**2+b**2)
            if a+b+c > p:
                break
            if a+b+c == p:
                sides.add((a,b,c))
            b += 1
        a += 1
    if len(sides) > maxsize:
        maxsize = len(sides)
        maxp = p

print maxsize, maxp
#solution: 840
