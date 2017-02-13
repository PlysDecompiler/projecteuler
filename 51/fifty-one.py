#https://projecteuler.net/problem=51
import math
from itertools import combinations

primes = [2]

def prime(i):
    rt = math.sqrt(i)
    for p in primes:
        if p > rt:
            return True
        if i % p == 0:
            return False
    return True

for p in range(3, 10000000, 2):
    if prime(p):
        primes.append(p)

#find necessary combinations of digits that should be replaceable
numd = {}
combs = []
for v in range(2,6):
    combs.extend([[int(i) for i in tup] for tup in combinations('234567',v)])
for c in combs:
    mc = max(c)
    if mc not in numd:
        numd[mc] = []
    numd[mc].append(c)

primes = [p for p in primes if p>100]

#setting up a dictionary that gets filled with patterns of X'ed numbers
patterns = {}

found = False
for p in primes:
    if found:
        break
    s = str(p)
    l = len(s)
    for r in range(3,l+1):
        for tup in numd[r]:
            if all(s[-tup[0]]==s[-tup[i]] for i in range(1,len(tup))):
                pat = list(s)
                for i in range(len(tup)):
                    pat[-tup[i]]='X'
                pat = ''.join(pat)
                if pat not in patterns:
                    patterns[pat] = 0
                patterns[pat]+=1
                if patterns[pat] == 8:
                    found = pat
                    break
                    
#finding the smallest number with the found pattern
if found:
    for j in range(3):
        if int(found.replace('X',str(j))) in primes:
            print int(found.replace('X',str(j)))
            break

#solution: 121313                
