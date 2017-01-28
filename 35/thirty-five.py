#https://projecteuler.net/problem=35
import math

circprime = set()

def is_prime(i):
    return True if all(i%n for n in range(2,int(math.sqrt(i))+1)) else False

rng = range(3,100000)
for r in range(5):
    #only check numbers over 100000 that begin with 1,3,5,7,9
    rng.extend(range(100000+200000*r,200000+200000*r))
#check whether there are any 2,4,6,8,0 in str(num)
nope = '02468'

for num in rng:
    if any([n in str(num) for n in nope]):
        continue
    if is_prime(num):
        snum = str(num)
        if all([is_prime(int(snum[k:]+snum[:k])) for k in range(1,len(snum))]):
            circprime.add(num)

print len(circprime)+1 #(+1 because 2 is not counted in the list)
print circprime
#solution: 55
