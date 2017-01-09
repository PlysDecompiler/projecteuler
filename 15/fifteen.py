#https://projecteuler.net/problem=15

gridsize = 20

theGrid = [[1 if (i==gridsize) != (j==gridsize) else None for j in range(gridsize+1)] for i in range(gridsize+1)]

for g in theGrid:
    print g

for i in range(gridsize-1, -1,-1):
    for j in range(gridsize-1, -1,-1):
        theGrid[i][j] = theGrid[i+1][j]+theGrid[i][j+1]

print theGrid[0][0]

#solution: 137846528820
