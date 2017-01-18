#https://projecteuler.net/problem=24
from itertools import permutations

li = [str(i) for i in range(10)]
perm = list(permutations(li))

print ''.join(perm[999999])
#solution: 2783915460
