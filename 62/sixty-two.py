#https://projecteuler.net/problem=62

cubes = []
digits = '0123456789'
greatdict = {i: {} for i in range(3,15)}

for i in range(11,10000):
    cub = i**3
    cubes.append(cub)
    s = str(cub)
    digs = ''
    for d in digits:
        digs+=str(s.count(d))
    if digs not in greatdict[len(s)]:
        greatdict[len(s)][digs] = []
    greatdict[len(s)][digs].append(cub)

for i in range(3,15):
    pleasedel = []
    for k,v in greatdict[i].iteritems():
        if len(v)<5:
            pleasedel.append(k)
    for pd in pleasedel:
        del greatdict[i][pd]

possibles = []
for i in range(3,15):
    if len(greatdict[i].keys()):
        for k,v in greatdict[i].iteritems():
            possibles.extend(v)
            
print min(possibles)
#solution: 127035954683
