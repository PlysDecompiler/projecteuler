#https://projecteuler.net/problem=55

lychrel = 0

for n in range(1,10000):
    s = str(n)
    for i in range(50):
        s = str(int(s)+int(s[::-1]))
        if s == s[::-1]:
            break
        
    else:
        lychrel+=1
        
print lychrel
#solution: 249
