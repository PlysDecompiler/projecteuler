#https://projecteuler.net/problem=12

def count_divisors(n):
    d = 0
    i = 1
    while i<=n/2+1:
        if n%i == 0:
            d+=1
        i+=1
    d+=1
    return d

j=4800
maxcdtri = 0
#for j in range(1,28):
while j<5000:
    tri = (j*(j+1))/2      #sum(range(1,j+1))
    cdtri = count_divisors(tri)
    if cdtri>maxcdtri:
        maxcdtri = cdtri    
    if cdtri > 500:
        print j, tri, cdtri        
        break
    j+=1
    #print j, tri, count_divisors(tri)

print maxcdtri
#solution: 
