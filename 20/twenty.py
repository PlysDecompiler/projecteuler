#https://projecteuler.net/problem=20

def fac(n):
    return n*fac(n-1) if n>=2 else 1

hundredfac = fac(100)
print sum([int(i) for i in list(str(hundredfac))])
#solution: 648
