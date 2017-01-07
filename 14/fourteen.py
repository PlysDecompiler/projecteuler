#https://projecteuler.net/problem=14

def nextnumber(i):
    if i%2:
        return 3*i+1
    else:
        return i/2

maxi = (0,0)
n = 1

while n < 1000000:
    chain = 1
    m = n
    while True:
        if m!=1:
            m = nextnumber(m)        
            chain+=1
        else:
            break
    if chain > maxi[0]:
        maxi = (chain, n)
    n+=1

print maxi
#solution: 837799
