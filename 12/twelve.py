#https://projecteuler.net/problem=12
import math

def count_divisors(n):
    d = 0
    i = 1
    rt = int(math.sqrt(n))
    while i<rt:
        if n%i == 0:
            d+=1
        i+=1
    d*=2    
    if 1.*n/rt == rt:
        d+=1
    return d

j=1
while True:
    tri = (j*(j+1))/2      #sum(range(1,j+1))
    cdtri = count_divisors(tri)
    if cdtri > 500:
        print j, tri, cdtri        
        break
    j+=1

#solution: 12375 76576500 576
