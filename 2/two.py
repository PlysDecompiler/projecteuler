fiblist = [1,1]

while True:
    s = sum(fiblist[-2:])
    if s<=4000000:
        fiblist.append(s)
    else:
        break

solution = sum(fiblist[2::3])
print solution
#4613732
