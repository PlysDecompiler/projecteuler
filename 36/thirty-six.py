#https://projecteuler.net/problem=36

palin = []

for i in range(1,1000001,2):
    s = str(i) 
    if s == s[::-1]:
        b = bin(i)[2:]
        if b == b[::-1]:
            palin.append(i)

print sum(palin)
#solution: 872187
