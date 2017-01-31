#https://projecteuler.net/problem=38

maxi = 123456789
alldigits = str(maxi)

for i in range(1,10000):
    s = str(i)
    n = 2
    while len(s)<9:
        s+=str(n*i)
        n+=1
    if len(s) > 9:
        continue
    if all(d in s for d in alldigits):
        if int(s)>maxi:
            print 'i:', i, 's:', s
            maxi = int(s)
        
print maxi
#solution: 932718654
