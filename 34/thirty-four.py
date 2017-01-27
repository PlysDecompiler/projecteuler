#https://projecteuler.net/problem=34

def fac(n):
    return n*fac(n-1) if n >= 2 else 1 

curiouslist = []

for i in range(3,3000000):
    s = sum([fac(int(n)) for n in list(str(i))])
    if s==i:
        curiouslist.append(i)

print sum(curiouslist)
#solution: 47030
