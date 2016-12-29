#https://projecteuler.net/problem=5

def fac(n):
    if n<=1: 
        return 1
    else:
        return fac(n-1)*n

test = 20

num = fac(test)
divlist = range(2,test+1)

for d in divlist:
    while True:
        ii = num    
        tr = num/d
        if any(tr%e for e in divlist):
            break
        else:
            num /= d 
        if ii==num:
            break

print "The number is:", num
#232792560
