#https://projecteuler.net/problem=56

maxi = 0

for a in range(100):
    for b in range(100):
        power = str(a**b)
        s = sum([int(i) for i in power])
        if s > maxi:
            maxi = s
print maxi

#solution: 972
