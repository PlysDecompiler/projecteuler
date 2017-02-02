#https://projecteuler.net/problem=40

s = ''
i = 1
curexp = 0
digs = []
while True:
    s+=str(i)
    if len(s)>=10**curexp:
        digs.append(int(s[10**curexp-1]))
        curexp+=1
        if curexp == 7:
            break
    i += 1
print digs, reduce(lambda x,y: x*y, digs, 1)
#solution: 210
