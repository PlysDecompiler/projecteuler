#https://projecteuler.net/problem=29

alltehpowers = set()

for i in range(2,101):
    for j in range(2,101):
        alltehpowers.add(i**j)

print len(alltehpowers)
#solution: 9183
