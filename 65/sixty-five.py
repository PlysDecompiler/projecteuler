#https://projecteuler.net/problem=65

elist = []
for i in range(1,50):
    elist.extend([1,2*i,1])

convs = [2,3]

for e in elist[1:]:
    nextE = e*convs[-1]+convs[-2]
    convs.append(nextE)

print sum(int(i) for i in list(str(convs[99])))
#solution:  272
