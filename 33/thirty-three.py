#https://projecteuler.net/problem=33

fractions = {}

for i in range(11,100):
    for j in range(11,i):
        if '0' in str(i)+str(j):
            continue
        k = float(j)/i
        if k not in fractions:
            fractions[k] = []
        fractions[k].append((j,i))        

curious = set()
for k,v in fractions.iteritems():
    for frac in v:
        for c in str(frac[0]):
            if c in str(frac[1]):
                alist = list(str(frac[0]))
                alist.remove(c)
                numerator = int(alist[0])
                blist = list(str(frac[1]))
                blist.remove(c)
                denominator = float(blist[0])
                if numerator/denominator == k:
                    curious.add(frac)

print len(curious), curious
n = reduce(lambda x,y: x*y,[cur[0] for cur in curious],1)
d = reduce(lambda x,y: x*y,[cur[1] for cur in curious],1)

print d/n
#solution: 100
