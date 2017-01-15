#https://projecteuler.net/problem=21
import math

def list_prop_divisors(n):
    li = set()
    rt = int(math.sqrt(n))
    for i in range(2,rt+1):
        if n%i == 0:
            li.add(i)
    for i in list(li):
        li.add(n/i)
    li.add(1)
    return li

di = {}
for i in range(2,10000):    
    di[i] = sum(list_prop_divisors(i))

amicable = set()
for k in di.keys():
    if di[k] in di and di[di[k]] == k and k!=di[k]:
        amicable.add(k)

print sum(amicable)
#solution: 31626
