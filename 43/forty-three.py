#https://projecteuler.net/problem=43
from itertools import permutations

alldigits = '0123456789'
divisors = [2,3,5,7,11,13,17]
perms = [''.join(perm) for perm in permutations(alldigits)]
pandivs = []

for num in perms:
    if all([int(num[i+1:i+4])%divisors[i] == 0 for i in range(7)]):
        pandivs.append(int(num))

print len(pandivs), sum(pandivs)
#solution: 16695334890
