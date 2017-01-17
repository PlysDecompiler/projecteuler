#https://projecteuler.net/problem=23
import math

def sum_prop_divisors(n):
    li = set()
    rt = int(math.sqrt(n))
    for i in range(2,rt+1):
        if n%i == 0:
            li.add(i)
    for i in list(li):
        li.add(n/i)
    li.add(1)
    return sum(li)

abundance = []
for i in range(2,28124):
    if sum_prop_divisors(i) > i:
        abundance.append(i)

s = 0
for i in range(1,28124):
    ended = False    
    for j in abundance:
        if j>i:
            ended = True
            break
        if (i-j) in abundance:
            break
    else:
        ended = True
    if ended:
        s+=i

print s
#solution: 4179871
