#https://projecteuler.net/problem=45
import time

starttime = time.time()
d = {
    3: { 'fn': lambda n: (n*(n+1))/2, 'n': 1},
    5: { 'fn': lambda n: (n*(3*n-1))/2, 'n': 1},
    6: { 'fn': lambda n: (n*(2*n-1)), 'n': 1}
}

for edges in [3,5,6]:
    while d[edges]['fn'](d[edges]['n']) <= 40775:
        d[edges]['n']+=1

found = False
while not found:
    tph = d[6]['fn'](d[6]['n'])
    for ed in [5,3]:
        while d[ed]['fn'](d[ed]['n']) < tph:
            d[ed]['n'] += 1
        if d[ed]['fn'](d[ed]['n']) != tph:
            if ed == 5:
                d[3]['n'] = d[5]['n']
            break
        else:
            if ed == 3:
                print tph, d[3]['n'], d[5]['n'], d[6]['n']
                found = True
                break
    d[6]['n'] += 1
print time.time()-starttime
#solution: 1533776805
