#https://projecteuler.net/problem=53

def fac(n): return fac(n-1)*n if n >= 2 else 1
def comb(n,r): return fac(n)/(fac(r)*fac(n-r))

result = sum([ sum([(1 if comb(n,r)>1000000 else 0) for r in range(2,n-1)] ) for n in range(1,101) ])
print result

#solution: 4075
